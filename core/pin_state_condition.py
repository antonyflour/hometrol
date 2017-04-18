from condition import ConditionInterface

class PinStateCondition(ConditionInterface):

    def __init__(self, pin, state):
        self.pin = pin
        self.state = state

    def isVerified(self):
        if self.pin.stato == self.state:
            return True
        return False