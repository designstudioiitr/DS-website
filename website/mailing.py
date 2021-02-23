import smtplib
import ftplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(subject, body, render=""):

    '''Mailer function'''

    sender = 'designstudio.designiitr@gmail.com'

    msg = MIMEMultipart()
    msg2 = MIMEText("{}".format(body))

    msg['Subject'] = "Design studio contact mail from : " + subject
    msg['From'] = sender
    msg['To'] = ""

    msg.attach(msg2)

    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(sender,"*1Sujihai")

    smtpserver.sendmail(sender, sender, msg.as_string())
    smtpserver.quit()
