## why doesnt DHCP use TCP

for handshake you need IP



## what is dhcp

DHCP consists of two components 

* a protocol for delivering host-specific configuration parameters from a
   DHCP server to a host 
   
* and a mechanism for allocation of network
   addresses to hosts.


## ip allocation via DHCP

DHCP supports three mechanisms for IP address allocation.  In
   "automatic allocation", DHCP assigns a permanent IP address to a
   client.  In "dynamic allocation", DHCP assigns an IP address to a
   client for a limited period of time (or until the client explicitly
   relinquishes the address).  In "manual allocation", a client's IP
   address is assigned by the network administrator, and DHCP is used
   simply to convey the assigned address to the client

   
## what all icmp can do?

 The Internet Control Message Protocol (ICMP) [16]
   provides for informing hosts of additional routers via "ICMP
   redirect" messages.  ICMP also can provide subnet mask information
   through the "ICMP mask request" message and other information through
   the (obsolete) "ICMP information request" message.  Hosts can locate
   routers through the ICMP router discovery mechanism [8].


## DHCP vs Bootp

There are two primary differences between DHCP and BOOTP.  

* DHCP defines mechanisms through which clients can be assigned a
network address for a finite lease, allowing for serial reassignment
of network addresses to different clients.

* DHCP provides the
mechanism for a client to acquire all of the IP configuration
parameters that it needs in order to operate.

   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |     op (1)    |   htype (1)   |   hlen (1)    |   hops (1)    |
   +---------------+---------------+---------------+---------------+
   |                            xid (4)                            |
   +-------------------------------+-------------------------------+
   |           secs (2)            |           flags (2)           |
   +-------------------------------+-------------------------------+
   |                          ciaddr  (4)                          |
   +---------------------------------------------------------------+
   |                          yiaddr  (4)                          |
   +---------------------------------------------------------------+
   |                          siaddr  (4)                          |
   +---------------------------------------------------------------+
   |                          giaddr  (4)                          |
   +---------------------------------------------------------------+
   |                                                               |
   |                          chaddr  (16)                         |
   |                                                               |
   |                                                               |
   +---------------------------------------------------------------+
   |                                                               |
   |                          sname   (64)                         |
   +---------------------------------------------------------------+
   |                                                               |
   |                          file    (128)                        |
   +---------------------------------------------------------------+
   |                                                               |
   |                          options (variable)                   |
   +---------------------------------------------------------------+


 FIELD      OCTETS       DESCRIPTION
   -----      ------       -----------

   op            1  Message op code / message type.
                    1 = BOOTREQUEST, 2 = BOOTREPLY
   htype         1  Hardware address type, see ARP section in "Assigned
                    Numbers" RFC; e.g., '1' = 10mb ethernet.
   hlen          1  Hardware address length (e.g.  '6' for 10mb
                    ethernet).
   hops          1  Client sets to zero, optionally used by relay agents
                    when booting via a relay agent.
   xid           4  Transaction ID, a random number chosen by the
                    client, used by the client and server to associate
                    messages and responses between a client and a
                    server.
   secs          2  Filled in by client, seconds elapsed since client
                    began address acquisition or renewal process.
   flags         2  Flags (see figure 2).
   ciaddr        4  Client IP address; only filled in if client is in
                    BOUND, RENEW or REBINDING state and can respond
                    to ARP requests.
   yiaddr        4  'your' (client) IP address.
   siaddr        4  IP address of next server to use in bootstrap;
                    returned in DHCPOFFER, DHCPACK by server.
   giaddr        4  Relay agent IP address, used in booting via a
                    relay agent.
   chaddr       16  Client hardware address.
   sname        64  Optional server host name, null terminated string.
   file        128  Boot file name, null terminated string; "generic"
                    name or null in DHCPDISCOVER, fully qualified
                    directory-path name in DHCPOFFER.
   options     var  Optional parameters field.  See the options
                    documents for a list of defined options.


## whats new in DHCP - client identifier

DHCP defines a new 'client identifier' option that is used to pass an
   explicit client identifier to a DHCP server

The 'client identifier' chosen by a
   DHCP client MUST be unique to that client within the subnet to which
   the client is attached. If the client uses a 'client identifier' in
   one message, it MUST use that same identifier in all subsequent
   messages, to ensure that all servers correctly identify the client.


## siaddr

A DHCP server always returns its own address in the 'server
   identifier' option.


## DHCP before TCP/IP - significance of broadcast bit

