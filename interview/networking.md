# Vlan

VLAN is a single broadcast domain

Static VLANs offer port-based membership, in which switch ports are assigned to specific
VLANs. End-user devices become members in a VLAN based on the physical switch
port to which they are connected. No handshaking or unique VLAN membership protocol
is needed for the end devices; they automatically assume


To perform this function, you could use either a Layer 3 device to route packets or an external Layer 2 device
to bridge packets between the two VLANs. The static port-to-VLAN membership normally is handled in hardware with applicationspecific
integrated circuits (ASIC) in the switch

The VLAN Trunking Protocol (VTP) uses the VLAN database so that VLAN definitions
can be advertised and shared between switches over trunk links. When extended-range
VLANs are created, they are not stored in the VLAN database file

VLAN number
can be 1 to 4094

As long as the switch remains in VTP transparent mode, the extended
VLANs can be used. However, if the switch is later configured to participate in VTP
as either a server or a client, you must manually delete the extended VLANs. For any switch
ports that were assigned to the extended VLANs, you also must reconfigure them for
VLAN membership within the normal VLAN range.

Dynamic VLANs provide membership based on the MAC address of an end-user device.
When a device is connected to a switch port, the switch must, in effect, query a database
to establish VLAN membership. A network administrator also must assign the user’s
MAC address to a VLAN in the database of a VLAN Membership Policy Server (VMPS).


## end-to-end vlans


End-to-end VLANs should group users according to common requirements. All users in a
VLAN should have roughly the same traffic flow patterns, following the 80/20 rule.

Because all VLANs must be available at each access-layer switch, VLAN trunking must be
used to carry all VLANs between the access- and distribution-layer switches

End-to-end VLANs are not recommended in an enterprise network, unless there is a
good reason. In an end-to-end VLAN, broadcast traffic is carried over from one end of the
network to the other, creating the possibility for a broadcast storm or Layer 2 bridging
loop to spread across the whole extent of a VLAN. This can exhaust the bandwidth of distribution-
and core-layer links, as well as switch CPU resources


## Local Vlans

The 20/80 rule

Arranging VLANs in this fashion enables the Layer 3 function in the campus
network to intelligently handle the interVLAN traffic loads, where traffic passes into
the core. This scenario provides maximum availability by using multiple paths to destinations,
maximum scalability by keeping the VLAN within a switch block, and maximum
manageability

### trunk links

A trunk link, however, can transport more than one VLAN through a single switch port.
Trunk links are most beneficial when switches are connected to other switches or switches
are connected to routers. A trunk link is not assigned to a specific VLAN. Instead, one,
many, or all active VLANs can be transported between switches using a single physical
trunk link.

### vlan tagging

If frames must be transported out another trunk link, the VLAN identifier is added back
into the frame header. 

Otherwise, if frames are destined out an access (nontrunk) link, the
switch removes the VLAN identifier before transmitting the frames to the end station.
Therefore, all traces of VLAN association are hidden from the end station.

The IEEE 802.1Q protocol also can carry VLAN associations over trunk links.However, instead of encapsulating each frame with a VLAN ID header and trailer,802.1Q embeds its tagging information within the Layer 2 frame. This method is referred
to as single tagging or internal tagging.  -4byte 

The first two bytes are used as a Tag Protocol Identifier (TPID) and always have a value of
0x8100 to signify an 802.1Q tag. The remaining two bytes are used as a Tag Control Information
(TCI) field. The TCI information contains a three-bit Priority field, which is used to
implement class-of-service (CoS) functions in the accompanying 802.1Q/802.1p prioritization
standard. One bit of the TCI is a Canonical Format Indicator (CFI), flagging whether
the MAC addresses are in Ethernet or Token Ring format. (This also is known as canonical
format, or little-endian or big-endian format.)
The last 12 bits are used as a VLAN identifier (VID) to indicate the source VLAN for the
frame. The VID can have values from 0 to 4095, but VLANs 0, 1, and 4095 are reserved.

## trunk modes

trunk - The trunk mode is usually used to establish an unconditional trunk

dynamic desirable (the default)—The port actively attempts to convert the link
into trunking mode. In other words, it “asks” the far-end switch to bring up a trunk. If
the far-end switch port is configured to trunk, dynamic desirable, or dynamic auto
mode, trunking is negotiated successfully.

dynamic auto—The port can be converted into a trunk link, but only if the far-end
switch actively requests it. Therefore, if the far-end switch port is configured to trunk
or dynamic desirable mode, trunking is negotiated. Because of the passive negotiation
behavior, the link never becomes a trunk if both ends of the link are left to the
dynamic auto default.


## VTP

The VLAN
Trunking Protocol (VTP) uses Layer 2 trunk frames to communicate VLAN information
among a group of switches. VTP manages the addition, deletion, and renaming of VLANs
across the network from a central point of control. Any switch participating in a VTP exchange
is aware of and can use any VLAN that VTP manages.

## vtp domains

VTP is organized into management domains, or areas with common VLAN requirements.
A switch can belong to only one VTP domain, in addition to sharing VLAN information
with other switches in the domain. Switches in different VTP domains, however, do not
share VTP information.
Switches in a VTP domain advertise several attributes to their domain neighbors. Each advertisement
contains information about the VTP management domain, VTP revision number,
known VLANs, and specific VLAN parameters. When a VLAN is added to a switch
in a management domain, other switches are notified of the new VLAN through VTP advertisements.
In this way, all switches

### server mode

Server mode—VTP servers have full control over VLAN creation and modification
for their domains. All VTP information is advertised to other switches in the domain,
while all received VTP information is synchronized with the other switches. By default,
a switch is in VTP server mode. Note that each VTP domain must have at least
one server so that VLAN

### Client mode

