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
  - [ISIS CLNS interfaces](#isis-clns-interfaces)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| DC1_FABRIC | rr | DC1-BL1 | 10.88.169.133/24 | vEOS-lab | Provisioned | - |
| DC1_FABRIC | rr | DC1-BL2 | 10.88.169.134/24 | vEOS-lab | Provisioned | - |
| DC1_FABRIC | pe | DC1-CL1 | 10.88.169.135/24 | vEOS-lab | Provisioned | - |
| DC1_FABRIC | pe | DC1-CL2 | 10.88.169.136/24 | vEOS-lab | Provisioned | - |
| DC1_FABRIC | pe | DC1-CL3 | 10.88.169.137/24 | vEOS-lab | Provisioned | - |
| DC1_FABRIC | pe | DC1-CL4 | 10.88.169.138/24 | vEOS-lab | Provisioned | - |
| DC1_FABRIC | p | DC1-SP1 | 10.88.169.131/24 | vEOS-lab | Provisioned | - |
| DC1_FABRIC | p | DC1-SP2 | 10.88.169.132/24 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| rr | DC1-BL1 | Ethernet1 | p | DC1-SP1 | Ethernet5 |
| rr | DC1-BL1 | Ethernet2 | p | DC1-SP2 | Ethernet5 |
| rr | DC1-BL1 | Ethernet8 | rr | DC1-BL2 | Ethernet8 |
| rr | DC1-BL2 | Ethernet1 | p | DC1-SP1 | Ethernet6 |
| rr | DC1-BL2 | Ethernet2 | p | DC1-SP2 | Ethernet6 |
| pe | DC1-CL1 | Ethernet1 | p | DC1-SP1 | Ethernet1 |
| pe | DC1-CL1 | Ethernet2 | p | DC1-SP2 | Ethernet1 |
| pe | DC1-CL1 | Ethernet8 | pe | DC1-CL2 | Ethernet8 |
| pe | DC1-CL2 | Ethernet1 | p | DC1-SP1 | Ethernet2 |
| pe | DC1-CL2 | Ethernet2 | p | DC1-SP2 | Ethernet2 |
| pe | DC1-CL3 | Ethernet1 | p | DC1-SP1 | Ethernet3 |
| pe | DC1-CL3 | Ethernet2 | p | DC1-SP2 | Ethernet3 |
| pe | DC1-CL3 | Ethernet8 | pe | DC1-CL4 | Ethernet8 |
| pe | DC1-CL4 | Ethernet1 | p | DC1-SP1 | Ethernet4 |
| pe | DC1-CL4 | Ethernet2 | p | DC1-SP2 | Ethernet4 |
| p | DC1-SP1 | Ethernet7 | p | DC1-SP2 | Ethernet7 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC1-BL1 | Ethernet1 | 100.64.1.20/31 | DC1-SP1 | Ethernet5 | 100.64.1.21/31 |
| DC1-BL1 | Ethernet2 | 100.64.1.22/31 | DC1-SP2 | Ethernet5 | 100.64.1.23/31 |
| DC1-BL1 | Ethernet8 | 100.64.1.28/31 | DC1-BL2 | Ethernet8 | 100.64.1.29/31 |
| DC1-BL2 | Ethernet1 | 100.64.1.24/31 | DC1-SP1 | Ethernet6 | 100.64.1.25/31 |
| DC1-BL2 | Ethernet2 | 100.64.1.26/31 | DC1-SP2 | Ethernet6 | 100.64.1.27/31 |
| DC1-CL1 | Ethernet1 | 100.64.1.0/31 | DC1-SP1 | Ethernet1 | 100.64.1.1/31 |
| DC1-CL1 | Ethernet2 | 100.64.1.2/31 | DC1-SP2 | Ethernet1 | 100.64.1.3/31 |
| DC1-CL1 | Ethernet8 | 100.64.1.8/31 | DC1-CL2 | Ethernet8 | 100.64.1.9/31 |
| DC1-CL2 | Ethernet1 | 100.64.1.4/31 | DC1-SP1 | Ethernet2 | 100.64.1.5/31 |
| DC1-CL2 | Ethernet2 | 100.64.1.6/31 | DC1-SP2 | Ethernet2 | 100.64.1.7/31 |
| DC1-CL3 | Ethernet1 | 100.64.1.10/31 | DC1-SP1 | Ethernet3 | 100.64.1.11/31 |
| DC1-CL3 | Ethernet2 | 100.64.1.12/31 | DC1-SP2 | Ethernet3 | 100.64.1.13/31 |
| DC1-CL3 | Ethernet8 | 100.64.1.18/31 | DC1-CL4 | Ethernet8 | 100.64.1.19/31 |
| DC1-CL4 | Ethernet1 | 100.64.1.14/31 | DC1-SP1 | Ethernet4 | 100.64.1.15/31 |
| DC1-CL4 | Ethernet2 | 100.64.1.16/31 | DC1-SP2 | Ethernet4 | 100.64.1.17/31 |
| DC1-SP1 | Ethernet7 | 100.64.1.30/31 | DC1-SP2 | Ethernet7 | 100.64.1.31/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.250.1.0/24 | 256 | 8 | 3.13 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_FABRIC | DC1-BL1 | 10.250.1.7/32 |
| DC1_FABRIC | DC1-BL2 | 10.250.1.8/32 |
| DC1_FABRIC | DC1-CL1 | 10.250.1.3/32 |
| DC1_FABRIC | DC1-CL2 | 10.250.1.4/32 |
| DC1_FABRIC | DC1-CL3 | 10.250.1.5/32 |
| DC1_FABRIC | DC1-CL4 | 10.250.1.6/32 |
| DC1_FABRIC | DC1-SP1 | 10.250.1.1/32 |
| DC1_FABRIC | DC1-SP2 | 10.250.1.2/32 |

### ISIS CLNS interfaces

| POD | Node | CLNS Address |
| --- | ---- | ------------ |
| DC1_FABRIC | DC1-BL1 | 49.0001.1921.6810.0007.00 |
| DC1_FABRIC | DC1-BL2 | 49.0001.1921.6810.0008.00 |
| DC1_FABRIC | DC1-CL1 | 49.0001.1921.6810.0003.00 |
| DC1_FABRIC | DC1-CL2 | 49.0001.1921.6810.0004.00 |
| DC1_FABRIC | DC1-CL3 | 49.0001.1921.6810.0005.00 |
| DC1_FABRIC | DC1-CL4 | 49.0001.1921.6810.0006.00 |
| DC1_FABRIC | DC1-SP1 | 49.0001.1921.6810.0001.00 |
| DC1_FABRIC | DC1-SP2 | 49.0001.1921.6810.0002.00 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
