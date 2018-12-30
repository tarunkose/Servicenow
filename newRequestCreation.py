# Need to install requests package for python
# easy_install requests
import requests
import json


class RequestCls:
    def __init__(self, openedby, requested_for, short_des):
        self.openedby = openedby
        self.requested_for = requested_for
        self.short_des = short_des

    def __str__(self):
        return "Incident> Id: %s, opened_by: %s, requested_for %s, short_des: %s" % (
            self.openedby, self.requested_for, self.short_des)


# Set the request parameters
# url = 'https://dev24748.service-now.com/api/now/table/incident'
url = 'https://dev24748.service-now.com/api/now/table/sc_request'
# Eg. User name="username", Password="password" for this code sample.
user = 'admin'
pwd = 'Welcome001;'

# Set proper headers
headers = {"Content-Type": "application/json", "Accept": "application/json"}
'''
# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers, data="{\"opened_by\":\"kyle.lindauer\","
                                                                      "\"category\":\"Request\","
                                                                      "\"subcategory\":\"Other\","
                                                                      "\"business_service\":\"AirWatch MDM\","
                                                                      "\"cmdb_ci\":\"LTAC0001\","
                                                                      "\"contact_type\":\"Automation\","
                                                                      "\"impact\":\"2\",\"urgency\":\"2\","
                                                                      "\"short_description\":\"T     his is for testing -"
                                                                      "description summary field 2!\","
                                                                      "\"comments\":\"This could be the long "
                                                                      "description as needed.\","
                                                                      "\"assignment_group\":\"MCD Triage\"}")
'''
response = requests.post(url, auth=(user, pwd), headers=headers, data="{\"opened_by\":\"kyle.lindauer\","
                                                                      "\"category\":\"Request\","
                                                                      "\"requested_for\":\"Tia Lino\","
                                                                      "\"subcategory\":\"Other\","
                                                                      "\"assigned_to\":\"Prince Kauk\","
                                                                      "\"cmdb_ci\":\"LTAC0001\","
                                                                      "\"contact_type\":\"Automation\","
                                                                      "\"short_description\":\"Request creation test\","
                                                                      "\"description\":\"This is a request creation test. we are putting data in description test box \","
                                                                      "\"comments\":\"This could be the long description as needed.\","
                                                                      "\"assignment_group\":\"MCD Triage\"}")

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
#data = response.json()
#print(data)

resData = json.loads(response.content.decode("utf-8"))

Req_res_list = []
for element in resData['result']:
    req_res = RequestCls(element["opened_by"]["value"],
                          element["requested_for"]["value"],
                          element["short_description"])
    print(req_res)
    Req_res_list.append(req_res)

print("Printing request response:")
print(Req_res_list)
