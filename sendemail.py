import smtplib
from_addr = 'akinyelethompson@gmail.com'
to_addr = 'david@someemail.com'
from_name = ''
to_name = ''
subject = ''
msg = ''
message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
"""

message_to_send = message.format(from_name, from_addr, to_name,to_addr, subject, msg)
# Credentials (if needed)
username = 'akinyelethompson@gmail.com'
password = 'dkca ejuj nufl qyiy'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 