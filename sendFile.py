import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


userData=[]
try:
    with open('user.txt', 'r') as file:
        file_contents = file.read()
        userData = file_contents.split('\n')
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    
emailData=[]
try:
    with open('data.txt', 'r') as file:
        file_contents = file.read()
        emailData = file_contents.split('\n')
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

print(emailData)
def sem():  
    fromaddr = emailData[0]
    toaddr = emailData[1]
       
    # instance of MIMEMultipart
    msg = MIMEMultipart()
      
    # storing the senders email address  
    msg['From'] = fromaddr
      
    # storing the receivers email address 
    msg['To'] = toaddr
      
    # storing the subject 
    msg['Subject'] = "Test1"
      
    # string to store the body of the mail
    body = "Body_of_the_mail"
      
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
      
    # open the file to be sent 
    arch="message.txt"
    filename = "message.txt"
    attachment = open(arch, "rb")
      
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
      
    # To change the payload into encoded form
    p.set_payload((attachment).read())
      
    # encode into base64
    encoders.encode_base64(p)
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
      
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
      
    # creates SMTP session
    s = smtplib.SMTP("smtp.gmail.com", 587)
      
    # start TLS for security
    s.starttls()
      
    # Authentication
    s.login(userData[0], userData[1])
      
    # Converts the Multipart msg into a string
    text = msg.as_string()
      
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
      
    # terminating the session
    s.quit()
    
sem()
