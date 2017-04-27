from core.actions.action import ActionInterface
from core.email_sender.gmail_email_sender import GmailEmailSender


class EmailNotifyAction(ActionInterface):

    def __init__(self, id, email, msg):
        self.id = id
        self.email = email
        self.msg = msg

    def execute(self):
        try:
            sender = GmailEmailSender("raspberryprova@gmail.com", "raspberry1234")
            sender.send(self.email, "HOMETROL NOTIFY", self.msg)
        except Exception:
            pass