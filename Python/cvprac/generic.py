from cvprac import cvp_client as cvp_client
import requests
import os

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


### https://cvprac.readthedocs.io/en/latest/cvprac.html#

cvp1 = "10.88.160.63"
cvp_user = "cvpadmin"
cvp_pw = "arista123"

client = cvp_client.CvpClient()

client.connect([cvp1], cvp_user, cvp_pw)


# ## Get CVP Info
# result = client.get('/cvpInfo/getCvpInfo.do')
# print(result)


# ## Get CVP Containers
# result = client.api.get_containers()
# for itens in result['data']:
#     print(f"{itens['name']} under {itens['parentName']}")

# ## Get Inventory
# result = client.api.get_inventory()
# for itens in result:
#     print(itens['hostname'], itens['ipAddress'])

# ##ADD configlet from file
# configlet_name = 'test557'
# with open(os.path.join('configs', 'test8888.txt'), "r") as f:
#     text = f.read()
# client.api.add_configlet(configlet_name , text)

## Delete Configlet
try:
    configlet_name = 'test557'
    result = client.api.get_configlet_by_name(configlet_name)
    print (f'KEY assigned to configlet "{configlet_name}": "{result['key']}"')
    client.api.delete_configlet(configlet_name, result['key'])
    print (f'Configlet "{configlet_name}" deleted')
except:
    print(f'Configlet "{configlet_name}" DO NOT EXIST')