The TCP/IP software SHOULD accept and
   forward to the IP layer any IP packets delivered to the client's
   hardware address before the IP address is configured; DHCP servers
   and BOOTP relay agents may not be able to deliver DHCP messages to
   clients that cannot accept hardware unicast datagrams before the
   TCP/IP software is configured.


 To work around some clients that cannot accept IP unicast datagrams
   before the TCP/IP software is configured as discussed in the previous
   paragraph, DHCP uses the 'flags' field [21].  The leftmost bit is
   defined as the BROADCAST (B) flag.


## DHCP parameter repository - usecase 1

The first service provided by DHCP is to provide persistent storage
   of network parameters for network clients.  The model of DHCP
   persistent storage is that the DHCP service stores a key-value entry
   for each client, where the key is some unique identifier (for
   example, an IP subnet number and a unique identifier within the
   subnet) and the value contains the configuration parameters for the
   client.

The protocol defines
   that the key will be (IP-subnet-number, hardware-address) unless the
   client explicitly supplies an identifier using the 'client
   identifier' option.



## Allocation of Network Address - usecase 2


 As a consistency check - for reused addresses, the allocating
   server SHOULD probe the reused address before allocating the address,
   e.g., with an ICMP echo request, and the client SHOULD probe the
   newly received address, e.g., with ARP.

## dhcp options


One particular option -
   the "DHCP message type" option - must be included in every DHCP
   message.  This option defines the "type" of the DHCP message.


## DHCP Message types


   Message         Use
   -------         ---

   DHCPDISCOVER -  Client broadcast to locate available servers.

   DHCPOFFER    -  Server to client in response to DHCPDISCOVER with
                   offer of configuration parameters.

   DHCPREQUEST  -  Client message to servers either (a) requesting
                   offered parameters from one server and implicitly
                   declining offers from all others, (b) confirming
                   correctness of previously allocated address after,
                   e.g., system reboot, or (c) extending the lease on a
                   particular network address.

   DHCPACK      -  Server to client with configuration parameters,
                   including committed network address.

   DHCPNAK      -  Server to client indicating client's notion of network
                   address is incorrect (e.g., client has moved to new
                   subnet) or client's lease as expired

   DHCPDECLINE  -  Client to server indicating network address is already
                   in use.

   DHCPRELEASE  -  Client to server relinquishing network address and
                   cancelling remaining lease.

   DHCPINFORM   -  Client to server, asking only for local configuration
                   parameters; client already has externally configured
                   network address.



## allocating network address for new client

1. The DHCPDISCOVER message MAY include options that suggest
      values for the network address and lease duration

2. Each server may respond with a DHCPOFFER message that includes an
      available network address in the 'yiaddr' field (and other
      configuration parameters in DHCP options)

   the server may probe the offered address
      with an ICMP Echo Request - admins can disable probe

3. selection of DHCP server amongst multiple servers and DHCP request

The client receives one or more DHCPOFFER messages from one or more
     servers.  The client may choose to wait for multiple responses.
     The client chooses one server from which to request configuration
     parameters, based on the configuration parameters offered in the
     DHCPOFFER messages.  The client broadcasts a DHCPREQUEST message
     that MUST include the 'server identifier' option to indicate which
     server it has selected

 The 'requested IP
     address' option MUST be set to the value of 'yiaddr' in the
     DHCPOFFER message from the server.

The client times out and retransmits the DHCPDISCOVER message if
     the client receives no DHCPOFFER messages.

4. The server selected in the DHCPREQUEST message commits the
     binding for the client to persistent storage and responds with a
     DHCPACK message containing the configuration parameters for the
     requesting client

The server SHOULD NOT check the offered
     network address at this point - check happpened in step-2

 If the selected server is unable to satisfy the DHCPREQUEST message
     (e.g., the requested network address has been allocated), the
     server SHOULD respond with a DHCPNAK message.

The client receives the DHCPACK message with configuration
     parameters.  The client SHOULD perform a final check on the
     parameters (e.g., ARP for allocated network address), and notes the
     duration of the lease specified in the DHCPACK message

If the client detects that the
     address is already in use (e.g., through the use of ARP), the
     client MUST send a DHCPDECLINE message

The client may choose to relinquish its lease on a network address
     by sending a DHCPRELEASE message to the server.  The client
     identifies the lease to be released with its 'client identifier',
     or 'chaddr' and network address in the DHCPRELEASE message. If the
     client used a 'client identifier' when it obtained the lease, it
     MUST use the same 'client identifier' in the DHCPRELEASE message.


## indentifier in DHCP msgs

The combination of 'client identifier' or
     'chaddr' and assigned network address constitute a unique
     identifier for the client's lease and are used by both the client
     and server to identify a lease referred to in any DHCP messages.


## when to check for availibility of IP address offered to the client

