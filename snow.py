# Need to install requests package for python
# easy_install requests
import requests
import json
import xlwt
import getUserDetails
import userCredentials
import styleSheet
#import incidentValidation
#from datetime import datetime


class Incident:
    def __init__(self, incidentId, openedBy, sysCreatedOn, priority, assignedTo, short_description):
        self.incidentId = incidentId
        self.openedBy = openedBy
        self.sysCreatedOn = sysCreatedOn
        self.priority = priority
        self.assignedTo = assignedTo
        self.short_description = short_description

    def __str__(self):
        return "Incident> Id: %s, opened_by: %s, sys_created_on: %s, priority: %s, assignedTo %s,short_description %s" % (
        self.incidentId, self.openedBy, self.sysCreatedOn, self.priority, self.assignedTo, self.short_description)


# Set the request parameters
#url = 'https://dev43599.service-now.com/api/now/table/incident?sysparm_query=active=true^assignment_group=d71f7935c0a8016700802b64c67c11c6^ORDERBYnumber'
url = 'https://dev43599.service-now.com/api/now/table/incident?sysparm_query=active=true^ORDERBYnumber'
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

Record_list = []
for element in resData['result']:
    if element["assigned_to"] =='':
        incident = Incident(element["number"], element["opened_by"]["value"], element["sys_created_on"], element["priority"]
                            , element["assigned_to"], element["short_description"])
    else:
        incident = Incident(element["number"], element["opened_by"]["value"], element["sys_created_on"], element["priority"]
                            , element["assigned_to"]["value"], element["short_description"])
    print(incident)
    Record_list.append(incident)

print("Records fetched:", len(Record_list))

style0 = xlwt.easyxf('font: name Times New Roman, color-index  blue', num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('Incident', cell_overwrite_ok=False)


# Column Names
ws.write(0, 0, 'Incident', style0)
ws.write(0, 1, 'Opened By', style0)
ws.write(0, 2, 'Assigned To', style0)
ws.write(0, 3, 'Start Time', style0)
ws.write(0, 4, 'Short Description', style0)

i = 0
row = 1
col = 0

# Writing data to Excel
while i < len(Record_list):

    # Validating incident priority
    if Record_list[i].priority == '1' or Record_list[i].priority == '2':
        p_style = xlwt.easyxf('font: color-index  red', num_format_str='#,##0.00')
        ws.write(row, col, Record_list[i].incidentId, p_style)
    else:
        ws.write(row, col, Record_list[i].incidentId)

    ws.write(row, col + 1, getUserDetails.get_user_name(Record_list[i].openedBy))
    ws.write(row, col + 2, getUserDetails.get_user_name(Record_list[i].assignedTo))
    ws.write(row, col + 3, Record_list[i].sysCreatedOn)
    colLen = len(Record_list[i].short_description)
    ws.write(row, col + 4, Record_list[i].short_description, style=styleSheet.set_style('Times New Roman', 220))
    row += 1
    i += 1

print("writing data in file...")
wb.save('D:/example.xls')
