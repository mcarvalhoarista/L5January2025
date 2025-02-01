import yaml
import pyeapi
import re
import ssl
import json
import sys

sys.tracebacklimit = 0

# Use TLSv1.2
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.minimum_version = ssl.TLSVersion.TLSv1_2
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Using the EOS default ciphers
context.set_ciphers('AES256-SHA:DHE-RSA-AES256-SHA:AES128-SHA:DHE-RSA-AES128-SHA')



# Expresiones regulares para buscar los datos
pattern_248 = re.compile(r"248 .* (\d+)\n")
pattern_model = re.compile(r"Device Model: .* (\S+ \S+)\n")

# Create file list under "devices.yml"
file = open('devices.yml', 'r')
# load yml file with devices list
devices_dict = yaml.safe_load(file)

# Switch Credentials
username = "admin"        ## Modify credentials
password = "Aristaps@123" ## Modify credentials


SSD_SW_DIC = {}
x = 0
y = 0

for switch in devices_dict['switches']:
    print(f"\nConnecting to {switch}")
    try:
        connect = pyeapi.client.connect(host=switch, username=username, password=password, context=context)
        output_1 = connect.execute(['show hostname', 'show version'])
        hostname = output_1['result'][0]['hostname']
        model_id = output_1['result'][1]['modelName']
        try:
            output_2 = connect.execute(['bash timeout 2 sudo smartctl -A --info /dev/sda | grep "Device Model"','bash timeout 2 sudo smartctl -A --info /dev/sda | grep "248 "'])
            line_1 = output_2['result'][0]['messages'][0]
            line_2 = output_2['result'][1]['messages'][0]
            print (f"Switch {hostname} with model {model_id} have the following SSD:")
            if re.match(r"Device Model: .*\n", line_1):
                ssd_model = str((pattern_model.search(line_1)).group(1))

            if re.match(r"248 .*\n", line_2):
                lifetime = str((pattern_248.search(line_2)).group(1))

            try:
                SSD_SW_DIC[hostname] = {}
                SSD_SW_DIC[hostname]["MODEL"] = model_id
                SSD_SW_DIC[hostname]["SSD_MODEL"] = ssd_model
                SSD_SW_DIC[hostname]["SSD_LIFETIME"] = lifetime
                print (f"SSD_MODEL = {ssd_model}")
                print (f"SSD_LIFETIME = {lifetime}")
                x += 1
            except:
                ssd_model = line_1.rstrip("\n")
                lifetime = line_2.rstrip("\n")
                print (f"SSD_MODEL = {ssd_model}")
                print (f"SSD_LIFETIME = {lifetime}")
                x += 1

        except:
            print (f"Switch {hostname} with model {model_id} do NOT support the SSD command")
            y += 1
    except:
        print (f"Switch {switch} do NOT have eAPI enabled or wrong credentials")
        y += 1

filename = "SSD_MODELs_LIFETIME.json"

SSD_SW_DIC_file = open(filename, "w")
SSD_SW_DIC_file = json.dump(SSD_SW_DIC, SSD_SW_DIC_file, indent=4, sort_keys=True)

print(f'\nTotal of switches in the list = {x+y}')
print(f'Total of switches with SSD info= {x}')
print(f'Total of switches without SSD info= {y}')
