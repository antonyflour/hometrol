
class SystemEmail():

    def __init__(self, address, password):
        self.address = address
        self.password = password

    def isSet(self):
        return self.address is not None

    def __str__(self):
        address = "None"
        if self.address is not None: address = self.address

        password = "None"
        if self.password is not None: password = self.password

        return address + " : " + password