VTP clients do not allow the administrator to create, change, or
delete any VLANs. Instead, they listen to VTP advertisements from other switches
and modify their VLAN configurations accordingly. In effect, this is a passive listening
mode. Received VTP information is forwarded out trunk links to neighboring
switches in the domain, so the switch also acts as a VTP relay

### transparent mode


While a switch is in VTP transparent mode, it can create and delete VLANs that are
local only to itself. These VLAN changes, however, are not propagated to any other switch.


# STP

STP operates as switches communicate with one another. Data messages are exchanged in
the form of bridge protocol data units (BPDU). A switch sends a BPDU frame out a port,
using the unique MAC address of the port itself as a source address. The switch is unaware
of the other switches around it, so BPDU frames are sent with a destination address
of the well-known STP multicast address 01-80-c2-00-00-00.


Two types of BPDU exist:

*  Configuration BPDU, used for spanning-tree computation

*  Topology Change Notification (TCN) BPDU, used to announce changes in the network
topology

STP decisions are based on the following sequence of four conditions:
1. Lowest root bridge ID
2. Lowest root path cost to root bridge
3. Lowest sender bridge ID
4. Lowest sender port ID

## stp port states

The STP port states are as follows:

Disabled—Ports that are administratively shut down by the network administrator

Blocking—After a port initializes, it begins in the Blocking state so that no bridging
loops can form. In the Blocking state, a port cannot receive or transmit data and cannot
add MAC addresses to its address table. Instead, a port is allowed to receive only
BPDUs so that the switch can hear from other neighboring switches.

Listening - In the Listening state, the port still cannot send or receive data frames. However, the
port is allowed to receive and send BPDUs so that it can actively participate in the
Spanning Tree topology process.

Learning—After a period of time called the Forward Delay in the Listening state,
the port is allowed to move into the Learning state. The port still sends and receives
BPDUs as before. In addition, the switch now can learn new MAC addresses to add to
its address table. The port cannot yet send any data frames, however.

## STP timers

Hello Interval between configuration BPDUs.

Forward Delay Time spent in Listening and Learning states before transitioning
toward Forwarding state.

Max Age Maximum length of time a BPDU can be stored without receiving
an update. Timer expiration signals an indirect failure
with designated or root bridge.

## TCN BPDU

TCN BPDU carries no data about the change but informs recipients only
that a change has occurred. Also notice that the switch will not send TCN BPDUs if the
port has been configured with PortFast enabled.


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



# SNMP

Simple Network Management Protocol (SNMP) is an application–layer protocol

It is a part of Transmission Control Protocol⁄Internet Protocol (TCP⁄IP) protocol suite.

## SNMP Manager

A manager or management system is a separate entity that is responsible to communicate with the SNMP agent implemented network devices. This is typically a computer that is used to run one or more network management systems.

SNMP Manager’s key functions
* Queries agents
* Gets responses from agents
* Sets variables in agents
* Acknowledges asynchronous events from agents

## Managed Devices

A managed device or the network element is a part of the network that requires some form of monitoring and management e.g. routers, switches, servers, workstations, printers, UPSs, etc...


## SNMP agent

The agent is a program that is packaged within the network element. Enabling the agent allows it to collect the management information database from the device locally and makes it available to the SNMP manager, when it is queried for. These agents could be standard (e.g. Net-SNMP) or specific to a vendor (e.g. HP insight agent)

SNMP agent’s key functions

*   Collects management information about its local environment
*   Stores and retrieves management information as defined in the MIB.
*   Signals an event to the manager.
*   Acts as a proxy for some non–SNMP manageable network node.

## Management information base (MIB)

Every SNMP agent maintains an information database describing the managed device parameters. The SNMP manager uses this database to request the agent for specific information and further translates the information as needed for the Network Management System (NMS). This commonly shared database between the Agent and the Manager is called Management Information Base (MIB).

MIB files are the set of questions that a SNMP Manager can ask the agent. Agent collects these data locally and stores it, as defined in the MIB. So, the SNMP Manager should be aware of these standard and private questions for every type of agent.


The MIBs comprises of managed objects identified by the name Object Identifier (Object ID or OID).

There are two types of Managed Object or Object ID: Scalar and Tabular. They could be better understandable with an example

Scalar: Device’s vendor name, the result can be only one. (As definition says: "Scalar Object define a single object instance")

Tabular: CPU utilization of a Quad Processor, this would give me a result for each CPU separately, means there will be 4 results for that particular Object ID. (As definition says: "Tabular object defines multiple related object instance that are grouped together in MIB tables")


Every Object ID is organized hierarchically in MIB. The MIB hierarchy can be represented in a tree structure with individual variable identifier.

A typical object ID will be a dotted list of integers. For example, the OID in RFC1213 for "sysDescr" is .1.3.6.1.2.1.1.1

## snmp commands

The simplicity in information exchange has made the SNMP as widely accepted protocol. The main reason being concise set of commands, here are they listed below:

GET: The GET operation is a request sent by the manager to the managed device. It is performed to retrieve one or more values from the managed device.
GET NEXT: This operation is similar to the GET. The significant difference is that the GET NEXT operation retrieves the value of the next OID in the MIB tree.
GET BULK: The GETBULK operation is used to retrieve voluminous data from large MIB table.
SET: This operation is used by the managers to modify or assign the value of the Managed device.
TRAPS: Unlike the above commands which are initiated from the SNMP Manager, TRAPS are initiated by the Agents. It is a signal to the SNMP Manager by the Agent on the occurrence of an event.
INFORM: This command is similar to the TRAP initiated by the Agent, additionally INFORM includes confirmation from the SNMP manager on receiving the message.
RESPONSE: It is the command used to carry back the value(s) or signal of actions directed by the SNMP Manager.








