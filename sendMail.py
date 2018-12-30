# Python code to illustrate Sending mail from your Gmail account
import gmailSmtpCon
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import userCredentials


fromaddr = userCredentials.fromaddr
toaddr = userCredentials.toaddr
pwd = userCredentials.pwd


file_path = 'D:/example.xls'
file_name = "example.xls"
# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "Python email sending test"

# string to store the body of the mail
body = "his is python mail testing module"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = file_name
attachment = open(file_path, "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload(attachment.read())

# encode into base64
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# Getting gmail smtp connection
getConn = gmailSmtpCon.get_conn(fromaddr, pwd)

# Converts the Multipart msg into a string
text_msg = msg.as_string()

# sending the mail
getConn.sendmail(fromaddr, toaddr, text_msg)

# terminating the session
getConn.quit()
