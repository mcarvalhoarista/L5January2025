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
| 320 | 306 | 14 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| DC1-BL1 |  45 | 43 | 2 | NTP, Interface State |
| DC1-BL2 |  45 | 43 | 2 | NTP, Interface State |
| DC1-CL1 |  41 | 39 | 2 | NTP, Interface State |
| DC1-CL2 |  41 | 39 | 2 | NTP, Interface State |
| DC1-CL3 |  41 | 39 | 2 | NTP, Interface State |
| DC1-CL4 |  41 | 39 | 2 | NTP, Interface State |
| DC1-SP1 |  33 | 32 | 1 | NTP |
| DC1-SP2 |  33 | 32 | 1 | NTP |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  8 | 0 | 8 |
| Interface State |  70 | 64 | 6 |
| LLDP Topology |  32 | 32 | 0 |
| MLAG |  6 | 6 | 0 |
| IP Reachability |  24 | 24 | 0 |
| BGP |  66 | 66 | 0 |
| Routing Table |  66 | 66 | 0 |
| Loopback0 Reachability |  48 | 48 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | DC1-BL1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 2 | DC1-BL2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 3 | DC1-CL1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 4 | DC1-CL2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 5 | DC1-CL3 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 6 | DC1-CL4 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 7 | DC1-SP1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 8 | DC1-SP2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 59 | DC1-BL1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 60 | DC1-BL2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 61 | DC1-CL1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 62 | DC1-CL2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 63 | DC1-CL3 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 64 | DC1-CL4 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | DC1-BL1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 2 | DC1-BL2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 3 | DC1-CL1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 4 | DC1-CL2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 5 | DC1-CL3 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 6 | DC1-CL4 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 7 | DC1-SP1 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 8 | DC1-SP2 | NTP | Synchronised with NTP server | NTP | FAIL | Not synchronised to NTP server |
| 9 | DC1-BL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - MLAG_PEER_DC1-BL2_Ethernet8 | PASS | - |
| 10 | DC1-BL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC1-SP1_Ethernet5 | PASS | - |
| 11 | DC1-BL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC1-SP2_Ethernet5 | PASS | - |
| 12 | DC1-BL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_DC2-BL1_Ethernet4 | PASS | - |
| 13 | DC1-BL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - MLAG_PEER_DC1-BL1_Ethernet8 | PASS | - |
| 14 | DC1-BL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC1-SP1_Ethernet6 | PASS | - |
| 15 | DC1-BL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC1-SP2_Ethernet6 | PASS | - |
| 16 | DC1-BL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_DC2-BL2_Ethernet4 | PASS | - |
| 17 | DC1-CL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - MLAG_PEER_DC1-CL2_Ethernet8 | PASS | - |
| 18 | DC1-CL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC1-SP1_Ethernet1 | PASS | - |
| 19 | DC1-CL1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC1-SP2_Ethernet1 | PASS | - |
| 20 | DC1-CL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - MLAG_PEER_DC1-CL1_Ethernet8 | PASS | - |
| 21 | DC1-CL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC1-SP1_Ethernet2 | PASS | - |
| 22 | DC1-CL2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC1-SP2_Ethernet2 | PASS | - |
| 23 | DC1-CL3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - MLAG_PEER_DC1-CL4_Ethernet8 | PASS | - |
| 24 | DC1-CL3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC1-SP1_Ethernet3 | PASS | - |
| 25 | DC1-CL3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC1-SP2_Ethernet3 | PASS | - |
| 26 | DC1-CL4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet8 - MLAG_PEER_DC1-CL3_Ethernet8 | PASS | - |
| 27 | DC1-CL4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC1-SP1_Ethernet4 | PASS | - |
| 28 | DC1-CL4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC1-SP2_Ethernet4 | PASS | - |
| 29 | DC1-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC1-CL1_Ethernet1 | PASS | - |
| 30 | DC1-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC1-CL2_Ethernet1 | PASS | - |
| 31 | DC1-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_DC1-CL3_Ethernet1 | PASS | - |
| 32 | DC1-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_DC1-CL4_Ethernet1 | PASS | - |
| 33 | DC1-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_DC1-BL1_Ethernet1 | PASS | - |
| 34 | DC1-SP1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_DC1-BL2_Ethernet1 | PASS | - |
| 35 | DC1-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_DC1-CL1_Ethernet2 | PASS | - |
| 36 | DC1-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_DC1-CL2_Ethernet2 | PASS | - |
| 37 | DC1-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_DC1-CL3_Ethernet2 | PASS | - |
| 38 | DC1-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_DC1-CL4_Ethernet2 | PASS | - |
| 39 | DC1-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_DC1-BL1_Ethernet2 | PASS | - |
| 40 | DC1-SP2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_DC1-BL2_Ethernet2 | PASS | - |
| 41 | DC1-BL1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel8 - MLAG_PEER_DC1-BL2_Po8 | PASS | - |
| 42 | DC1-BL2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel8 - MLAG_PEER_DC1-BL1_Po8 | PASS | - |
| 43 | DC1-CL1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel8 - MLAG_PEER_DC1-CL2_Po8 | PASS | - |
| 44 | DC1-CL2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel8 - MLAG_PEER_DC1-CL1_Po8 | PASS | - |
| 45 | DC1-CL3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel8 - MLAG_PEER_DC1-CL4_Po8 | PASS | - |
| 46 | DC1-CL4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel8 - MLAG_PEER_DC1-CL3_Po8 | PASS | - |
| 47 | DC1-BL1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 48 | DC1-BL1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 49 | DC1-BL2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 50 | DC1-BL2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 51 | DC1-CL1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 52 | DC1-CL1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 53 | DC1-CL2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 54 | DC1-CL2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 55 | DC1-CL3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 56 | DC1-CL3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 57 | DC1-CL4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 58 | DC1-CL4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 59 | DC1-BL1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 60 | DC1-BL2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 61 | DC1-CL1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 62 | DC1-CL2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 63 | DC1-CL3 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 64 | DC1-CL4 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | FAIL | Interface status: down - line protocol status: down |
| 65 | DC1-BL1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 66 | DC1-BL1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 67 | DC1-BL2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 68 | DC1-BL2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 69 | DC1-CL1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 70 | DC1-CL1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 71 | DC1-CL2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 72 | DC1-CL2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 73 | DC1-CL3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 74 | DC1-CL3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 75 | DC1-CL4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 76 | DC1-CL4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 77 | DC1-SP1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 78 | DC1-SP2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 79 | DC1-BL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: DC1-BL2_Ethernet8 | PASS | - |
| 80 | DC1-BL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC1-SP1_Ethernet5 | PASS | - |
| 81 | DC1-BL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC1-SP2_Ethernet5 | PASS | - |
| 82 | DC1-BL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: DC2-BL1_Ethernet4 | PASS | - |
| 83 | DC1-BL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: DC1-BL1_Ethernet8 | PASS | - |
| 84 | DC1-BL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC1-SP1_Ethernet6 | PASS | - |
| 85 | DC1-BL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC1-SP2_Ethernet6 | PASS | - |
| 86 | DC1-BL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: DC2-BL2_Ethernet4 | PASS | - |
| 87 | DC1-CL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: DC1-CL2_Ethernet8 | PASS | - |
| 88 | DC1-CL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC1-SP1_Ethernet1 | PASS | - |
| 89 | DC1-CL1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC1-SP2_Ethernet1 | PASS | - |
| 90 | DC1-CL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: DC1-CL1_Ethernet8 | PASS | - |
| 91 | DC1-CL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC1-SP1_Ethernet2 | PASS | - |
| 92 | DC1-CL2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC1-SP2_Ethernet2 | PASS | - |
| 93 | DC1-CL3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: DC1-CL4_Ethernet8 | PASS | - |
| 94 | DC1-CL3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC1-SP1_Ethernet3 | PASS | - |
| 95 | DC1-CL3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC1-SP2_Ethernet3 | PASS | - |
| 96 | DC1-CL4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet8 - remote: DC1-CL3_Ethernet8 | PASS | - |
| 97 | DC1-CL4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC1-SP1_Ethernet4 | PASS | - |
| 98 | DC1-CL4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC1-SP2_Ethernet4 | PASS | - |
| 99 | DC1-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC1-CL1_Ethernet1 | PASS | - |
| 100 | DC1-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC1-CL2_Ethernet1 | PASS | - |
| 101 | DC1-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: DC1-CL3_Ethernet1 | PASS | - |
| 102 | DC1-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: DC1-CL4_Ethernet1 | PASS | - |
| 103 | DC1-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: DC1-BL1_Ethernet1 | PASS | - |
| 104 | DC1-SP1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: DC1-BL2_Ethernet1 | PASS | - |
| 105 | DC1-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: DC1-CL1_Ethernet2 | PASS | - |
| 106 | DC1-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: DC1-CL2_Ethernet2 | PASS | - |
| 107 | DC1-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: DC1-CL3_Ethernet2 | PASS | - |
| 108 | DC1-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: DC1-CL4_Ethernet2 | PASS | - |
| 109 | DC1-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: DC1-BL1_Ethernet2 | PASS | - |
| 110 | DC1-SP2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: DC1-BL2_Ethernet2 | PASS | - |
| 111 | DC1-BL1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 112 | DC1-BL2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 113 | DC1-CL1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 114 | DC1-CL2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 115 | DC1-CL3 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 116 | DC1-CL4 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 117 | DC1-BL1 | IP Reachability | ip reachability test p2p links | Source: DC1-BL1_Ethernet1 - Destination: DC1-SP1_Ethernet5 | PASS | - |
| 118 | DC1-BL1 | IP Reachability | ip reachability test p2p links | Source: DC1-BL1_Ethernet2 - Destination: DC1-SP2_Ethernet5 | PASS | - |
| 119 | DC1-BL2 | IP Reachability | ip reachability test p2p links | Source: DC1-BL2_Ethernet1 - Destination: DC1-SP1_Ethernet6 | PASS | - |
| 120 | DC1-BL2 | IP Reachability | ip reachability test p2p links | Source: DC1-BL2_Ethernet2 - Destination: DC1-SP2_Ethernet6 | PASS | - |
| 121 | DC1-CL1 | IP Reachability | ip reachability test p2p links | Source: DC1-CL1_Ethernet1 - Destination: DC1-SP1_Ethernet1 | PASS | - |
| 122 | DC1-CL1 | IP Reachability | ip reachability test p2p links | Source: DC1-CL1_Ethernet2 - Destination: DC1-SP2_Ethernet1 | PASS | - |
| 123 | DC1-CL2 | IP Reachability | ip reachability test p2p links | Source: DC1-CL2_Ethernet1 - Destination: DC1-SP1_Ethernet2 | PASS | - |
| 124 | DC1-CL2 | IP Reachability | ip reachability test p2p links | Source: DC1-CL2_Ethernet2 - Destination: DC1-SP2_Ethernet2 | PASS | - |
| 125 | DC1-CL3 | IP Reachability | ip reachability test p2p links | Source: DC1-CL3_Ethernet1 - Destination: DC1-SP1_Ethernet3 | PASS | - |
| 126 | DC1-CL3 | IP Reachability | ip reachability test p2p links | Source: DC1-CL3_Ethernet2 - Destination: DC1-SP2_Ethernet3 | PASS | - |
| 127 | DC1-CL4 | IP Reachability | ip reachability test p2p links | Source: DC1-CL4_Ethernet1 - Destination: DC1-SP1_Ethernet4 | PASS | - |
| 128 | DC1-CL4 | IP Reachability | ip reachability test p2p links | Source: DC1-CL4_Ethernet2 - Destination: DC1-SP2_Ethernet4 | PASS | - |
| 129 | DC1-SP1 | IP Reachability | ip reachability test p2p links | Source: DC1-SP1_Ethernet1 - Destination: DC1-CL1_Ethernet1 | PASS | - |
| 130 | DC1-SP1 | IP Reachability | ip reachability test p2p links | Source: DC1-SP1_Ethernet2 - Destination: DC1-CL2_Ethernet1 | PASS | - |
| 131 | DC1-SP1 | IP Reachability | ip reachability test p2p links | Source: DC1-SP1_Ethernet3 - Destination: DC1-CL3_Ethernet1 | PASS | - |
| 132 | DC1-SP1 | IP Reachability | ip reachability test p2p links | Source: DC1-SP1_Ethernet4 - Destination: DC1-CL4_Ethernet1 | PASS | - |
| 133 | DC1-SP1 | IP Reachability | ip reachability test p2p links | Source: DC1-SP1_Ethernet5 - Destination: DC1-BL1_Ethernet1 | PASS | - |
| 134 | DC1-SP1 | IP Reachability | ip reachability test p2p links | Source: DC1-SP1_Ethernet6 - Destination: DC1-BL2_Ethernet1 | PASS | - |
| 135 | DC1-SP2 | IP Reachability | ip reachability test p2p links | Source: DC1-SP2_Ethernet1 - Destination: DC1-CL1_Ethernet2 | PASS | - |
| 136 | DC1-SP2 | IP Reachability | ip reachability test p2p links | Source: DC1-SP2_Ethernet2 - Destination: DC1-CL2_Ethernet2 | PASS | - |
| 137 | DC1-SP2 | IP Reachability | ip reachability test p2p links | Source: DC1-SP2_Ethernet3 - Destination: DC1-CL3_Ethernet2 | PASS | - |
| 138 | DC1-SP2 | IP Reachability | ip reachability test p2p links | Source: DC1-SP2_Ethernet4 - Destination: DC1-CL4_Ethernet2 | PASS | - |
| 139 | DC1-SP2 | IP Reachability | ip reachability test p2p links | Source: DC1-SP2_Ethernet5 - Destination: DC1-BL1_Ethernet2 | PASS | - |
| 140 | DC1-SP2 | IP Reachability | ip reachability test p2p links | Source: DC1-SP2_Ethernet6 - Destination: DC1-BL2_Ethernet2 | PASS | - |
| 141 | DC1-BL1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 142 | DC1-BL2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 143 | DC1-CL1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 144 | DC1-CL2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 145 | DC1-CL3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 146 | DC1-CL4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 147 | DC1-SP1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 148 | DC1-SP2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 149 | DC1-BL1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.252.1.9 | PASS | - |
| 150 | DC1-BL1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.16 | PASS | - |
| 151 | DC1-BL1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.18 | PASS | - |
| 152 | DC1-BL1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.255.1 | PASS | - |
| 153 | DC1-BL2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.252.1.8 | PASS | - |
| 154 | DC1-BL2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.20 | PASS | - |
| 155 | DC1-BL2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.22 | PASS | - |
| 156 | DC1-BL2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.255.3 | PASS | - |
| 157 | DC1-CL1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.252.1.1 | PASS | - |
| 158 | DC1-CL1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.0 | PASS | - |
| 159 | DC1-CL1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.2 | PASS | - |
| 160 | DC1-CL2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.252.1.0 | PASS | - |
| 161 | DC1-CL2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.4 | PASS | - |
| 162 | DC1-CL2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.6 | PASS | - |
| 163 | DC1-CL3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.252.1.5 | PASS | - |
| 164 | DC1-CL3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.8 | PASS | - |
| 165 | DC1-CL3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.10 | PASS | - |
| 166 | DC1-CL4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.252.1.4 | PASS | - |
| 167 | DC1-CL4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.12 | PASS | - |
| 168 | DC1-CL4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.14 | PASS | - |
| 169 | DC1-SP1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.1 | PASS | - |
| 170 | DC1-SP1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.5 | PASS | - |
| 171 | DC1-SP1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.9 | PASS | - |
| 172 | DC1-SP1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.13 | PASS | - |
| 173 | DC1-SP1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.17 | PASS | - |
| 174 | DC1-SP1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.21 | PASS | - |
| 175 | DC1-SP2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.3 | PASS | - |
| 176 | DC1-SP2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.7 | PASS | - |
| 177 | DC1-SP2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.11 | PASS | - |
| 178 | DC1-SP2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.15 | PASS | - |
| 179 | DC1-SP2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.19 | PASS | - |
| 180 | DC1-SP2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.16.1.23 | PASS | - |
| 181 | DC1-BL1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.1 | PASS | - |
| 182 | DC1-BL1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.2 | PASS | - |
| 183 | DC1-BL1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.7 | PASS | - |
| 184 | DC1-BL2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.1 | PASS | - |
| 185 | DC1-BL2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.2 | PASS | - |
| 186 | DC1-BL2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.2.8 | PASS | - |
| 187 | DC1-CL1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.1 | PASS | - |
| 188 | DC1-CL1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.2 | PASS | - |
| 189 | DC1-CL2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.1 | PASS | - |
| 190 | DC1-CL2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.2 | PASS | - |
| 191 | DC1-CL3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.1 | PASS | - |
| 192 | DC1-CL3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.2 | PASS | - |
| 193 | DC1-CL4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.1 | PASS | - |
| 194 | DC1-CL4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.2 | PASS | - |
| 195 | DC1-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.7 | PASS | - |
| 196 | DC1-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.8 | PASS | - |
| 197 | DC1-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.3 | PASS | - |
| 198 | DC1-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.4 | PASS | - |
| 199 | DC1-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.5 | PASS | - |
| 200 | DC1-SP1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.6 | PASS | - |
| 201 | DC1-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.7 | PASS | - |
| 202 | DC1-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.8 | PASS | - |
| 203 | DC1-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.3 | PASS | - |
| 204 | DC1-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.4 | PASS | - |
| 205 | DC1-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.5 | PASS | - |
| 206 | DC1-SP2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 10.250.1.6 | PASS | - |
| 207 | DC1-BL1 | Routing Table | Remote VTEP address | 10.255.1.7 | PASS | - |
| 208 | DC1-BL1 | Routing Table | Remote VTEP address | 10.255.1.3 | PASS | - |
| 209 | DC1-BL1 | Routing Table | Remote VTEP address | 10.255.1.5 | PASS | - |
| 210 | DC1-BL2 | Routing Table | Remote VTEP address | 10.255.1.7 | PASS | - |
| 211 | DC1-BL2 | Routing Table | Remote VTEP address | 10.255.1.3 | PASS | - |
| 212 | DC1-BL2 | Routing Table | Remote VTEP address | 10.255.1.5 | PASS | - |
| 213 | DC1-CL1 | Routing Table | Remote VTEP address | 10.255.1.7 | PASS | - |
| 214 | DC1-CL1 | Routing Table | Remote VTEP address | 10.255.1.3 | PASS | - |
| 215 | DC1-CL1 | Routing Table | Remote VTEP address | 10.255.1.5 | PASS | - |
| 216 | DC1-CL2 | Routing Table | Remote VTEP address | 10.255.1.7 | PASS | - |
| 217 | DC1-CL2 | Routing Table | Remote VTEP address | 10.255.1.3 | PASS | - |
| 218 | DC1-CL2 | Routing Table | Remote VTEP address | 10.255.1.5 | PASS | - |
| 219 | DC1-CL3 | Routing Table | Remote VTEP address | 10.255.1.7 | PASS | - |
| 220 | DC1-CL3 | Routing Table | Remote VTEP address | 10.255.1.3 | PASS | - |
| 221 | DC1-CL3 | Routing Table | Remote VTEP address | 10.255.1.5 | PASS | - |
| 222 | DC1-CL4 | Routing Table | Remote VTEP address | 10.255.1.7 | PASS | - |
| 223 | DC1-CL4 | Routing Table | Remote VTEP address | 10.255.1.3 | PASS | - |
| 224 | DC1-CL4 | Routing Table | Remote VTEP address | 10.255.1.5 | PASS | - |
| 225 | DC1-BL1 | Routing Table | Remote Lo0 address | 10.250.1.7 | PASS | - |
| 226 | DC1-BL1 | Routing Table | Remote Lo0 address | 10.250.1.8 | PASS | - |
| 227 | DC1-BL1 | Routing Table | Remote Lo0 address | 10.250.1.3 | PASS | - |
| 228 | DC1-BL1 | Routing Table | Remote Lo0 address | 10.250.1.4 | PASS | - |
| 229 | DC1-BL1 | Routing Table | Remote Lo0 address | 10.250.1.5 | PASS | - |
| 230 | DC1-BL1 | Routing Table | Remote Lo0 address | 10.250.1.6 | PASS | - |
| 231 | DC1-BL1 | Routing Table | Remote Lo0 address | 10.250.1.1 | PASS | - |
| 232 | DC1-BL1 | Routing Table | Remote Lo0 address | 10.250.1.2 | PASS | - |
| 233 | DC1-BL2 | Routing Table | Remote Lo0 address | 10.250.1.7 | PASS | - |
| 234 | DC1-BL2 | Routing Table | Remote Lo0 address | 10.250.1.8 | PASS | - |
| 235 | DC1-BL2 | Routing Table | Remote Lo0 address | 10.250.1.3 | PASS | - |
| 236 | DC1-BL2 | Routing Table | Remote Lo0 address | 10.250.1.4 | PASS | - |
| 237 | DC1-BL2 | Routing Table | Remote Lo0 address | 10.250.1.5 | PASS | - |
| 238 | DC1-BL2 | Routing Table | Remote Lo0 address | 10.250.1.6 | PASS | - |
| 239 | DC1-BL2 | Routing Table | Remote Lo0 address | 10.250.1.1 | PASS | - |
| 240 | DC1-BL2 | Routing Table | Remote Lo0 address | 10.250.1.2 | PASS | - |
| 241 | DC1-CL1 | Routing Table | Remote Lo0 address | 10.250.1.7 | PASS | - |
| 242 | DC1-CL1 | Routing Table | Remote Lo0 address | 10.250.1.8 | PASS | - |
| 243 | DC1-CL1 | Routing Table | Remote Lo0 address | 10.250.1.3 | PASS | - |
| 244 | DC1-CL1 | Routing Table | Remote Lo0 address | 10.250.1.4 | PASS | - |
| 245 | DC1-CL1 | Routing Table | Remote Lo0 address | 10.250.1.5 | PASS | - |
| 246 | DC1-CL1 | Routing Table | Remote Lo0 address | 10.250.1.6 | PASS | - |
| 247 | DC1-CL1 | Routing Table | Remote Lo0 address | 10.250.1.1 | PASS | - |
| 248 | DC1-CL1 | Routing Table | Remote Lo0 address | 10.250.1.2 | PASS | - |
| 249 | DC1-CL2 | Routing Table | Remote Lo0 address | 10.250.1.7 | PASS | - |
| 250 | DC1-CL2 | Routing Table | Remote Lo0 address | 10.250.1.8 | PASS | - |
| 251 | DC1-CL2 | Routing Table | Remote Lo0 address | 10.250.1.3 | PASS | - |
| 252 | DC1-CL2 | Routing Table | Remote Lo0 address | 10.250.1.4 | PASS | - |
| 253 | DC1-CL2 | Routing Table | Remote Lo0 address | 10.250.1.5 | PASS | - |
| 254 | DC1-CL2 | Routing Table | Remote Lo0 address | 10.250.1.6 | PASS | - |
| 255 | DC1-CL2 | Routing Table | Remote Lo0 address | 10.250.1.1 | PASS | - |
| 256 | DC1-CL2 | Routing Table | Remote Lo0 address | 10.250.1.2 | PASS | - |
| 257 | DC1-CL3 | Routing Table | Remote Lo0 address | 10.250.1.7 | PASS | - |
| 258 | DC1-CL3 | Routing Table | Remote Lo0 address | 10.250.1.8 | PASS | - |
| 259 | DC1-CL3 | Routing Table | Remote Lo0 address | 10.250.1.3 | PASS | - |
| 260 | DC1-CL3 | Routing Table | Remote Lo0 address | 10.250.1.4 | PASS | - |
| 261 | DC1-CL3 | Routing Table | Remote Lo0 address | 10.250.1.5 | PASS | - |
| 262 | DC1-CL3 | Routing Table | Remote Lo0 address | 10.250.1.6 | PASS | - |
| 263 | DC1-CL3 | Routing Table | Remote Lo0 address | 10.250.1.1 | PASS | - |
| 264 | DC1-CL3 | Routing Table | Remote Lo0 address | 10.250.1.2 | PASS | - |
| 265 | DC1-CL4 | Routing Table | Remote Lo0 address | 10.250.1.7 | PASS | - |
| 266 | DC1-CL4 | Routing Table | Remote Lo0 address | 10.250.1.8 | PASS | - |
| 267 | DC1-CL4 | Routing Table | Remote Lo0 address | 10.250.1.3 | PASS | - |
| 268 | DC1-CL4 | Routing Table | Remote Lo0 address | 10.250.1.4 | PASS | - |
| 269 | DC1-CL4 | Routing Table | Remote Lo0 address | 10.250.1.5 | PASS | - |
| 270 | DC1-CL4 | Routing Table | Remote Lo0 address | 10.250.1.6 | PASS | - |
| 271 | DC1-CL4 | Routing Table | Remote Lo0 address | 10.250.1.1 | PASS | - |
| 272 | DC1-CL4 | Routing Table | Remote Lo0 address | 10.250.1.2 | PASS | - |
| 273 | DC1-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL1 - 10.250.1.7 Destination: 10.250.1.7 | PASS | - |
| 274 | DC1-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL1 - 10.250.1.7 Destination: 10.250.1.8 | PASS | - |
| 275 | DC1-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL1 - 10.250.1.7 Destination: 10.250.1.3 | PASS | - |
| 276 | DC1-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL1 - 10.250.1.7 Destination: 10.250.1.4 | PASS | - |
| 277 | DC1-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL1 - 10.250.1.7 Destination: 10.250.1.5 | PASS | - |
| 278 | DC1-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL1 - 10.250.1.7 Destination: 10.250.1.6 | PASS | - |
| 279 | DC1-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL1 - 10.250.1.7 Destination: 10.250.1.1 | PASS | - |
| 280 | DC1-BL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL1 - 10.250.1.7 Destination: 10.250.1.2 | PASS | - |
| 281 | DC1-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL2 - 10.250.1.8 Destination: 10.250.1.7 | PASS | - |
| 282 | DC1-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL2 - 10.250.1.8 Destination: 10.250.1.8 | PASS | - |
| 283 | DC1-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL2 - 10.250.1.8 Destination: 10.250.1.3 | PASS | - |
| 284 | DC1-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL2 - 10.250.1.8 Destination: 10.250.1.4 | PASS | - |
| 285 | DC1-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL2 - 10.250.1.8 Destination: 10.250.1.5 | PASS | - |
| 286 | DC1-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL2 - 10.250.1.8 Destination: 10.250.1.6 | PASS | - |
| 287 | DC1-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL2 - 10.250.1.8 Destination: 10.250.1.1 | PASS | - |
| 288 | DC1-BL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-BL2 - 10.250.1.8 Destination: 10.250.1.2 | PASS | - |
| 289 | DC1-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL1 - 10.250.1.3 Destination: 10.250.1.7 | PASS | - |
| 290 | DC1-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL1 - 10.250.1.3 Destination: 10.250.1.8 | PASS | - |
| 291 | DC1-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL1 - 10.250.1.3 Destination: 10.250.1.3 | PASS | - |
| 292 | DC1-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL1 - 10.250.1.3 Destination: 10.250.1.4 | PASS | - |
| 293 | DC1-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL1 - 10.250.1.3 Destination: 10.250.1.5 | PASS | - |
| 294 | DC1-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL1 - 10.250.1.3 Destination: 10.250.1.6 | PASS | - |
| 295 | DC1-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL1 - 10.250.1.3 Destination: 10.250.1.1 | PASS | - |
| 296 | DC1-CL1 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL1 - 10.250.1.3 Destination: 10.250.1.2 | PASS | - |
| 297 | DC1-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL2 - 10.250.1.4 Destination: 10.250.1.7 | PASS | - |
| 298 | DC1-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL2 - 10.250.1.4 Destination: 10.250.1.8 | PASS | - |
| 299 | DC1-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL2 - 10.250.1.4 Destination: 10.250.1.3 | PASS | - |
| 300 | DC1-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL2 - 10.250.1.4 Destination: 10.250.1.4 | PASS | - |
| 301 | DC1-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL2 - 10.250.1.4 Destination: 10.250.1.5 | PASS | - |
| 302 | DC1-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL2 - 10.250.1.4 Destination: 10.250.1.6 | PASS | - |
| 303 | DC1-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL2 - 10.250.1.4 Destination: 10.250.1.1 | PASS | - |
| 304 | DC1-CL2 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL2 - 10.250.1.4 Destination: 10.250.1.2 | PASS | - |
| 305 | DC1-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL3 - 10.250.1.5 Destination: 10.250.1.7 | PASS | - |
| 306 | DC1-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL3 - 10.250.1.5 Destination: 10.250.1.8 | PASS | - |
| 307 | DC1-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL3 - 10.250.1.5 Destination: 10.250.1.3 | PASS | - |
| 308 | DC1-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL3 - 10.250.1.5 Destination: 10.250.1.4 | PASS | - |
| 309 | DC1-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL3 - 10.250.1.5 Destination: 10.250.1.5 | PASS | - |
| 310 | DC1-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL3 - 10.250.1.5 Destination: 10.250.1.6 | PASS | - |
| 311 | DC1-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL3 - 10.250.1.5 Destination: 10.250.1.1 | PASS | - |
| 312 | DC1-CL3 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL3 - 10.250.1.5 Destination: 10.250.1.2 | PASS | - |
| 313 | DC1-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL4 - 10.250.1.6 Destination: 10.250.1.7 | PASS | - |
| 314 | DC1-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL4 - 10.250.1.6 Destination: 10.250.1.8 | PASS | - |
| 315 | DC1-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL4 - 10.250.1.6 Destination: 10.250.1.3 | PASS | - |
| 316 | DC1-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL4 - 10.250.1.6 Destination: 10.250.1.4 | PASS | - |
| 317 | DC1-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL4 - 10.250.1.6 Destination: 10.250.1.5 | PASS | - |
| 318 | DC1-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL4 - 10.250.1.6 Destination: 10.250.1.6 | PASS | - |
| 319 | DC1-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL4 - 10.250.1.6 Destination: 10.250.1.1 | PASS | - |
| 320 | DC1-CL4 | Loopback0 Reachability | Loopback0 Reachability | Source: DC1-CL4 - 10.250.1.6 Destination: 10.250.1.2 | PASS | - |
