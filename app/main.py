
#importing the necessary libraries
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 

# creating message object instance 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = "sender_email_address"

# storing the receivers email address 
msg['To'] = "receiver_email_address"

# storing the subject 
msg['Subject'] = "Subject_of_the_mail"

# string to store the body of the mail 
body = "Body_of_the_mail"

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(msg['From'], "sender_email_password") 
