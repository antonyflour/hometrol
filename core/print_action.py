from action import ActionInterface
import time

class PrintAction(ActionInterface):

    def __init__(self, msg):
        self.msg = msg

    def execute(self):
        time.sleep(1)
        print self.msg