from action import ActionInterface
import time

class PrintAction(ActionInterface):

    def __init__(self, id, msg):
        self.id = id
        self.msg = msg

    def execute(self):
        time.sleep(1)
        print self.msg