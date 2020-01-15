

<image>

## Is ICMP part of IP ?

ICMP uses the basic support of IP as if it were a higher level protocol, however, ICMP is actually an integral part of IP. Although ICMP messages are contained within standard IP packets, ICMP messages are usually processed as a special case, distinguished from normal IP processing

ICMP is directly linked to the IP header, which is marked by the protocol number 1 or 58 (ICMPv6) in the IP field “protocol”



## what situations are icmp sent ?

 The ICMP messages typically report errors in the processing of
   datagrams

ICMP messages are sent in several situations:  

1. for example, when a
   datagram cannot reach its destination, 
   
2. when the gateway does not have
   the buffering capacity to forward a datagram, and 
   
3. when the gateway
   can direct the host to send traffic on a shorter route.

## icmp for icmp ?

no ICMP messages are sent about ICMP messages - to avoid the infinite regress of messages about messages

## reliability ?

Higher level protocols are responsible for the reliability, IP doesnt provide reliability

## icmp for fragments?

Also ICMP
   messages are only sent about errors in handling fragment zero of
   fragemented datagrams.  (Fragment zero has the fragment offeset equal
   zero).


## icmp format?

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |     Type      |     Code      |          Checksum             |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                             unused                            |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |      Internet Header + 64 bits of Original Data Datagram      |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


## why 64 bits of data / how the host matches the data?

If a higher level protocol
      uses port numbers, they are assumed to be in the first 64 data
      bits of the original datagram's data.


## icmp fields and types

   ICMP Fields:

   Type

      3

   Code

      0 = net unreachable;

      1 = host unreachable;

      2 = protocol unreachable;

      3 = port unreachable;

      4 = fragmentation needed and DF set;

      5 = source route failed.





