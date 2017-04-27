import datetime
import threading

from actions.action import ActionInterface
from conditions.condition import ConditionInterface
from json_encoder import JsonActionEncoder, JsonConditionEncoder
import json


class Evento():


    # condizione da verificare, azione da compiere se la condizione e' verificata, intervallo di ripetizione dell'azione
    def __init__(self, id, condition, action, repetitionInterval = 10):

        if (condition is None or isinstance(condition, ConditionInterface)) and \
                (action is None or isinstance(action, ActionInterface)):
            self.condition = condition
            self.action = action
        else:
            raise TypeError()
        self.id = id
        self.repetitionInterval = repetitionInterval
        self.lastExecutionTime = None
        self.enabled = True


    def checkAndExecute(self):
        if self.isEnabled():
            now = datetime.datetime.today()
            if self.condition.isVerified():
                if self.lastExecutionTime == None or \
                        (now - self.lastExecutionTime).total_seconds() > (self.repetitionInterval*60):
                    thread = threading.Thread(target=self.action.execute)
                    thread.start()
                    print now
                    self.lastExecutionTime = now

    def isEnabled(self):
        return self.enabled

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True



class JsonEventEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, Evento):
            timeSerialized = None
            if obj.lastExecutionTime is not None:
                timeSerialized = obj.lastExecutionTime.isoformat()
            return {"id" : obj.id,
                    "condition": json.dumps(obj.condition, cls=JsonConditionEncoder),
                    "action" : json.dumps(obj.action, cls=JsonActionEncoder),
                    "repetitionInterval" : obj.repetitionInterval,
                    "enabled" : obj.enabled,
                    "last_exec_time" : timeSerialized
                    }

        return json.JSONEncoder.default(self, obj)
