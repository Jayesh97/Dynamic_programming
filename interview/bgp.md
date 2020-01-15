# BGP


 We have connectivity because of the default routes but this can lead to sub-optimal routing

  If we look at AS 1 then we have a lot of different paths we can take to reach network 192.168.9.0 /24 in AS 9.

Does this mean the network administrator at AS 1 can choose the path we are going to use? Not really because of the following reasons:

You can choose the exit path…AS1 can send traffic to AS 2 or AS4 but you don’t make routing decisions for other autonomous systems.
Each autonomous system will only advertise the best path to your autonomous system. AS 1 will only learn about the best path from AS 2 and AS 4 unless their best path fails…only then you will learn about the second best path.
BGP uses a set of BGP attributes to select a path


update source loback to tell thats the source of the connection

for a router to install a prefix, next hop must be reachable

max paths command

## internview questions in bgp?

bgp conf, bgp route ref rules
arp in ipv4 and ipv6
ibpg and ebgp non loops, internal packets
bgp load balancing inbound and outbound
dup acks, neg acks
why there is slow communication between the server and cliet(tell in perspective of bgp)
update source loopback 0 why??

### types of Routing protocols?

routing protocols used today are based on one of two types of
distributed routing algorithms: link-state or distance vectorv


### Disadvantages of Distance vector?

* lower hop path might have low Bw

* not more than 15 hops - solved

* Propagation of the
path failure would be suppressed until the refresh timer expired, thereby slowing convergence
considerably. - solved by new versions through triggered updates

### count to infinity problem

In addition to the standard distance vector properties, BGP employs an additional
mechanism referred to as the path vector, used to avoid the count to infinity problem

### what is AS?

An autonomous system (AS) is a set of routers that has a single routing policy, that run under
a single technical administration, and that commonly utilizes a single IGP

#### Stub As

An AS is considered stub when it reaches networks outside its domain via a single exit point.
These ASs are also referred to as single-homed with respect to other providers.

### how isp learns routes from customers

ISP can learn and advertise the customer's routes is to use
BGP between the customer and the provider.


## BGP

### which port bgp uses

BGP uses TCP port 179 to communicate with other routers

### how does bgp know ipv4 or ipv6

Address family information

### option fields in open msgs

capability - multipprotocol extension capability, tcp auth

### prefix length for classless

in NLRI prefix lenght indicates the network bits

## how do you know which attribute

path attribute -> flags

## types of well known and optional attributes

well known desc

## read this

https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/26634-bgp-toc.html


https://whatismyipaddress.com/ipv6-questions



communities, states, active
tcp - slow

add strings - decimal, infinite

pressure, 

bgp tells the path attributes and the n