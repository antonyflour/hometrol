from abc import ABCMeta
from abc import abstractmethod

class ActionInterface:

    __metaclass__ = ABCMeta

    #metodo void per l'esecuzione dell'azione (es. invio notifica mail)
    @abstractmethod
    def execute(self):
        pass