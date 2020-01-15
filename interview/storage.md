# Storage Architecture

## Centralized Storage Advantages

* Management

    * Easy to manage all the storages 

* Disk utilization

    * Centralized pool to slice up and distribute storage

    * Change of disk space is non distructive

    * Thin Provisioning

        * To give the appearance of having more physical resources than are actually available. 
        
        * If a system always has enough resource to simultaneously support all of the virtualized resources, then it is not thin provisioned

    * Deduplication and Compression

        * Is a process that eliminates redundant copies of data and reduces storage overhead.

    * Boot - Diskless server (using SAN protocol)

    * Storage Tiering -Support for Moving from HOT to cold and archives

    * Resiliency 

        * Disk failure - by RAID, disk shelf failure - by mirroring, contoller failure - by multi-controller

    * snapshot - point in time copy of filesystem

## NAS

* File level access to storage system

* Mgmt of Fs resides with the storage system

* Uses exiting data architecture, no need to put seperate network for storage

## NAS Protocols

## CIFS (Common Internet File System)

* A version of SMB, CIFS - Microsoft, SMB - UNIX based

* Servers - share the storage, clients - map to that share

    * Ex - \\172.16.31.14\share


## NFS

* Servers - Export and clients - Mount 

    * Ex - mount storage:/sales mnt/sales

## SAN

* Block level access

* Mgmt of Fs resides with Client, client has to format the storage before it can use it

* Dedicated storage network (typical)

* Boot from SAN is available


## SAN Protocols

### SAN Terminology

* **LUN** - Represents a disk presented to a host

    * Client sees the LUN as if it was a local Hard Drive

    * client - initiator, storage system - Target

## Fibre Channel

* Fibre Channel is the original SAN protocol, and is still very popularIt uses dedicated adapters, cables and switches and is different than Ethernet at all layers of the OSI stack, including the physical level

* FCP is used to send SCSI commands over the Fibre Channel network

* Fibre channel is a very stable and reliable protocolIt is lossless, unlike TCP and UDP

* It supports bandwidths of 2, 4, 6, 8 and 16 Gbps


Some storages support both SAN and NAS protocols

## VSA



## Nutanix 


controller CPU bottleneck, scalability(if storage array hits saturation - we would need a new one), 

pros - data locality, SSD, HDD

3 levels of cache - in memory cache, ssd flash, HDD

Nutanix Distributed file system - scale up FS (as a data store)

3 - 3 
5 - reasoning
7
8 - reasoning
9