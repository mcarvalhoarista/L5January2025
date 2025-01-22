import yaml
import pyeapi
import pprint


file = open('vlans.yml', 'r')

pyeapi.load_config('eapi.conf')
vlan_dict = yaml.safe_load(file)

for switch in vlan_dict['switches']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    output = connect.enable(['show bgp summary','show version'])
    # pprint.pprint (output[1]['result'])
    print(f"System MAC address is {output[1]['result']['systemMacAddress']}")
    for value in output[0]['result'].values():
        for r_key, r_value in value.items():
            print(f"For VRF {r_key}, ASN is {r_value['asn']}, have the following peers with State:")
            for s_key, s_value in r_value['peers'].items():
                print(f"     - {s_key} on AS# {s_value['peerAsn']} is {s_value['peerState']}")   
    print("\n")
