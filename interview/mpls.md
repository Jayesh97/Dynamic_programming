ISP is running eBGP between the CE (Customer Edge) and PE (Provider Edge) to exchange prefixes. This means all internal (P) routers of the ISP have to run iBGP or they don’t know where to forward their packets to.

All routers have to do lookups in the routing table for any possible destination.

when our goal is to have connectivity between two customer sites, why should all internal P routers know about this? The only routers that need to know how to reach the customer sites are the PE routers of the provider. Why not build a tunnel between the PE routers

What does multi protocol label switching mean?

Multi protocol: besides IP you can tunnel pretty much anything…IP, IPv6, Ethernet, PPP, frame-relay, etc.
Label switching: forwarding is done based on labels, not by looking up the destination in the routing table.

## tunneling way

The outer IP header has source address 2.2.2.2 and destination address 4.4.4.4, the P router knows how to route these since it learned these addresses through OSPF.


## mpls fields

Label value: the name says it all, this is where you will find the value of the label.

EXP: these are the three experimental bits. These are used for QoS, normally the IP precedence value of the IP packet will be copied here.

S: this is the “bottom of stack” bit. With MPLS it’s possible to add more than one label, you’ll see why in some of the MPLS VPN lessons. When this bit is set to one, it’s the last MPLS header. When it’s set to zero then there is one or more MPLS headers left.

TTL: just like in the IP header, this is the time to live field. You you can use this for traces in the MPLS network. Each hop decrements the TTL by one.


P3 receives the labeled packet and will pop the label, forwarding the IP packet to PE2. This is called penultimate hop popping and is performed to save PE2 the trouble of looking at the MPLS label

# LDP

LDP is a protocol that automatically generates and exchanges labels between routers. Each router will locally generate labels for its prefixes and will then advertise the label values to its neighbors.

 LDP first establishes a neighbor adjacency before it exchanges label information

First we send UDP multicast hello packets to discover other neighbors. Once two routers decide to become neighbors, they build the neighbor adjacency using a TCP connection. This connection is then used for the exchange of label information.

## udp multicast hello - src 646 dest 646

Within this hello packet, they will advertise a transport IP address. This IP address is then used to establish the TCP connection between the two routers

The hello packets are sent to multicast address 224.0.0.2 using source/destination UDP port 646

note :- Make sure that the IP address that LDP has selected for the transport address is advertised in your routing protocol. Otherwise your routers will be able to hear each others hello packets but they can’t form a neighbor adjacency since the transport address(es) are unreachable.

### how neighbor adj is diff from ospf

when you run OSPF then your routers will form neighbor adjacencies on all interfaces that run OSPF:
LDP will only form a single neighbor adjacency, no matter how many interfaces you have in between your routers:


### source as loopback

LDP is a bit similar to BGP when you use the loopback interfaces for the neighbor adjacency. When we use BGP we have to use the update-source command to select the source, LDP does it automatically.

### LIB = RIB

When we use LDP on Cisco IOS, we locally generate a label for each prefix that we can find in the RIB, except for BGP prefixes. This information is then added to the LIB (Label Information Base).

The information in the LIB is used to build the LFIB (Label Forwarding Information Base). When the router has to forward a packet with a MPLS label on it, it will use the LFIB for forwarding decisions.

Two routers that have formed a LDP neighbor adjacency will exchange the label information in their LIBs to tell each other what label values to use for different prefixes.

## LDP configure

There are two ways to configure LDP:

On the interface level with the mpls ip command.
Globally under the OSPF process with the mpls ldp autoconfig command.

## verifying LDP configuration

The show mpls interfaces command is a quick way to see if LDP is enabled or not. It tells us what interfaces are enabled and if they are operational or not.



## MPLS control plane

When you use LDP, all routers will start assigning labels with label value 16. This might be a bit annoying if you are new to MPLS as some routers will use the same label value. To make it easier to read the different tables I will configure each router to use different label values.


The LFIB is much smaller, keep in mind that this is similar to the CEF table that we use for IP forwarding. There is no entry for 1.1.1.1 /32 or 192.168.12.0 /24 here since we don’t have a label for these prefixes.

