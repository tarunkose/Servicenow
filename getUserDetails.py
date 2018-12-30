# Need to install requests package for python
# easy_install requests
import requests
import json
import userCredentials

url = 'https://dev43599.service-now.com/api/now/table/sys_user?sysparm_query=active=true'
# Eg. User name="username", Password="password" for this code sample.
user = userCredentials.snowuser
pwd = userCredentials.snowpwd

# Set proper headers
headers = {"Content-Type": "application/json", "Accept": "application/json"}
response = requests.get(url, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)
    exit()

# Decode the XML response into a dictionary and use the data
# print(type(response.content.decode("utf-8")))

resData = json.loads(response.content.decode("utf-8"))
print(resData)
Rec_list = {}
for element in resData['result']:
    Rec_list.update({element["sys_id"]: element["name"]})


def get_user_name(usr_id):
    return Rec_list.get(usr_id)

print(Rec_list)
