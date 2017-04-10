class Cosa:

    def __init__(self, nome, pin):
        self.pin = pin
        self.nome = nome
        self.stato = 0

    def getStato(self):
        return self.stato

    def getNome(self):
        return self.nome