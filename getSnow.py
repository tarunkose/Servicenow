# Need to install requests package for python
# easy_install requests
import requests
import json

# Set the request parameters
url = 'https://dev24748.service-now.com/api/now/table/incident'

# Eg. User name="username", Password="password" for this code sample.
user = 'admin'
pwd = 'Welcome001;'

# Set proper headers
headers = {"Content-Type": "application/json", "Accept": "application/json"}

response = requests.get(url, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)
    exit()

# Decode the XML response into a dictionary and use the data
print(type(response.content.decode("utf-8")))

resData = json.loads(response.content.decode("utf-8"))
print(resData["result"][0]["number"])

