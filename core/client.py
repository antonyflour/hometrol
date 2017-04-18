import StringIO
import cgi
import json
import re
import socket
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

import commons
from commons import EngineCommands
from util.json_util import is_json

PORT_NUMBER = 8080
BUFFER_SIZE = 1000000
# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):

        #ottieni informazioni su tutte le schede
        if re.match("/shields$", self.path):
            buf = self.send_to_engine(EngineCommands.COMMAND_GET_INFO_SHIELDS, "")

            self.send_response(200)
            self.send_headers()
            self.end_headers()
            #   Send the html message
            self.wfile.write(buf)

        #ottieni informazioni su un pin
        elif re.match("/shield/.+/pin/.+", self.path):
            mac_address = self.path.split('/')[-3]
            numero_pin = self.path.split('/')[-1]
            if re.match(commons.REG_EXP_MAC_ADDRESS, mac_address.lower()) and re.match("[0-9]+$", numero_pin):
                payload = {}
                payload['mac'] = mac_address
                payload['numero_pin'] = numero_pin
                payload = json.dumps(payload)

                buf = self.send_to_engine(EngineCommands.COMMAND_GET_PIN, payload)
                code, body = self.parseResponse(buf)
                print buf

                if code == 200:
                    self.send_response(200)
                    self.send_headers()
                    self.send_payload(body)
                else:
                    self.send_response(code, body)
                    self.send_headers()
            else:
                self.send_response(commons.ErrorCode.ERROR_INVALID_MAC_PIN_NUMBER,
                                   commons.ErrorCode.ERROR_INVALID_MAC_PIN_MSG)
                self.send_headers()

        #ottini informazioni su una scheda
        elif re.match("/shield/.+", self.path):
            mac_address = self.path.split('/')[-1]  # prendo l'ultimo token
            if re.match(commons.REG_EXP_MAC_ADDRESS, mac_address.lower()):
                # invio comando e argomenti
                buf = self.send_to_engine(EngineCommands.COMMAND_GET_SHIELD, mac_address)
                code, body = self.parseResponse(buf)
                print buf

                if code == 200:
                    self.send_response(200)
                    self.send_headers()
                    self.send_payload(body)
                else:
                    self.send_response(code, body)
                    self.send_headers()
            else:
                self.send_response(commons.ErrorCode.ERROR_INVALID_MAC_NUMBER,
                                   commons.ErrorCode.ERROR_INVALID_MAC_MSG)
                self.send_headers()

        else:
            self.send_response(commons.ErrorCode.ERROR_NOT_FOUND_NUMBER,
                               commons.ErrorCode.ERROR_NOT_FOUND_MSG)
            self.send_headers()

        return

    def do_POST(self):

        #modifica stato pin
        if re.match("/shield/.+/pin/.+/state", self.path):
            mac_address = self.path.split('/')[-4]  # prendo l'ultimo token
            numero_pin = self.path.split('/')[-2]

            if re.match(commons.REG_EXP_MAC_ADDRESS, mac_address.lower()) and re.match("[0-9]+$", numero_pin):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'application/json':
                    length = int(self.headers.getheader('content-length'))
                    payload = self.rfile.read(length).decode("utf-8")

                    if is_json(payload):
                        #inserisco mac e numero pin come argomenti
                        payload = json.loads(payload)
                        if 'stato' in payload and re.match("[0-9]+$", payload['stato']):
                            payload['mac'] = mac_address
                            payload['numero_pin'] = numero_pin
                            payload = json.dumps(payload)

                            buf = self.send_to_engine(EngineCommands.COMMAND_SET_PIN_STATE, payload)
                            print buf

                            code, body = self.parseResponse(buf)
                            if code == 200:
                                self.send_response(200)
                                self.send_headers()
                                self.send_payload(body)
                            else:
                                self.send_response(code, body)
                                self.send_headers()
                        else:
                            self.send_response(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                               commons.ErrorCode.ERROR_INVALID_BODY_MSG)
                            self.send_headers()
                    else:
                        self.send_response(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                           commons.ErrorCode.ERROR_INVALID_BODY_MSG)
                        self.send_headers()
                else:
                    self.send_response(commons.ErrorCode.ERROR_INVALID_CONTENT_TYPE_NUMBER,
                                       commons.ErrorCode.ERROR_INVALID_CONTENT_TYPE_MSG)
                    self.send_headers()
            else:
                self.send_response(commons.ErrorCode.ERROR_INVALID_MAC_PIN_NUMBER,
                                   commons.ErrorCode.ERROR_INVALID_MAC_PIN_MSG)
                self.send_headers()

        #modifica informazioni del pin
        elif re.match("/shield/.+/pin/.+", self.path):
            mac_address = self.path.split('/')[-3]
            numero_pin = self.path.split('/')[-1]

            if re.match(commons.REG_EXP_MAC_ADDRESS, mac_address.lower()) and re.match("[0-9]+$", numero_pin):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'application/json':
                    length = int(self.headers.getheader('content-length'))
                    payload = self.rfile.read(length).decode("utf-8")

                    if is_json(payload):
                        #inserisco mac e numero pin come argomenti
                        payload = json.loads(payload)
                        payload['mac'] = mac_address
                        payload['numero_pin'] = numero_pin
                        payload = json.dumps(payload)

                        buf = self.send_to_engine(EngineCommands.COMMAND_MODIFY_PIN, payload)
                        print buf

                        code, body = self.parseResponse(buf)
                        if code == 200:
                            self.send_response(200)
                            self.send_headers()
                            self.send_payload(body)
                        else:
                            self.send_response(code, body)
                            self.send_headers()
                    else:
                        self.send_response(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                           commons.ErrorCode.ERROR_INVALID_BODY_MSG)
                        self.send_headers()
                else:
                    self.send_response(commons.ErrorCode.ERROR_INVALID_CONTENT_TYPE_NUMBER,
                                       commons.ErrorCode.ERROR_INVALID_CONTENT_TYPE_MSG)
                    self.send_headers()
            else:
                self.send_response(commons.ErrorCode.ERROR_INVALID_MAC_PIN_NUMBER,
                                   commons.ErrorCode.ERROR_INVALID_MAC_PIN_MSG)
                self.send_headers()

        # modifica informazioni scheda (supportata solo la modifica del nome)
        elif re.match("/shield/.+", self.path):
            mac_address = self.path.split('/')[-1]

            if re.match(commons.REG_EXP_MAC_ADDRESS, mac_address.lower()):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'application/json':
                    length = int(self.headers.getheader('content-length'))
                    payload = self.rfile.read(length).decode("utf-8")

                    if is_json(payload):
                        # inserisco mac e numero pin come argomenti
                        payload = json.loads(payload)
                        payload['mac'] = mac_address
                        payload = json.dumps(payload)

                        buf = self.send_to_engine(EngineCommands.COMMAND_MODIFY_SHIELD, payload)
                        print buf

                        code, body = self.parseResponse(buf)
                        if code == 200:
                            self.send_response(200)
                            self.send_headers()
                            self.send_payload(body)
                        else:
                            self.send_response(code, body)
                            self.send_headers()
                    else:
                        self.send_response(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                           commons.ErrorCode.ERROR_INVALID_BODY_MSG)
                        self.send_headers()
                else:
                    self.send_response(commons.ErrorCode.ERROR_INVALID_CONTENT_TYPE_NUMBER,
                                       commons.ErrorCode.ERROR_INVALID_CONTENT_TYPE_MSG)
                    self.send_headers()
            else:
                self.send_response(commons.ErrorCode.ERROR_INVALID_MAC_NUMBER,
                                   commons.ErrorCode.ERROR_INVALID_MAC_MSG)
                self.send_headers()

        # aggiungi una nuova scheda remota
        elif re.match("/shield$", self.path):
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'application/json':
                length = int(self.headers.getheader('content-length'))
                payload = self.rfile.read(length).decode("utf-8")
                if is_json(payload):
                    payload = json.loads(payload)
                    if 'ip_shield' in payload and 'port_shield' in payload:
                        payload = json.dumps(payload)
                        buf = self.send_to_engine(EngineCommands.COMMAND_ADD_SHIELD, payload)
                        print buf

                        code, body = self.parseResponse(buf)
                        if code == 200:
                            self.send_response(200)
                            self.send_headers()
                            self.send_payload(body)
                        else:
                            self.send_response(code, body)
                            self.send_headers()

                    else:
                        self.send_response(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                           commons.ErrorCode.ERROR_INVALID_BODY_MSG)
                        self.send_headers()
                else:
                    self.send_response(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                       commons.ErrorCode.ERROR_INVALID_BODY_MSG)
                    self.send_headers()

        else:
            self.send_response(commons.ErrorCode.ERROR_NOT_FOUND_NUMBER,
                               commons.ErrorCode.ERROR_NOT_FOUND_MSG)
            self.send_headers()

        return


    def do_DELETE(self):

        #elimina una scheda
        if re.match("/shield/.+", self.path):
            mac_address = self.path.split('/')[-1]    #prendo l'ultimo token
            if re.match(commons.REG_EXP_MAC_ADDRESS, mac_address.lower()):
                # invio comando e argomenti
                buf = self.send_to_engine(EngineCommands.COMMAND_DELETE_SHIELD, mac_address)

                code, body = self.parseResponse(buf)
                if code == 200:
                    self.send_response(200)
                    self.send_headers()
                    self.send_payload(body)
                else:
                    self.send_response(code, body)
                    self.send_headers()
            else:
                self.send_response(commons.ErrorCode.ERROR_INVALID_MAC_NUMBER,
                                   commons.ErrorCode.ERROR_INVALID_MAC_MSG)
                self.send_headers()

        else:
            self.send_response(commons.ErrorCode.ERROR_NOT_FOUND_NUMBER,
                               commons.ErrorCode.ERROR_NOT_FOUND_MSG)
            self.send_headers()

        return

    def do_PUT(self):

        # aggiungi un nuovo evento
        if re.match("/events", self.path):
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'application/json':
                length = int(self.headers.getheader('content-length'))
                payload = self.rfile.read(length).decode("utf-8")

                if is_json(payload):

                    buf = self.send_to_engine(EngineCommands.COMMAND_ADD_EVENT, payload)
                    print buf

                    code, body = self.parseResponse(buf)
                    if code == 200:
                        self.send_response(200)
                        self.send_headers()
                        self.send_payload(body)
                    else:
                        self.send_response(code, body)
                        self.send_headers()
                else:
                    self.send_response(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                       commons.ErrorCode.ERROR_INVALID_BODY_MSG)
                    self.send_headers()
            else:
                self.send_response(commons.ErrorCode.ERROR_INVALID_CONTENT_TYPE_NUMBER,
                                   commons.ErrorCode.ERROR_INVALID_CONTENT_TYPE_MSG)
                self.send_headers()

        return

    def send_headers(self):
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def send_payload(self, payload):
        self.wfile.write(payload)

    def send_to_engine(self, command, arguments):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('localhost', 8089))
        clientsocket.send(command + "\n" + arguments)
        buf = clientsocket.recv(BUFFER_SIZE)
        return buf

    def parseResponse(self, response):
        stringa = StringIO.StringIO(response)
        code = stringa.readline().strip()  # la prima linea contiene il codice
        msg = stringa.readline()    # la seconda linea contiene il body o il messaggio
        return int(code), msg

''' MAIN'''
try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    # Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()


