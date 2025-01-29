# DC2-SP1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [NTP](#ntp)
  - [Management SSH](#management-ssh)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [IP TACACS Source Interfaces](#ip-tacacs-source-interfaces)
  - [AAA Authorization](#aaa-authorization)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
  - [Logging](#logging)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [Interfaces](#interfaces)
  - [Switchport Default](#switchport-default)
  - [Interface Defaults](#interface-defaults)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | Management_Interface | oob | MGMT | 10.88.169.139/24 | 10.88.169.129 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | Management_Interface | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description Management_Interface
   no shutdown
   vrf MGMT
   ip address 10.88.169.139/24
```

### DNS Domain

DNS domain: atd.lab

#### DNS Domain Device Configuration

```eos
dns domain atd.lab
!
```

### NTP

#### NTP Summary

##### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 0.pool.ntp.org | MGMT | - | - | True | - | - | - | Management1 | - |

#### NTP Device Configuration

```eos
!
ntp server vrf MGMT 0.pool.ntp.org iburst local-interface Management1
```

### Management SSH

#### SSH Timeout and Management

| Idle Timeout | SSH Management |
| ------------ | -------------- |
| 5 | Enabled |

#### Max number of SSH sessions limit and per-host limit

| Connection Limit | Max from a single Host |
| ---------------- | ---------------------- |
| - | - |

#### Ciphers and Algorithms

| Ciphers | Key-exchange methods | MAC algorithms | Hostkey server algorithms |
|---------|----------------------|----------------|---------------------------|
| default | default | default | default |

#### VRFs

| VRF | Status |
| --- | ------ |
| MGMT | Enabled |

#### Management SSH Device Configuration

```eos
!
management ssh
   idle-timeout 5
   no shutdown
   !
   vrf MGMT
      no shutdown
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| arista | 15 | network-admin | False | - |
| cvpadmin | 15 | network-admin | False | - |
| marcelo | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username arista privilege 15 role network-admin secret sha512 <removed>
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
username marcelo privilege 15 role network-admin secret sha512 <removed>
```

### IP TACACS Source Interfaces

#### IP TACACS Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| MGMT | Management1 |

#### IP TACACS Source Interfaces Device Configuration

```eos
!
ip tacacs vrf MGMT source-interface Management1
```

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | local |

Authorization for configuration commands is disabled.

#### AAA Authorization Device Configuration

```eos
aaa authorization exec default local
!
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 10.88.160.63:9910 | MGMT | token,/tmp/token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=10.88.160.63:9910 -cvauth=token,/tmp/token -cvvrf=MGMT -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

### Logging

#### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |

| VRF | Source Interface |
| --- | ---------------- |
| MGMT | Management1 |

| VRF | Hosts | Ports | Protocol |
| --- | ----- | ----- | -------- |
| MGMT | 10.200.0.108 | Default | UDP |
| MGMT | 10.200.1.108 | Default | UDP |

#### Logging Servers and Features Device Configuration

```eos
!
logging vrf MGMT host 10.200.0.108
logging vrf MGMT host 10.200.1.108
logging vrf MGMT source-interface Management1
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## Interfaces

### Switchport Default

#### Switchport Defaults Summary

- Default Switchport Mode: routed

#### Switchport Default Device Configuration

```eos
!
switchport default mode routed
```

### Interface Defaults

#### Interface Defaults Summary

- Default Ethernet Interface Shutdown: True

- Default Routed Interface MTU: 1500

#### Interface Defaults Device Configuration

```eos
!
interface defaults
   ethernet
      shutdown
   mtu 1500
```

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC2-CL1_Ethernet1 | routed | - | 172.16.2.36/31 | default | 1500 | False | - | - |
| Ethernet2 | P2P_LINK_TO_DC2-CL2_Ethernet1 | routed | - | 172.16.2.40/31 | default | 1500 | False | - | - |
| Ethernet3 | P2P_LINK_TO_DC2-CL3_Ethernet1 | routed | - | 172.16.2.8/31 | default | 1500 | False | - | - |
| Ethernet4 | P2P_LINK_TO_DC2-CL4_Ethernet1 | routed | - | 172.16.2.12/31 | default | 1500 | False | - | - |
| Ethernet5 | P2P_LINK_TO_DC2-BL1_Ethernet1 | routed | - | 172.16.2.16/31 | default | 1500 | False | - | - |
| Ethernet6 | P2P_LINK_TO_DC2-BL2_Ethernet1 | routed | - | 172.16.2.20/31 | default | 1500 | False | - | - |

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet1 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet2 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet3 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet4 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet5 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet6 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC2-CL1_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.2.36/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet2
   description P2P_LINK_TO_DC2-CL2_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.2.40/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet3
   description P2P_LINK_TO_DC2-CL3_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.2.8/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet4
   description P2P_LINK_TO_DC2-CL4_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.2.12/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet5
   description P2P_LINK_TO_DC2-BL1_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.2.16/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet6
   description P2P_LINK_TO_DC2-BL2_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.2.20/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.250.2.1/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |

##### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | EVPN_UNDERLAY | - | passive |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.250.2.1/32
   isis enable EVPN_UNDERLAY
   isis passive
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 10.88.169.129 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 10.88.169.129
```

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| Net-ID | 49.0001.1921.6820.0001.00 |
| Type | level-2 |
| Router-ID | 10.250.2.1 |
| Log Adjacency Changes | True |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet1 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet2 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet3 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet4 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet5 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet6 | EVPN_UNDERLAY | 50 | point-to-point |
| Loopback0 | EVPN_UNDERLAY | - | passive |

#### ISIS IPv4 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv4 Address-family Enabled | True |
| Maximum-paths | 128 |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   net 49.0001.1921.6820.0001.00
   is-type level-2
   router-id ipv4 10.250.2.1
   log-adjacency-changes
   !
   address-family ipv4 unicast
      maximum-paths 128
   !
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65200 | 10.250.2.1 |

| BGP AS | Cluster ID |
| ------ | --------- |
| 65200 | 10.250.2.1 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Remote AS | 65200 |
| Route Reflector Client | Yes |
| Source | Loopback0 |
| BFD | True |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.250.2.5 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - |
| 10.250.2.6 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - |
| 10.250.2.7 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - |
| 10.250.2.8 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - |
| 10.250.2.12 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - |
| 10.250.2.13 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

#### Router BGP Device Configuration

```eos
!
router bgp 65200
   router-id 10.250.2.1
   maximum-paths 4 ecmp 4
   no bgp default ipv4-unicast
   bgp cluster-id 10.250.2.1
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65200
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS route-reflector-client
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor 10.250.2.5 peer group EVPN-OVERLAY-PEERS
   neighbor 10.250.2.5 description DC2-CL3
   neighbor 10.250.2.6 peer group EVPN-OVERLAY-PEERS
   neighbor 10.250.2.6 description DC2-CL4
   neighbor 10.250.2.7 peer group EVPN-OVERLAY-PEERS
   neighbor 10.250.2.7 description DC2-BL1
   neighbor 10.250.2.8 peer group EVPN-OVERLAY-PEERS
   neighbor 10.250.2.8 description DC2-BL2
   neighbor 10.250.2.12 peer group EVPN-OVERLAY-PEERS
   neighbor 10.250.2.12 description DC2-CL1
   neighbor 10.250.2.13 peer group EVPN-OVERLAY-PEERS
   neighbor 10.250.2.13 description DC2-CL2
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```
