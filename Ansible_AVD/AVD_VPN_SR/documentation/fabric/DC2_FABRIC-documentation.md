# DC2_FABRIC

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
| DC2_FABRIC | rr | DC2-BL1 | 10.88.169.141/24 | vEOS-lab | Provisioned | - |
| DC2_FABRIC | rr | DC2-BL2 | 10.88.169.142/24 | vEOS-lab | Provisioned | - |
| DC2_FABRIC | pe | DC2-CL1 | 10.88.169.143/24 | vEOS-lab | Provisioned | - |
| DC2_FABRIC | pe | DC2-CL2 | 10.88.169.144/24 | vEOS-lab | Provisioned | - |
| DC2_FABRIC | pe | DC2-CL3 | 10.88.169.145/24 | vEOS-lab | Provisioned | - |
| DC2_FABRIC | pe | DC2-CL4 | 10.88.169.146/24 | vEOS-lab | Provisioned | - |
| DC2_FABRIC | p | DC2-SP1 | 10.88.169.139/24 | vEOS-lab | Provisioned | - |
| DC2_FABRIC | p | DC2-SP2 | 10.88.169.140/24 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| rr | DC2-BL1 | Ethernet1 | p | DC2-SP1 | Ethernet5 |
| rr | DC2-BL1 | Ethernet2 | p | DC2-SP2 | Ethernet5 |
| rr | DC2-BL1 | Ethernet8 | rr | DC2-BL2 | Ethernet8 |
| rr | DC2-BL2 | Ethernet1 | p | DC2-SP1 | Ethernet6 |
| rr | DC2-BL2 | Ethernet2 | p | DC2-SP2 | Ethernet6 |
| pe | DC2-CL1 | Ethernet1 | p | DC2-SP1 | Ethernet1 |
| pe | DC2-CL1 | Ethernet2 | p | DC2-SP2 | Ethernet1 |
| pe | DC2-CL1 | Ethernet8 | pe | DC2-CL2 | Ethernet8 |
| pe | DC2-CL2 | Ethernet1 | p | DC2-SP1 | Ethernet2 |
| pe | DC2-CL2 | Ethernet2 | p | DC2-SP2 | Ethernet2 |
| pe | DC2-CL3 | Ethernet1 | p | DC2-SP1 | Ethernet3 |
| pe | DC2-CL3 | Ethernet2 | p | DC2-SP2 | Ethernet3 |
| pe | DC2-CL3 | Ethernet8 | pe | DC2-CL4 | Ethernet8 |
| pe | DC2-CL4 | Ethernet1 | p | DC2-SP1 | Ethernet4 |
| pe | DC2-CL4 | Ethernet2 | p | DC2-SP2 | Ethernet4 |
| p | DC2-SP1 | Ethernet7 | p | DC2-SP2 | Ethernet7 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC2-BL1 | Ethernet1 | 100.64.2.20/31 | DC2-SP1 | Ethernet5 | 100.64.2.21/31 |
| DC2-BL1 | Ethernet2 | 100.64.2.22/31 | DC2-SP2 | Ethernet5 | 100.64.2.23/31 |
| DC2-BL1 | Ethernet8 | 100.64.2.28/31 | DC2-BL2 | Ethernet8 | 100.64.2.29/31 |
| DC2-BL2 | Ethernet1 | 100.64.2.24/31 | DC2-SP1 | Ethernet6 | 100.64.2.25/31 |
| DC2-BL2 | Ethernet2 | 100.64.2.26/31 | DC2-SP2 | Ethernet6 | 100.64.2.27/31 |
| DC2-CL1 | Ethernet1 | 100.64.2.0/31 | DC2-SP1 | Ethernet1 | 100.64.2.1/31 |
| DC2-CL1 | Ethernet2 | 100.64.2.2/31 | DC2-SP2 | Ethernet1 | 100.64.2.3/31 |
| DC2-CL1 | Ethernet8 | 100.64.2.8/31 | DC2-CL2 | Ethernet8 | 100.64.2.9/31 |
| DC2-CL2 | Ethernet1 | 100.64.2.4/31 | DC2-SP1 | Ethernet2 | 100.64.2.5/31 |
| DC2-CL2 | Ethernet2 | 100.64.2.6/31 | DC2-SP2 | Ethernet2 | 100.64.2.7/31 |
| DC2-CL3 | Ethernet1 | 100.64.2.10/31 | DC2-SP1 | Ethernet3 | 100.64.2.11/31 |
| DC2-CL3 | Ethernet2 | 100.64.2.12/31 | DC2-SP2 | Ethernet3 | 100.64.2.13/31 |
| DC2-CL3 | Ethernet8 | 100.64.2.18/31 | DC2-CL4 | Ethernet8 | 100.64.2.19/31 |
| DC2-CL4 | Ethernet1 | 100.64.2.14/31 | DC2-SP1 | Ethernet4 | 100.64.2.15/31 |
| DC2-CL4 | Ethernet2 | 100.64.2.16/31 | DC2-SP2 | Ethernet4 | 100.64.2.17/31 |
| DC2-SP1 | Ethernet7 | 100.64.2.30/31 | DC2-SP2 | Ethernet7 | 100.64.2.31/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.250.2.0/24 | 256 | 8 | 3.13 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC2_FABRIC | DC2-BL1 | 10.250.2.7/32 |
| DC2_FABRIC | DC2-BL2 | 10.250.2.8/32 |
| DC2_FABRIC | DC2-CL1 | 10.250.2.3/32 |
| DC2_FABRIC | DC2-CL2 | 10.250.2.4/32 |
| DC2_FABRIC | DC2-CL3 | 10.250.2.5/32 |
| DC2_FABRIC | DC2-CL4 | 10.250.2.6/32 |
| DC2_FABRIC | DC2-SP1 | 10.250.2.1/32 |
| DC2_FABRIC | DC2-SP2 | 10.250.2.2/32 |

### ISIS CLNS interfaces

| POD | Node | CLNS Address |
| --- | ---- | ------------ |
| DC2_FABRIC | DC2-BL1 | 49.0001.1921.6820.0007.00 |
| DC2_FABRIC | DC2-BL2 | 49.0001.1921.6820.0008.00 |
| DC2_FABRIC | DC2-CL1 | 49.0001.1921.6820.0003.00 |
| DC2_FABRIC | DC2-CL2 | 49.0001.1921.6820.0004.00 |
| DC2_FABRIC | DC2-CL3 | 49.0001.1921.6820.0005.00 |
| DC2_FABRIC | DC2-CL4 | 49.0001.1921.6820.0006.00 |
| DC2_FABRIC | DC2-SP1 | 49.0001.1921.6820.0001.00 |
| DC2_FABRIC | DC2-SP2 | 49.0001.1921.6820.0002.00 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
