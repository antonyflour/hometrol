import threading
from condition import ConditionInterface
from action import ActionInterface
from json_encoder import *
import datetime
import json

class Evento():


    # condizione da verificare, azione da compiere se la condizione e' verificata, intervallo di ripetizione dell'azione
    def __init__(self, id, condition, action, repetitionInterval = 10):

        if isinstance(condition, ConditionInterface) and \
                isinstance(action, ActionInterface):
            self.condition = condition
            self.action = action
        else:
            raise TypeError()
        self.id = id
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



class JsonEventEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Evento):
            return {"id" : obj.id,
                    "condition": json.dumps(obj.condition, cls=JsonConditionEncoder),
                    "action" : json.dumps(obj.action, cls=JsonActionEncoder),
                    "repetitionInterval" : obj.repetitionInterval,
                    }

        return json.JSONEncoder.default(self, obj)
