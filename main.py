import requests
import sys

SERVER_URL = "10.0.1.21"
TOKEN = sys.argv[1]
URL = f'https://{SERVER_URL}/api/groups'
HEADERS = {"Authorization": f'BEARER {TOKEN}', "Content-Type": "application/json"}
GROUP_NAME = morpheus['customOptions']['subgroupname']
GROUP_CODE = morpheus['customOptions']['subgroupcode']
GROUP_LOCATION = morpheus['customOptions']['subgrouplocation']
PAYLOAD = {"group": {"name": GROUP_NAME, "code": GROUP_CODE, "location": GROUP_LOCATION}}

response = requests.post(URL, json=PAYLOAD, headers=HEADERS)
print('Group Added Successfully.')