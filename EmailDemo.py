#! /usr/bin/python
# this is a python email sending demo

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("composing!")
print("Welcome to Your name's email system!")
you = input("Please input recipient's address:\n")
# me == my email address
# you == recipient's email address
me = "saarthi.jethi@gmail.com"   # change this to your email address
psw = input(print("Please input your password!\n"))  # skip this part

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Hello"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version). Change this part
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi Cary! <br>
       How are you? I am using a Python Email Sending Module writting to you!<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>

</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)  # change the SMTP server for other email servers

mail.ehlo()  # Please Google the difference between HELO and EHLO

mail.starttls()  # take an existing insecure connection and upgrade it to a secure connection using SSL/TLS

# this will be your email login information
mail.login('sjethi', 'password')           # you need to chang here
mail.sendmail(me, you, msg.as_string())
print("Email sent!")
mail.quit()
