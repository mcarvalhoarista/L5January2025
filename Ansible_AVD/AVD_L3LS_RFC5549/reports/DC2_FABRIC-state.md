# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 280 | 267 | 13 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| DC2-BL1 |  39 | 38 | 1 | NTP |
| DC2-BL2 |  39 | 37 | 2 | NTP, BGP |
| DC2-CL1 |  40 | 38 | 2 | NTP, Interface State |
| DC2-CL2 |  40 | 38 | 2 | NTP, Interface State |
| DC2-CL3 |  40 | 38 | 2 | NTP, Interface State |
| DC2-CL4 |  40 | 38 | 2 | NTP, Interface State |
| DC2-SP1 |  21 | 20 | 1 | NTP |
| DC2-SP2 |  21 | 20 | 1 | NTP |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  8 | 0 | 8 |
| Interface State |  80 | 76 | 4 |
| LLDP Topology |  26 | 26 | 0 |
| BGP |  34 | 33 | 1 |
| Routing Table |  84 | 84 | 0 |
| Loopback0 Reachability |  48 | 48 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | DC2-BL1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 2 | DC2-BL2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 3 | DC2-CL1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 4 | DC2-CL2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 5 | DC2-CL3 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 6 | DC2-CL4 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 7 | DC2-SP1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 8 | DC2-SP2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 44 | DC2-CL1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel4 - DC2-R1_PortChannel100 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 46 | DC2-CL2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel4 - DC2-R1_PortChannel100 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 48 | DC2-CL3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel4 - DC2-R2_PortChannel100 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 50 | DC2-CL4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel4 - DC2-R2_PortChannel100 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 128 | DC2-BL2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.8 | FAIL | Session state: Active |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | DC2-BL1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 2 | DC2-BL2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 3 | DC2-CL1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 4 | DC2-CL2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 5 | DC2-CL3 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 6 | DC2-CL4 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 7 | DC2-SP1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 8 | DC2-SP2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 9 | DC2-BL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC2-SP1_Ethernet5 | PASS | - |
| 10 | DC2-BL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC2-SP2_Ethernet5 | PASS | - |
| 11 | DC2-BL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_DC1-BL1_Ethernet4 | PASS | - |
| 12 | DC2-BL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC2-SP1_Ethernet6 | PASS | - |
| 13 | DC2-BL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC2-SP2_Ethernet6 | PASS | - |
| 14 | DC2-BL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_DC1-BL2_Ethernet4 | PASS | - |
| 15 | DC2-CL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC2-SP1_Ethernet1 | PASS | - |
| 16 | DC2-CL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC2-SP2_Ethernet1 | PASS | - |
| 17 | DC2-CL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - DC2-SW1_Ethernet1 | PASS | - |
| 18 | DC2-CL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - DC2-R1_Ethernet0/1 | PASS | - |
| 19 | DC2-CL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC2-SP1_Ethernet2 | PASS | - |
| 20 | DC2-CL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC2-SP2_Ethernet2 | PASS | - |
| 21 | DC2-CL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - DC2-SW1_Ethernet2 | PASS | - |
| 22 | DC2-CL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - DC2-R1_Ethernet0/2 | PASS | - |
| 23 | DC2-CL3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC2-SP1_Ethernet3 | PASS | - |
| 24 | DC2-CL3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC2-SP2_Ethernet3 | PASS | - |
| 25 | DC2-CL3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - DC2-SW2_Ethernet1 | PASS | - |
| 26 | DC2-CL3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - DC2-R2_Ethernet0/1 | PASS | - |
| 27 | DC2-CL4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC2-SP1_Ethernet4 | PASS | - |
| 28 | DC2-CL4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC2-SP2_Ethernet4 | PASS | - |
| 29 | DC2-CL4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - DC2-SW2_Ethernet2 | PASS | - |
| 30 | DC2-CL4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - DC2-R2_Ethernet0/2 | PASS | - |
| 31 | DC2-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC2-CL1_Ethernet1 | PASS | - |
| 32 | DC2-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC2-CL2_Ethernet1 | PASS | - |
| 33 | DC2-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_DC2-CL3_Ethernet1 | PASS | - |
| 34 | DC2-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_DC2-CL4_Ethernet1 | PASS | - |
| 35 | DC2-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_DC2-BL1_Ethernet1 | PASS | - |
| 36 | DC2-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_DC2-BL2_Ethernet1 | PASS | - |
| 37 | DC2-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC2-CL1_Ethernet2 | PASS | - |
| 38 | DC2-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC2-CL2_Ethernet2 | PASS | - |
| 39 | DC2-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_DC2-CL3_Ethernet2 | PASS | - |
| 40 | DC2-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_DC2-CL4_Ethernet2 | PASS | - |
| 41 | DC2-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_DC2-BL1_Ethernet2 | PASS | - |
| 42 | DC2-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_DC2-BL2_Ethernet2 | PASS | - |
| 43 | DC2-CL1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel3 - DC2-SW1_PortChannel100 | PASS | - |
| 44 | DC2-CL1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel4 - DC2-R1_PortChannel100 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 45 | DC2-CL2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel3 - DC2-SW1_PortChannel100 | PASS | - |
| 46 | DC2-CL2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel4 - DC2-R1_PortChannel100 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 47 | DC2-CL3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel3 - DC2-SW2_PortChannel100 | PASS | - |
| 48 | DC2-CL3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel4 - DC2-R2_PortChannel100 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 49 | DC2-CL4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel3 - DC2-SW2_PortChannel100 | PASS | - |
| 50 | DC2-CL4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel4 - DC2-R2_PortChannel100 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 51 | DC2-BL1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 52 | DC2-BL1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - DMZ | PASS | - |
| 53 | DC2-BL2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 54 | DC2-BL2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - DMZ | PASS | - |
| 55 | DC2-CL1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 56 | DC2-CL1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - DMZ | PASS | - |
| 57 | DC2-CL2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 58 | DC2-CL2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - DMZ | PASS | - |
| 59 | DC2-CL3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 60 | DC2-CL3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - DMZ | PASS | - |
| 61 | DC2-CL4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 62 | DC2-CL4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - DMZ | PASS | - |
| 63 | DC2-BL1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 64 | DC2-BL2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 65 | DC2-CL1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 66 | DC2-CL2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 67 | DC2-CL3 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 68 | DC2-CL4 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 69 | DC2-BL1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 70 | DC2-BL1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 71 | DC2-BL1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback666 - VRF_A_VTEP_DIAGNOSTICS | PASS | - |
| 72 | DC2-BL2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 73 | DC2-BL2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 74 | DC2-BL2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback666 - VRF_A_VTEP_DIAGNOSTICS | PASS | - |
| 75 | DC2-CL1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 76 | DC2-CL1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 77 | DC2-CL1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback666 - VRF_A_VTEP_DIAGNOSTICS | PASS | - |
| 78 | DC2-CL2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 79 | DC2-CL2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 80 | DC2-CL2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback666 - VRF_A_VTEP_DIAGNOSTICS | PASS | - |
| 81 | DC2-CL3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 82 | DC2-CL3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 83 | DC2-CL3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback666 - VRF_A_VTEP_DIAGNOSTICS | PASS | - |
| 84 | DC2-CL4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 85 | DC2-CL4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 86 | DC2-CL4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback666 - VRF_A_VTEP_DIAGNOSTICS | PASS | - |
| 87 | DC2-SP1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 88 | DC2-SP2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 89 | DC2-BL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC2-SP1_Ethernet5 | PASS | - |
| 90 | DC2-BL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC2-SP2_Ethernet5 | PASS | - |
| 91 | DC2-BL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: DC1-BL1_Ethernet4 | PASS | - |
| 92 | DC2-BL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC2-SP1_Ethernet6 | PASS | - |
| 93 | DC2-BL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC2-SP2_Ethernet6 | PASS | - |
| 94 | DC2-BL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: DC1-BL2_Ethernet4 | PASS | - |
| 95 | DC2-CL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC2-SP1_Ethernet1 | PASS | - |
| 96 | DC2-CL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC2-SP2_Ethernet1 | PASS | - |
| 97 | DC2-CL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC2-SP1_Ethernet2 | PASS | - |
| 98 | DC2-CL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC2-SP2_Ethernet2 | PASS | - |
| 99 | DC2-CL3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC2-SP1_Ethernet3 | PASS | - |
| 100 | DC2-CL3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC2-SP2_Ethernet3 | PASS | - |
| 101 | DC2-CL4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC2-SP1_Ethernet4 | PASS | - |
| 102 | DC2-CL4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC2-SP2_Ethernet4 | PASS | - |
| 103 | DC2-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC2-CL1_Ethernet1 | PASS | - |
| 104 | DC2-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC2-CL2_Ethernet1 | PASS | - |
| 105 | DC2-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: DC2-CL3_Ethernet1 | PASS | - |
| 106 | DC2-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: DC2-CL4_Ethernet1 | PASS | - |
| 107 | DC2-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: DC2-BL1_Ethernet1 | PASS | - |
| 108 | DC2-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: DC2-BL2_Ethernet1 | PASS | - |
| 109 | DC2-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC2-CL1_Ethernet2 | PASS | - |
| 110 | DC2-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC2-CL2_Ethernet2 | PASS | - |
| 111 | DC2-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: DC2-CL3_Ethernet2 | PASS | - |
| 112 | DC2-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: DC2-CL4_Ethernet2 | PASS | - |
| 113 | DC2-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: DC2-BL1_Ethernet2 | PASS | - |
| 114 | DC2-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: DC2-BL2_Ethernet2 | PASS | - |
| 115 | DC2-BL1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 116 | DC2-BL2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 117 | DC2-CL1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 118 | DC2-CL2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 119 | DC2-CL3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 120 | DC2-CL4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 121 | DC2-SP1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 122 | DC2-SP2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 123 | DC2-BL1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.1 | PASS | - |
| 124 | DC2-BL1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.2 | PASS | - |
| 125 | DC2-BL1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.7 | PASS | - |
| 126 | DC2-BL2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.1 | PASS | - |
| 127 | DC2-BL2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.2 | PASS | - |
| 128 | DC2-BL2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.8 | FAIL | Session state: Active |
| 129 | DC2-CL1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.1 | PASS | - |
| 130 | DC2-CL1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.2 | PASS | - |
| 131 | DC2-CL2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.1 | PASS | - |
| 132 | DC2-CL2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.2 | PASS | - |
| 133 | DC2-CL3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.1 | PASS | - |
| 134 | DC2-CL3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.2 | PASS | - |
| 135 | DC2-CL4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.1 | PASS | - |
| 136 | DC2-CL4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.2 | PASS | - |
| 137 | DC2-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.7 | PASS | - |
| 138 | DC2-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.8 | PASS | - |
| 139 | DC2-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.3 | PASS | - |
| 140 | DC2-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.4 | PASS | - |
| 141 | DC2-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.5 | PASS | - |
| 142 | DC2-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.6 | PASS | - |
| 143 | DC2-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.7 | PASS | - |
| 144 | DC2-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.8 | PASS | - |
| 145 | DC2-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.3 | PASS | - |
| 146 | DC2-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.4 | PASS | - |
| 147 | DC2-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.5 | PASS | - |
| 148 | DC2-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.6 | PASS | - |
| 149 | DC2-BL1 | Routing Table | Remote VTEP address | 10.255.2.7 | PASS | - |
| 150 | DC2-BL1 | Routing Table | Remote VTEP address | 10.255.2.8 | PASS | - |
| 151 | DC2-BL1 | Routing Table | Remote VTEP address | 10.255.2.3 | PASS | - |
| 152 | DC2-BL1 | Routing Table | Remote VTEP address | 10.255.2.4 | PASS | - |
| 153 | DC2-BL1 | Routing Table | Remote VTEP address | 10.255.2.5 | PASS | - |
| 154 | DC2-BL1 | Routing Table | Remote VTEP address | 10.255.2.6 | PASS | - |
| 155 | DC2-BL2 | Routing Table | Remote VTEP address | 10.255.2.7 | PASS | - |
| 156 | DC2-BL2 | Routing Table | Remote VTEP address | 10.255.2.8 | PASS | - |
| 157 | DC2-BL2 | Routing Table | Remote VTEP address | 10.255.2.3 | PASS | - |
| 158 | DC2-BL2 | Routing Table | Remote VTEP address | 10.255.2.4 | PASS | - |
| 159 | DC2-BL2 | Routing Table | Remote VTEP address | 10.255.2.5 | PASS | - |
| 160 | DC2-BL2 | Routing Table | Remote VTEP address | 10.255.2.6 | PASS | - |
| 161 | DC2-CL1 | Routing Table | Remote VTEP address | 10.255.2.7 | PASS | - |
| 162 | DC2-CL1 | Routing Table | Remote VTEP address | 10.255.2.8 | PASS | - |
| 163 | DC2-CL1 | Routing Table | Remote VTEP address | 10.255.2.3 | PASS | - |
| 164 | DC2-CL1 | Routing Table | Remote VTEP address | 10.255.2.4 | PASS | - |
| 165 | DC2-CL1 | Routing Table | Remote VTEP address | 10.255.2.5 | PASS | - |
| 166 | DC2-CL1 | Routing Table | Remote VTEP address | 10.255.2.6 | PASS | - |
| 167 | DC2-CL2 | Routing Table | Remote VTEP address | 10.255.2.7 | PASS | - |
| 168 | DC2-CL2 | Routing Table | Remote VTEP address | 10.255.2.8 | PASS | - |
| 169 | DC2-CL2 | Routing Table | Remote VTEP address | 10.255.2.3 | PASS | - |
| 170 | DC2-CL2 | Routing Table | Remote VTEP address | 10.255.2.4 | PASS | - |
| 171 | DC2-CL2 | Routing Table | Remote VTEP address | 10.255.2.5 | PASS | - |
| 172 | DC2-CL2 | Routing Table | Remote VTEP address | 10.255.2.6 | PASS | - |
| 173 | DC2-CL3 | Routing Table | Remote VTEP address | 10.255.2.7 | PASS | - |
| 174 | DC2-CL3 | Routing Table | Remote VTEP address | 10.255.2.8 | PASS | - |
| 175 | DC2-CL3 | Routing Table | Remote VTEP address | 10.255.2.3 | PASS | - |
| 176 | DC2-CL3 | Routing Table | Remote VTEP address | 10.255.2.4 | PASS | - |
| 177 | DC2-CL3 | Routing Table | Remote VTEP address | 10.255.2.5 | PASS | - |
| 178 | DC2-CL3 | Routing Table | Remote VTEP address | 10.255.2.6 | PASS | - |
| 179 | DC2-CL4 | Routing Table | Remote VTEP address | 10.255.2.7 | PASS | - |
| 180 | DC2-CL4 | Routing Table | Remote VTEP address | 10.255.2.8 | PASS | - |
| 181 | DC2-CL4 | Routing Table | Remote VTEP address | 10.255.2.3 | PASS | - |
| 182 | DC2-CL4 | Routing Table | Remote VTEP address | 10.255.2.4 | PASS | - |
| 183 | DC2-CL4 | Routing Table | Remote VTEP address | 10.255.2.5 | PASS | - |
| 184 | DC2-CL4 | Routing Table | Remote VTEP address | 10.255.2.6 | PASS | - |
| 185 | DC2-BL1 | Routing Table | Remote Lo0 address | 10.250.2.7 | PASS | - |
| 186 | DC2-BL1 | Routing Table | Remote Lo0 address | 10.250.2.8 | PASS | - |
| 187 | DC2-BL1 | Routing Table | Remote Lo0 address | 10.250.2.3 | PASS | - |
| 188 | DC2-BL1 | Routing Table | Remote Lo0 address | 10.250.2.4 | PASS | - |
| 189 | DC2-BL1 | Routing Table | Remote Lo0 address | 10.250.2.5 | PASS | - |
| 190 | DC2-BL1 | Routing Table | Remote Lo0 address | 10.250.2.6 | PASS | - |
| 191 | DC2-BL1 | Routing Table | Remote Lo0 address | 10.250.2.1 | PASS | - |
| 192 | DC2-BL1 | Routing Table | Remote Lo0 address | 10.250.2.2 | PASS | - |
| 193 | DC2-BL2 | Routing Table | Remote Lo0 address | 10.250.2.7 | PASS | - |
| 194 | DC2-BL2 | Routing Table | Remote Lo0 address | 10.250.2.8 | PASS | - |
| 195 | DC2-BL2 | Routing Table | Remote Lo0 address | 10.250.2.3 | PASS | - |
| 196 | DC2-BL2 | Routing Table | Remote Lo0 address | 10.250.2.4 | PASS | - |
| 197 | DC2-BL2 | Routing Table | Remote Lo0 address | 10.250.2.5 | PASS | - |
| 198 | DC2-BL2 | Routing Table | Remote Lo0 address | 10.250.2.6 | PASS | - |
| 199 | DC2-BL2 | Routing Table | Remote Lo0 address | 10.250.2.1 | PASS | - |
| 200 | DC2-BL2 | Routing Table | Remote Lo0 address | 10.250.2.2 | PASS | - |
| 201 | DC2-CL1 | Routing Table | Remote Lo0 address | 10.250.2.7 | PASS | - |
| 202 | DC2-CL1 | Routing Table | Remote Lo0 address | 10.250.2.8 | PASS | - |
| 203 | DC2-CL1 | Routing Table | Remote Lo0 address | 10.250.2.3 | PASS | - |
| 204 | DC2-CL1 | Routing Table | Remote Lo0 address | 10.250.2.4 | PASS | - |
| 205 | DC2-CL1 | Routing Table | Remote Lo0 address | 10.250.2.5 | PASS | - |
| 206 | DC2-CL1 | Routing Table | Remote Lo0 address | 10.250.2.6 | PASS | - |
| 207 | DC2-CL1 | Routing Table | Remote Lo0 address | 10.250.2.1 | PASS | - |
| 208 | DC2-CL1 | Routing Table | Remote Lo0 address | 10.250.2.2 | PASS | - |
| 209 | DC2-CL2 | Routing Table | Remote Lo0 address | 10.250.2.7 | PASS | - |
| 210 | DC2-CL2 | Routing Table | Remote Lo0 address | 10.250.2.8 | PASS | - |
| 211 | DC2-CL2 | Routing Table | Remote Lo0 address | 10.250.2.3 | PASS | - |
| 212 | DC2-CL2 | Routing Table | Remote Lo0 address | 10.250.2.4 | PASS | - |
| 213 | DC2-CL2 | Routing Table | Remote Lo0 address | 10.250.2.5 | PASS | - |
| 214 | DC2-CL2 | Routing Table | Remote Lo0 address | 10.250.2.6 | PASS | - |
| 215 | DC2-CL2 | Routing Table | Remote Lo0 address | 10.250.2.1 | PASS | - |
| 216 | DC2-CL2 | Routing Table | Remote Lo0 address | 10.250.2.2 | PASS | - |
| 217 | DC2-CL3 | Routing Table | Remote Lo0 address | 10.250.2.7 | PASS | - |
| 218 | DC2-CL3 | Routing Table | Remote Lo0 address | 10.250.2.8 | PASS | - |
| 219 | DC2-CL3 | Routing Table | Remote Lo0 address | 10.250.2.3 | PASS | - |
| 220 | DC2-CL3 | Routing Table | Remote Lo0 address | 10.250.2.4 | PASS | - |
| 221 | DC2-CL3 | Routing Table | Remote Lo0 address | 10.250.2.5 | PASS | - |
| 222 | DC2-CL3 | Routing Table | Remote Lo0 address | 10.250.2.6 | PASS | - |
| 223 | DC2-CL3 | Routing Table | Remote Lo0 address | 10.250.2.1 | PASS | - |
| 224 | DC2-CL3 | Routing Table | Remote Lo0 address | 10.250.2.2 | PASS | - |
| 225 | DC2-CL4 | Routing Table | Remote Lo0 address | 10.250.2.7 | PASS | - |
| 226 | DC2-CL4 | Routing Table | Remote Lo0 address | 10.250.2.8 | PASS | - |
| 227 | DC2-CL4 | Routing Table | Remote Lo0 address | 10.250.2.3 | PASS | - |
| 228 | DC2-CL4 | Routing Table | Remote Lo0 address | 10.250.2.4 | PASS | - |
| 229 | DC2-CL4 | Routing Table | Remote Lo0 address | 10.250.2.5 | PASS | - |
| 230 | DC2-CL4 | Routing Table | Remote Lo0 address | 10.250.2.6 | PASS | - |
| 231 | DC2-CL4 | Routing Table | Remote Lo0 address | 10.250.2.1 | PASS | - |
| 232 | DC2-CL4 | Routing Table | Remote Lo0 address | 10.250.2.2 | PASS | - |
| 233 | DC2-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL1 - 10.250.2.7 Destination: 10.250.2.7 | PASS | - |
| 234 | DC2-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL1 - 10.250.2.7 Destination: 10.250.2.8 | PASS | - |
| 235 | DC2-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL1 - 10.250.2.7 Destination: 10.250.2.3 | PASS | - |
| 236 | DC2-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL1 - 10.250.2.7 Destination: 10.250.2.4 | PASS | - |
| 237 | DC2-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL1 - 10.250.2.7 Destination: 10.250.2.5 | PASS | - |
| 238 | DC2-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL1 - 10.250.2.7 Destination: 10.250.2.6 | PASS | - |
| 239 | DC2-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL1 - 10.250.2.7 Destination: 10.250.2.1 | PASS | - |
| 240 | DC2-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL1 - 10.250.2.7 Destination: 10.250.2.2 | PASS | - |
| 241 | DC2-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL2 - 10.250.2.8 Destination: 10.250.2.7 | PASS | - |
| 242 | DC2-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL2 - 10.250.2.8 Destination: 10.250.2.8 | PASS | - |
| 243 | DC2-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL2 - 10.250.2.8 Destination: 10.250.2.3 | PASS | - |
| 244 | DC2-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL2 - 10.250.2.8 Destination: 10.250.2.4 | PASS | - |
| 245 | DC2-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL2 - 10.250.2.8 Destination: 10.250.2.5 | PASS | - |
| 246 | DC2-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL2 - 10.250.2.8 Destination: 10.250.2.6 | PASS | - |
| 247 | DC2-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL2 - 10.250.2.8 Destination: 10.250.2.1 | PASS | - |
| 248 | DC2-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-BL2 - 10.250.2.8 Destination: 10.250.2.2 | PASS | - |
| 249 | DC2-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL1 - 10.250.2.3 Destination: 10.250.2.7 | PASS | - |
| 250 | DC2-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL1 - 10.250.2.3 Destination: 10.250.2.8 | PASS | - |
| 251 | DC2-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL1 - 10.250.2.3 Destination: 10.250.2.3 | PASS | - |
| 252 | DC2-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL1 - 10.250.2.3 Destination: 10.250.2.4 | PASS | - |
| 253 | DC2-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL1 - 10.250.2.3 Destination: 10.250.2.5 | PASS | - |
| 254 | DC2-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL1 - 10.250.2.3 Destination: 10.250.2.6 | PASS | - |
| 255 | DC2-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL1 - 10.250.2.3 Destination: 10.250.2.1 | PASS | - |
| 256 | DC2-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL1 - 10.250.2.3 Destination: 10.250.2.2 | PASS | - |
| 257 | DC2-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL2 - 10.250.2.4 Destination: 10.250.2.7 | PASS | - |
| 258 | DC2-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL2 - 10.250.2.4 Destination: 10.250.2.8 | PASS | - |
| 259 | DC2-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL2 - 10.250.2.4 Destination: 10.250.2.3 | PASS | - |
| 260 | DC2-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL2 - 10.250.2.4 Destination: 10.250.2.4 | PASS | - |
| 261 | DC2-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL2 - 10.250.2.4 Destination: 10.250.2.5 | PASS | - |
| 262 | DC2-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL2 - 10.250.2.4 Destination: 10.250.2.6 | PASS | - |
| 263 | DC2-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL2 - 10.250.2.4 Destination: 10.250.2.1 | PASS | - |
| 264 | DC2-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL2 - 10.250.2.4 Destination: 10.250.2.2 | PASS | - |
| 265 | DC2-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL3 - 10.250.2.5 Destination: 10.250.2.7 | PASS | - |
| 266 | DC2-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL3 - 10.250.2.5 Destination: 10.250.2.8 | PASS | - |
| 267 | DC2-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL3 - 10.250.2.5 Destination: 10.250.2.3 | PASS | - |
| 268 | DC2-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL3 - 10.250.2.5 Destination: 10.250.2.4 | PASS | - |
| 269 | DC2-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL3 - 10.250.2.5 Destination: 10.250.2.5 | PASS | - |
| 270 | DC2-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL3 - 10.250.2.5 Destination: 10.250.2.6 | PASS | - |
| 271 | DC2-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL3 - 10.250.2.5 Destination: 10.250.2.1 | PASS | - |
| 272 | DC2-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL3 - 10.250.2.5 Destination: 10.250.2.2 | PASS | - |
| 273 | DC2-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL4 - 10.250.2.6 Destination: 10.250.2.7 | PASS | - |
| 274 | DC2-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL4 - 10.250.2.6 Destination: 10.250.2.8 | PASS | - |
| 275 | DC2-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL4 - 10.250.2.6 Destination: 10.250.2.3 | PASS | - |
| 276 | DC2-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL4 - 10.250.2.6 Destination: 10.250.2.4 | PASS | - |
| 277 | DC2-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL4 - 10.250.2.6 Destination: 10.250.2.5 | PASS | - |
| 278 | DC2-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL4 - 10.250.2.6 Destination: 10.250.2.6 | PASS | - |
| 279 | DC2-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL4 - 10.250.2.6 Destination: 10.250.2.1 | PASS | - |
| 280 | DC2-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC2-CL4 - 10.250.2.6 Destination: 10.250.2.2 | PASS | - |
