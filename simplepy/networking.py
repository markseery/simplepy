##########################################################################
#
#   Copyright / License notice 2022
#   --------------------------------
#
#   Permission is hereby granted, free of charge,
#       to any person obtaining a copy of this software
#       and associated documentation files (the “Software”),
#       to deal in the Software without restriction, including
#       without limitation the rights to use, copy, modify, merge,
#       publish, distribute, sublicense, and/or sell copies of the Software,
#       and to permit persons to whom the Software is furnished to do so,
#       subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included
#       in all copies or substantial portions of the Software.
#
##########################################################################

#from simplepy.simplepy import Simplepy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import simplepy

class Networking:

    def __init__(self):
        pass

    def isUrlReachable(self,url):
        import subprocess
        ip = url
        ret = subprocess.call("ping -c 1 %s" % ip,
            shell=True,
            stdout=open('/dev/null', 'w'),
            stderr=subprocess.STDOUT)
        if ret == 0:
            return True
        else:
            return False

    def sendMail(self,service,sender,receivers,subject,text,html,user,password):
 
        if service.upper() != "GMAIL":
            simplepy.simplepy.Simplepy().log("Error","Email service name invalid: "+service,__class__)
            return -1

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
