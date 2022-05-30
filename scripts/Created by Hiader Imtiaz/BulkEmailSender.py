# Bulk Email Sender
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders, message
from email.mime.multipart import MIMEMultipart
import smtplib
# send email 
def send_email(email_list, subject, body):
mail_ID = 'SENDER_EMAIL'
    mail_pass = 'SENDER_EMAIL_PASSWORD'
    subject = 'EMAIL_SUBJECT'
    msg = MIMEMultipart()
    msg['From'] = mail_ID
    msg['To'] = ", ".join(email_list)
    msg['Subject'] = subject
    body = 'EMAIL_BODY'
    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(mail_ID,mail_pass)
    server.sendmail(mail_ID, email_list,text)
    server.quit()
send_email(['email1', 'email2'], 'EMAIL_SUBJECT', 'EMAIL_BODY')