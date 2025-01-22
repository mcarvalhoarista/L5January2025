import yaml
import pyeapi
import pprint

## Modules
## https://pyeapi.readthedocs.io/en/latest/modules.html

file = open('vlans.yml', 'r')

pyeapi.load_config('eapi.conf')
vlan_dict = yaml.safe_load(file)

# for switch in vlan_dict['switches']:
#     print(f"Connecting to {switch}")
#     connect = pyeapi.connect_to(switch)
#     mlag = connect.api('mlag')
#     mlag_dic = mlag.get()
#     pprint.pprint(mlag_dic)

# for switch in vlan_dict['switches']:
#     print(f"Connecting to {switch}")
#     connect = pyeapi.connect_to(switch)
#     bgp = connect.api('bgp')
#     bgp_dic = bgp.get()
#     pprint.pprint(bgp_dic)

# for switch in vlan_dict['switches']:
#     print(f"Connecting to {switch}")
#     connect = pyeapi.connect_to(switch)
#     # generic = connect.api('acl')
#     # generic = connect.api('interfaces')
#     # generic = connect.api('staticroute')
#     generic = connect.api('vrfs')  
#     generic_dic = generic.getall()
#     pprint.pprint(generic_dic)


for switch in vlan_dict['switches']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    connect.api('ipinterfaces').create('Ethernet5')
    # connect.api('baseinterface').set_shutdown('Ethernet5')
    connect.api('interfaces').create('Ethernet5.100')
    connect.api('interfaces').set_encapsulation('Ethernet5.100', 100)
    connect.api('ipinterfaces').set_address('Ethernet5.100', '9.9.9.9/24')
    generic = connect.api('interfaces')  
    generic_dic = generic.getall()
    pprint.pprint(generic_dic)
