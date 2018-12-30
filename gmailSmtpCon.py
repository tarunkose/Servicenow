import smtplib


def get_conn(fromaddr, pwd):
    # creates SMTP session
    server_con = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    server_con.starttls()

    # Authentication
    server_con.login(fromaddr, pwd)

    return server_con