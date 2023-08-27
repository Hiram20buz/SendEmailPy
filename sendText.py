import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

# Email configuration
sender_email = emailData[0]
receiver_email = emailData[1]
subject = "Subject of the Email"
message = "Hello, this is the email body."

# Create the email content
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(message, "plain"))

# Connect to Gmail's SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = userData[0]
smtp_password = userData[1]

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully.")
