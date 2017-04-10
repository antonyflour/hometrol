import json

from pin import JsonPinEncoder


class Shield:

    def __init__(self, mac, nome, ip, port):
        self.mac = mac
        self.nome = nome
        self.ip = ip
        self.port = port
        self.input_pin = []
        self.output_pin = []

    def getShieldJson(self):
        return json.dumps(self.__dict__)

    def getInputPinByNumber(self, numero):
        for pin in self.input_pin:
            if str(pin.numero) == numero:
                return pin
        return None

    def getOutputPinByNumber(self, numero):
        for pin in self.output_pin:
            if str(pin.numero) == numero:
                return pin
        return None

    def getPinByNumber(self, numero):
        pin = self.getInputPinByNumber(numero)
        if pin == None:
            pin = self.getOutputPinByNumber(numero)
        return pin

class JsonShieldEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Shield):

            input_pin_json = "["
            for i in range(0,len(obj.input_pin)):
                input_pin_json+=json.dumps(obj.input_pin[i], cls=JsonPinEncoder)
                if (i != (len(obj.input_pin) - 1)):
                    input_pin_json += ","
            input_pin_json+="]"

            output_pin_json = "["
            #il for con il range equivale a while(i < len)
            for i in range(0, len(obj.output_pin)):
                output_pin_json += json.dumps(obj.output_pin[i], cls=JsonPinEncoder)
                if (i != (len(obj.output_pin) - 1)):
                    output_pin_json += ","
            output_pin_json += "]"

            return {"mac" : obj.mac,
                    "nome": obj.nome,
                    "ip" : obj.ip,
                    "port" : obj.port,
                    "input_pin" : input_pin_json,
                    "output_pin" : output_pin_json}

        return json.JSONEncoder.default(self, obj)