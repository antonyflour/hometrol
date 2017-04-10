import json

class Pin:

    def __init__(self, numero, tipo, nome, usato, out_mode, in_mode):
        self.numero = numero
        self.tipo = tipo
        self.nome = nome
        self.usato = usato
        self.out_mode = out_mode
        self.in_mode = in_mode
        self.stato = 0

class JsonPinEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Pin):
            return {"numero_pin" : obj.numero,
                    "tipo": obj.tipo,
                    "nome_pin" : obj.nome,
                    "usato" : obj.usato,
                    "out_mode" : obj.out_mode,
                    "in_mode" : obj.in_mode,
                    "stato" : obj.stato
                    }

        return json.JSONEncoder.default(self, obj)