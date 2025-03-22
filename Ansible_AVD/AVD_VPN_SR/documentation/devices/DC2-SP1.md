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
- [MPLS](#mpls)
  - [MPLS and LDP](#mpls-and-ldp)
  - [MPLS Interfaces](#mpls-interfaces)
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
| Ethernet1 | P2P_LINK_TO_DC2-CL1_Ethernet1 | routed | - | 100.64.2.1/31 | default | 1500 | False | - | - |
| Ethernet2 | P2P_LINK_TO_DC2-CL2_Ethernet1 | routed | - | 100.64.2.5/31 | default | 1500 | False | - | - |
| Ethernet3 | P2P_LINK_TO_DC2-CL3_Ethernet1 | routed | - | 100.64.2.11/31 | default | 1500 | False | - | - |
| Ethernet4 | P2P_LINK_TO_DC2-CL4_Ethernet1 | routed | - | 100.64.2.15/31 | default | 1500 | False | - | - |
| Ethernet5 | P2P_LINK_TO_DC2-BL1_Ethernet1 | routed | - | 100.64.2.21/31 | default | 1500 | False | - | - |
| Ethernet6 | P2P_LINK_TO_DC2-BL2_Ethernet1 | routed | - | 100.64.2.25/31 | default | 1500 | False | - | - |
| Ethernet7 | P2P_LINK_TO_DC2-SP2_Ethernet7 | routed | - | 100.64.2.30/31 | default | 1500 | False | - | - |

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet1 | - | CORE | - | 50 | point-to-point | level-2 | False | md5 |
| Ethernet2 | - | CORE | - | 50 | point-to-point | level-2 | False | md5 |
| Ethernet3 | - | CORE | - | 50 | point-to-point | level-2 | False | md5 |
| Ethernet4 | - | CORE | - | 50 | point-to-point | level-2 | False | md5 |
| Ethernet5 | - | CORE | - | 50 | point-to-point | level-2 | False | md5 |
| Ethernet6 | - | CORE | - | 50 | point-to-point | level-2 | False | md5 |
| Ethernet7 | - | CORE | - | 50 | point-to-point | level-2 | False | md5 |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC2-CL1_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 100.64.2.1/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 50
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
!
interface Ethernet2
   description P2P_LINK_TO_DC2-CL2_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 100.64.2.5/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 50
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
!
interface Ethernet3
   description P2P_LINK_TO_DC2-CL3_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 100.64.2.11/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 50
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
!
interface Ethernet4
   description P2P_LINK_TO_DC2-CL4_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 100.64.2.15/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 50
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
!
interface Ethernet5
   description P2P_LINK_TO_DC2-BL1_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 100.64.2.21/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 50
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
!
interface Ethernet6
   description P2P_LINK_TO_DC2-BL2_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 100.64.2.25/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 50
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
!
interface Ethernet7
   description P2P_LINK_TO_DC2-SP2_Ethernet7
   no shutdown
   mtu 1500
   no switchport
   ip address 100.64.2.30/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 50
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | LSR_Router_ID | default | 10.250.2.1/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | LSR_Router_ID | default | - |

##### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | CORE | - | passive |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description LSR_Router_ID
   no shutdown
   ip address 10.250.2.1/32
   isis enable CORE
   isis passive
   mpls ldp interface
   node-segment ipv4 index 11
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
| Instance | CORE |
| Net-ID | 49.0001.1921.6820.0001.00 |
| Type | level-2 |
| Router-ID | 10.250.2.1 |
| Log Adjacency Changes | True |
| MPLS LDP Sync Default | True |
| Advertise Passive-only | True |
| SR MPLS Enabled | True |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet1 | CORE | 50 | point-to-point |
| Ethernet2 | CORE | 50 | point-to-point |
| Ethernet3 | CORE | 50 | point-to-point |
| Ethernet4 | CORE | 50 | point-to-point |
| Ethernet5 | CORE | 50 | point-to-point |
| Ethernet6 | CORE | 50 | point-to-point |
| Ethernet7 | CORE | 50 | point-to-point |
| Loopback0 | CORE | - | passive |

#### ISIS Segment-routing Node-SID

| Loopback | IPv4 Index | IPv6 Index |
| -------- | ---------- | ---------- |
| Loopback0 | 11 | - |

#### ISIS IPv4 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv4 Address-family Enabled | True |
| Maximum-paths | 128 |

#### Router ISIS Device Configuration

```eos
!
router isis CORE
   net 49.0001.1921.6820.0001.00
   is-type level-2
   router-id ipv4 10.250.2.1
   log-adjacency-changes
   mpls ldp sync default
   advertise passive-only
   !
   address-family ipv4 unicast
      maximum-paths 128
   !
   segment-routing mpls
      no shutdown
```

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | True |
| LDP Enabled | True |
| LDP Router ID | 10.250.2.1 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | Loopback0 |

#### MPLS and LDP Device Configuration

```eos
!
mpls ip
!
mpls ldp
   interface disabled default
   router-id 10.250.2.1
   no shutdown
   transport-address interface Loopback0
```

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Ethernet1 | True | True | True |
| Ethernet2 | True | True | True |
| Ethernet3 | True | True | True |
| Ethernet4 | True | True | True |
| Ethernet5 | True | True | True |
| Ethernet6 | True | True | True |
| Ethernet7 | True | True | True |
| Loopback0 | - | True | - |

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
