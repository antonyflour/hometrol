from core.conditions.condition import ConditionInterface

class PinStateAlterationCondition(ConditionInterface):

    def __init__(self, id, shield, pin, expected_state):
        self.id = id
        self.shield = shield
        self.pin = pin
        self.expected_state = expected_state

    def isVerified(self):
        if self.pin.stato == self.expected_state:
            return True
        return False