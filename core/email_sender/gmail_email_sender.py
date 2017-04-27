import smtplib
from email import MIMEMultipart
from email import MIMEText

class GmailEmailSender:

    SERVER = "smtp.gmail.com"
    PORT = 587

    def __init__(self, fromAddress, fromPassword):
        self.fromAddress = fromAddress
        self.fromPassword = fromPassword


    def send(self, toAddress, subject, body):
        msg = MIMEMultipart.MIMEMultipart()
        msg['From'] = self.fromAddress
        msg['To'] = toAddress
        msg['Subject'] = subject

        msg.attach(MIMEText.MIMEText(body, 'plain'))
        server = smtplib.SMTP(self.SERVER, self.PORT)
        server.starttls()
        server.login(self.fromAddress, self.fromPassword)
        text = msg.as_string()
        server.sendmail(self.fromAddress, toAddress, text)
        server.quit()
