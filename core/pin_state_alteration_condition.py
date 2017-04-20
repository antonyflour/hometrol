from condition import ConditionInterface

class PinStateAlterationCondition(ConditionInterface):

    def __init__(self, id, shield, pin, stato):
        self.id = id
        self.shield = shield
        self.pin = pin
        self.stato = stato

    def isVerified(self):
        if self.pin.stato == self.stato:
            return True
        return False