Any configuration parameters in the DHCPACK message SHOULD NOT
     conflict with those in the earlier DHCPOFFER message to which the
     client is responding.  The server SHOULD NOT check the offered
     network address at this point. The 'yiaddr' field in the DHCPACK
     messages is filled in with the selected network address.


## what if server is unable to satify DHCP request

     If the selected server is unable to satisfy the DHCPREQUEST message
     (e.g., the requested network address has been allocated), the
     server SHOULD respond with a DHCPNAK message.

## is DHCP Request  - unicast or broadcast

A client that cannot receive unicast IP datagrams until its protocol software has been configured with an IP address SHOULD set the BROADCAST bit in the 'flags' field to 1 in any DHCPDISCOVER or DHCPREQUEST messages that client sends. The BROADCAST bit will provide a hint to the DHCP server and BOOTP relay agent to broadcast any messages to the client on the client's subnet

## when DHCP decline occur?

If the client detects that the
     address is already in use (e.g., through the use of ARP), the
     client MUST send a DHCPDECLINE message to the server and restarts
     the configuration process

## Reusing a previously allocated network address

The client broadcasts a DHCPREQUEST message on its local subnet.
      The message includes the client's network address in the
      'requested IP address' option. As the client has not received its
      network address, it MUST NOT fill in the 'ciaddr' field


### DHCPNAK in the resuing case

If the client's request is invalid (e.g., the client has moved
      to a new subnet), servers SHOULD respond with a DHCPNAK message to
      the client. Servers SHOULD NOT respond if their information is not
      guaranteed to be accurate.  For example, a server that identifies a
      request for an expired binding that is owned by another server SHOULD
      NOT respond with a DHCPNAK unless the servers are using an explicit
      mechanism to maintain coherency among the servers.

## DHCPNAK(if client has misconfig), how to convey? 


      If 'giaddr' is 0x0 in the DHCPREQUEST message, the client is on
      the same subnet as the server.  The server MUST
      broadcast the DHCPNAK message to the 0xffffffff broadcast address
      because the client may not have a correct network address or subnet
      mask, and the client may not be answering ARP requests.
      Otherwise, the server MUST send the DHCPNAK message to the IP
      address of the BOOTP relay agent, as recorded in 'giaddr'.  The
      relay agent will, in turn, forward the message directly to the
      client's hardware address, so that the DHCPNAK can be delivered even
      if the client has moved to a new network.

## when does client go to bound state

If the client
      receives neither a DHCPACK or a DHCPNAK message after employing
      the retransmission algorithm, the client MAY choose to use the
      previously allocated network address and configuration parameters
      for the remainder of the unexpired lease.  This corresponds to
      moving to BOUND state in the client state transition diagram shown
      in figure 5.


## obtaining parameters from external - DHCPINFORM unicast

Servers receiving a
   DHCPINFORM message construct a DHCPACK message with any local
   configuration parameters appropriate for the client without:
   allocating a new address, checking for an existing binding, filling
   in 'yiaddr' or including lease time parameters.  The servers SHOULD
   unicast the DHCPACK reply to the address given in the 'ciaddr' field
   of the DHCPINFORM message.
    
## Client parameters - what all client sends and what all it  requests

First, most of
   the parameters have defaults defined in the Host Requirements RFCs;
   if the client receives no parameters from the server that override
   the defaults, a client uses those default values

   The client can inform the server which configuration parameters the
   client is interested in by including the 'parameter request list'
   option.  The data portion of this option explicitly lists the options
   requested by tag number.





### what if parameters size exceed?

 The parameters returned to a client may still exceed the space
   allocated to options in a DHCP message.  In this case, two additional
   options flags (which must appear in the 'options' field of the
   message) indicate that the 'file' and 'sname' fields are to be used
   for options.


## requesting for particular IP and lease time

   In addition, the client may suggest values for the network address
   and lease time in the DHCPDISCOVER message.  The client may include
   the 'requested IP address' option to suggest that a particular IP
   address be assigned, and may include the 'IP address lease time'
   option to suggest the lease time it would like.


## how are error msgs included

The server may include an error message in the
   'message' option.

## Transport layer of DHCP

   DHCP uses UDP as its transport protocol.  DHCP messages from a client
   to a server are sent to the 'DHCP server' port (67), and DHCP
   messages from a server to a client are sent to the 'DHCP client' port
   (68). A server with multiple network address (e.g., a multi-homed
   host) MAY use any of its network addresses in outgoing DHCP messages.

## server identifier

 DHCP clients MUST
   use the IP address provided in the 'server identifier' option for any
   unicast requests to the DHCP server



