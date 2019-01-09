import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage

# creates SMTP session
smtpServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)

emailContent = MIMEMultipart('alternative')



messageBody = "<h3>restaurant search results</h3>"

emailContent['Subject'] = 'Zomato search results'
emailContent['From'] = 'chatbotemailer123@gmail.com'
emailContent['To'] = 'yugadeepa.c@gmail.com'
emailContent.attach(MIMEText(messageBody,'html'))

smtpServer.ehlo()
smtpServer.login('chatbotemailer123@gmail.com','learn.123')
smtpServer.send_message(emailContent)
smtpServer.quit()
