import yaml
import pyeapi


file = open('vlans.yml', 'r')

pyeapi.load_config('eapi.conf')
vlan_dict = yaml.safe_load(file)

for switch in vlan_dict['switches']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    interfaces = connect.api('ipinterfaces')
    for r_key, r_value in interfaces.items():
        print(f"Interface {r_key}, have IP {r_value['address']}")
    print("\n")
