import re
from util import util
import system_email
from email_sender.gmail_email_sender import GmailEmailSender

x = "90-A2-DA-0F-45-D4"
if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", x.lower()):
    print "yes"
else:
    print "no"

print "EV-"+util.randstring()


email = system_email.SystemEmail("raspberryprova@gmail.com", "pRova1234")
sender = GmailEmailSender(email.address, email.password)
sender.send("antoniofarina1702@gmail.com","hometrol", "ciaociao")
