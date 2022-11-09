import smtplib # protocol to send mails
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# we're going to log in to and existing mailing account and send mails using smtp
# we can't just send mails directly from the python script

server = smtplib.SMTP('smtp.gmail.com', 25) # we're using port 25 for smtp

server.ehlo() # starts our server

# next we need to login to the account using our credentials
server.login('mail@mail.com', 'password123') # recommended that you encrypt your password from a different file

message = MIMEMultipart() # define the message as a MIME multipart -> can be treated like a dictionary
# we have the from
message['From'] = ''
# the to part
message['To'] = ''
# the subject
message['Subject'] = 'Just a test'

with open('mail_msg.txt', 'r') as f:
    msg = f.read()

message.attach(MIMEText(msg, 'plain')) # this is the message part

# if you wanted to attach an img
filename = ''
attachment = open(filename, 'rb') # we use read byte mode here because this is an image

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
message.attach(p)

text = message.as_string() # makes the entire thing a string
server.sendmail('sample@mail.com', 'sampletarget@mail.com', text)