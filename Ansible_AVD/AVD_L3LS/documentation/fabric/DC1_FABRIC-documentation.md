# DC1_FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| DC1_FABRIC | l3leaf | DC1-BL1 | 10.88.169.133/24 | cEOS | Provisioned | - |
| DC1_FABRIC | l3leaf | DC1-BL2 | 10.88.169.134/24 | cEOS | Provisioned | - |
| DC1_FABRIC | l3leaf | DC1-CL1 | 10.88.169.135/24 | cEOS | Provisioned | - |
| DC1_FABRIC | l3leaf | DC1-CL2 | 10.88.169.136/24 | cEOS | Provisioned | - |
| DC1_FABRIC | l3leaf | DC1-CL3 | 10.88.169.137/24 | cEOS | Provisioned | - |
| DC1_FABRIC | l3leaf | DC1-CL4 | 10.88.169.138/24 | cEOS | Provisioned | - |
| DC1_FABRIC | spine | DC1-SP1 | 10.88.169.131/24 | cEOS | Provisioned | - |
| DC1_FABRIC | spine | DC1-SP2 | 10.88.169.132/24 | cEOS | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | DC1-BL1 | Ethernet1 | spine | DC1-SP1 | Ethernet5 |
| l3leaf | DC1-BL1 | Ethernet2 | spine | DC1-SP2 | Ethernet5 |
| l3leaf | DC1-BL1 | Ethernet8 | mlag_peer | DC1-BL2 | Ethernet8 |
| l3leaf | DC1-BL2 | Ethernet1 | spine | DC1-SP1 | Ethernet6 |
| l3leaf | DC1-BL2 | Ethernet2 | spine | DC1-SP2 | Ethernet6 |
| l3leaf | DC1-CL1 | Ethernet1 | spine | DC1-SP1 | Ethernet1 |
| l3leaf | DC1-CL1 | Ethernet2 | spine | DC1-SP2 | Ethernet1 |
| l3leaf | DC1-CL1 | Ethernet8 | mlag_peer | DC1-CL2 | Ethernet8 |
| l3leaf | DC1-CL2 | Ethernet1 | spine | DC1-SP1 | Ethernet2 |
| l3leaf | DC1-CL2 | Ethernet2 | spine | DC1-SP2 | Ethernet2 |
| l3leaf | DC1-CL3 | Ethernet1 | spine | DC1-SP1 | Ethernet3 |
| l3leaf | DC1-CL3 | Ethernet2 | spine | DC1-SP2 | Ethernet3 |
| l3leaf | DC1-CL3 | Ethernet8 | mlag_peer | DC1-CL4 | Ethernet8 |
| l3leaf | DC1-CL4 | Ethernet1 | spine | DC1-SP1 | Ethernet4 |
| l3leaf | DC1-CL4 | Ethernet2 | spine | DC1-SP2 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.16.1.0/24 | 256 | 24 | 9.38 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC1-BL1 | Ethernet1 | 172.16.1.129/31 | DC1-SP1 | Ethernet5 | 172.16.1.128/31 |
| DC1-BL1 | Ethernet2 | 172.16.1.131/31 | DC1-SP2 | Ethernet5 | 172.16.1.130/31 |
| DC1-BL2 | Ethernet1 | 172.16.1.161/31 | DC1-SP1 | Ethernet6 | 172.16.1.160/31 |
| DC1-BL2 | Ethernet2 | 172.16.1.163/31 | DC1-SP2 | Ethernet6 | 172.16.1.162/31 |
| DC1-CL1 | Ethernet1 | 172.16.1.1/31 | DC1-SP1 | Ethernet1 | 172.16.1.0/31 |
| DC1-CL1 | Ethernet2 | 172.16.1.3/31 | DC1-SP2 | Ethernet1 | 172.16.1.2/31 |
| DC1-CL2 | Ethernet1 | 172.16.1.33/31 | DC1-SP1 | Ethernet2 | 172.16.1.32/31 |
| DC1-CL2 | Ethernet2 | 172.16.1.35/31 | DC1-SP2 | Ethernet2 | 172.16.1.34/31 |
| DC1-CL3 | Ethernet1 | 172.16.1.65/31 | DC1-SP1 | Ethernet3 | 172.16.1.64/31 |
| DC1-CL3 | Ethernet2 | 172.16.1.67/31 | DC1-SP2 | Ethernet3 | 172.16.1.66/31 |
| DC1-CL4 | Ethernet1 | 172.16.1.97/31 | DC1-SP1 | Ethernet4 | 172.16.1.96/31 |
| DC1-CL4 | Ethernet2 | 172.16.1.99/31 | DC1-SP2 | Ethernet4 | 172.16.1.98/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.250.1.0/24 | 256 | 8 | 3.13 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_FABRIC | DC1-BL1 | 10.250.1.19/32 |
| DC1_FABRIC | DC1-BL2 | 10.250.1.23/32 |
| DC1_FABRIC | DC1-CL1 | 10.250.1.3/32 |
| DC1_FABRIC | DC1-CL2 | 10.250.1.7/32 |
| DC1_FABRIC | DC1-CL3 | 10.250.1.11/32 |
| DC1_FABRIC | DC1-CL4 | 10.250.1.15/32 |
| DC1_FABRIC | DC1-SP1 | 10.250.1.25/32 |
| DC1_FABRIC | DC1-SP2 | 10.250.1.29/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 10.255.1.0/24 | 256 | 6 | 2.35 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_FABRIC | DC1-BL1 | 10.255.1.19/32 |
| DC1_FABRIC | DC1-BL2 | 10.255.1.19/32 |
| DC1_FABRIC | DC1-CL1 | 10.255.1.3/32 |
| DC1_FABRIC | DC1-CL2 | 10.255.1.3/32 |
| DC1_FABRIC | DC1-CL3 | 10.255.1.11/32 |
| DC1_FABRIC | DC1-CL4 | 10.255.1.11/32 |
