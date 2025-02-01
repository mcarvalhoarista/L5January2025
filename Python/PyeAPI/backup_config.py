#!/Users/mcarvalho/VENV/bin/python3
# change file permision "chmod +x " 

import pyeapi
import os
import yaml

pyeapi.load_config('eapi.conf')


file = open('switches_list.yml', 'r')
switches_list = yaml.safe_load(file)

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)


# for switch in switches_list['switches']:
#     connect = pyeapi.connect_to(switch)
#     running_config = connect.get_config(as_string='True')
#     # path = directory+'/'+switch+'.cfg'
#     path = f"{directory}/{switch}.cfg"
#     file = open(path,'w')
#     file.write(running_config)
#     file.close()
#     print(f"Backing up {switch}")

total_config = []

for switch in switches_list['switches']:
    if "DC" in switch:
        print(switch)
        connect = pyeapi.connect_to(switch)
        running_config = connect.get_config()
        line1 = f"### Show Running-Config for Device:{switch} ###"
        line2 = "#" + "-" * len(line1)
        all_lines = [line2, line1, line2]
        total_config.extend(all_lines)
        total_config.extend(running_config)

with open("configs/total_config.txt", "w") as outfile:
    outfile.write("\n".join(str(item) for item in total_config))
