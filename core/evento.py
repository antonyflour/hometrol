import threading
from condition import ConditionInterface
from action import ActionInterface
import datetime

class Evento():


    # condizione da verificare, azione da compiere se la condizione e' verificata, intervallo di ripetizione dell'azione
    def __init__(self, condition, action, repetitionInterval):

        if isinstance(condition, ConditionInterface) and \
                isinstance(action, ActionInterface):
            self.condition = condition
            self.action = action
        else:
            raise TypeError()

        self.repetitionInterval = repetitionInterval
        self.lastNotifyTime = None
        self.enabled = True


    def checkAndExecute(self):
        if self.isEnabled():
            now = datetime.datetime.today()
            if self.condition.isVerified():
                if self.lastNotifyTime == None or \
                        (now - self.lastNotifyTime).total_seconds() > (self.repetitionInterval*60):
                    thread = threading.Thread(target=self.action.execute)
                    thread.start()
                    print now
                    self.lastNotifyTime = now

    def isEnabled(self):
        return self.enabled

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True
