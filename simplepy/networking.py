#from simplepy.simplepy import Simplepy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import simplepy

class Networking:

    def __init__(self):
        pass

    def sendMail(self,sender,receivers,subject,text,html,user,password):

        # me == my email address
        # you == recipient's email address
        me = sender
        you = sender

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = you

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        try:
            smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtpObj.ehlo()
            smtpObj.login(user, password)
            smtpObj.sendmail(sender, receivers, msg.as_string())
            simplepy.simplepy.Simplepy().log("Info", "Successfully sent email", __class__)
        except Exception as e:
            logMessage = "Error sending mail: " + str(e.args)
            simplepy.simplepy.Simplepy().log("Info",logMessage,__class__)