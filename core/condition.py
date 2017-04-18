from abc import ABCMeta
from abc import abstractmethod

class ConditionInterface:

    __metaclass__ = ABCMeta

    #restituisce vero se la condizione e' rispettata
    @abstractmethod
    def isVerified(self):
        pass


