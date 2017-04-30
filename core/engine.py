import StringIO
import httplib
import re
import select
import socket
import time
import json
import mysql.connector

from core.mysql_DAO import mysql_action_DAO, mysql_condition_DAO, mysql_database_init, mysql_event_DAO, mysql_pin_DAO, \
    mysql_shield_DAO, mysql_system_email_DAO

from mysql.connector import errorcode
from core.actions.email_notify_action import EmailNotifyAction
from core.actions.print_action import PrintAction
from core.conditions.pin_state_alteration_condition import PinStateAlterationCondition
from core.commons import EngineCommands, URIPath
import commons
from core.evento import Evento, JsonEventEncoder
from core.pin import JsonPinEncoder
from core.pin import Pin
from core.shield import JsonShieldEncoder
from core.shield import Shield
from core.util import util
from core.system_email import SystemEmail

BUFFER_SIZE = 1000000

def http_get(ip, port, request, timeout = 5):
    try:
        httpServ = httplib.HTTPConnection(ip, int(port), timeout=timeout)
        httpServ.connect()
        httpServ.request('GET', request)
        response = httpServ.getresponse()
        if response.status == httplib.OK:
            payload = response.read()
            return response.status, payload
        else:
            return response.status, ""
    except Exception as e:
        return "",""

def getArgumentLine(buf):
    # Recupero gli argomenti necessari ad eseguire il comando
    stringa = StringIO.StringIO(buf)
    stringa.readline().strip()  # la prima linea contiene il comando
    return stringa.readline()  # la seconda linea contiene gli argomenti in json

#Se il codice NON e' 200 il parametro body corrisponde al messaggio di errore
def formatResponse(response_code, body):
    return str(response_code)+"\n"+body



############ GET METHOD ##############

def getJsonSchede():
    response = formatResponse(200,json.dumps(schede.values(), cls = JsonShieldEncoder))
    return response


def getJsonScheda(mac):
    if mac in schede:
        scheda = schede[mac]
        response = formatResponse(200, json.dumps(scheda, cls=JsonShieldEncoder))
    else:
        response = formatResponse(commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_NUMBER,
                                  commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_MSG)
    return response

def getJsonPin(json_argument):
    # effettuo il parsing degli argomenti
    received_json_data = json.loads(json_argument)
    mac = received_json_data['mac']
    if mac in schede:
        scheda = schede[mac]
        pin = scheda.getPinByNumber(received_json_data['numero_pin'])
        if pin != None:
            response = formatResponse(200, json.dumps(pin, cls=JsonPinEncoder))

        else:
            response = formatResponse(commons.ErrorCode.ERROR_PIN_NOT_FOUND_NUMBER,
                                      commons.ErrorCode.ERROR_PIN_NOT_FOUND_MSG)
    else:
        response = formatResponse(commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_NUMBER,
                                  commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_MSG)
    return response

def getJsonEventi():
    response = formatResponse(200, json.dumps(eventi.values(), cls = JsonEventEncoder))
    return response

def getJsonSystemEmail():
    response = formatResponse(200, json.dumps(systemEmail.address))
    return response

########### ADD METHODS ###############

def aggiungiEvento(json_argument):
    # effettuo il parsing degli argomenti
    received_json_data = json.loads(json_argument)
    if 'mac' in received_json_data \
            and 'numero_pin' in received_json_data \
            and 'stato' in received_json_data \
            and 'condition_type' in received_json_data \
            and 'action_type' in received_json_data:
        mac = received_json_data['mac']
        if mac in schede:
            scheda = schede[mac]
            pin = scheda.getPinByNumber(received_json_data['numero_pin'])

            if pin != None:
                if received_json_data['condition_type'] == PinStateAlterationCondition.__name__:
                    id = "COND-"+util.randstring()
                    condition = PinStateAlterationCondition(id, scheda, pin, received_json_data['stato'])
                    if (received_json_data['action_type'] == PrintAction.__name__) or \
                            (received_json_data['action_type'] == EmailNotifyAction.__name__):

                        # creo l'azione associata all'evento
                        id = "ACT-" + util.randstring()

                        if received_json_data['action_type'] == PrintAction.__name__:
                            action = PrintAction(id, "e' stato attivato il pin " + pin.nome)
                        elif received_json_data['action_type'] == EmailNotifyAction.__name__:
                        #TODO: aggiundere ulteriori controlli
                            action = EmailNotifyAction(id, received_json_data['email'], "e' stato attivato il pin " + pin.nome)

                        #creo l'evento
                        id = "EV-" + util.randstring()
                        evento = Evento(id, condition, action)

                        # salvo tutto sul database
                        mysql_event_DAO.add_event(cnx, evento)
                        mysql_condition_DAO.add_condition(cnx, evento, condition)
                        mysql_action_DAO.add_action(cnx, evento, action)

                        eventi[id] = evento

                        response = formatResponse(200, "Evento "+id+" aggiunto")

                    else:
                        response = formatResponse(commons.ErrorCode.ERROR_ACTION_TYPE_NOT_RECOGNIZED_NUMBER,
                                                  commons.ErrorCode.ERROR_ACTION_TYPE_NOT_RECOGNIZED_MSG)
                else:
                    response = formatResponse(commons.ErrorCode.ERROR_CONDITION_TYPE_NOT_RECOGNIZED_NUMBER,
                                              commons.ErrorCode.ERROR_CONDITION_TYPE_NOT_RECOGNIZED_MSG)
            else:
                response = formatResponse(commons.ErrorCode.ERROR_PIN_NOT_FOUND_NUMBER,
                                          commons.ErrorCode.ERROR_PIN_NOT_FOUND_MSG)
        else:
            response = formatResponse(commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_NUMBER,
                                      commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_MSG)
    else:
        response = formatResponse(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                  commons.ErrorCode.ERROR_INVALID_BODY_MSG)
    return response

def aggiungiScheda(json_argument):
    received_json_data = json.loads(json_argument)
    ip = received_json_data['ip_shield']
    port = received_json_data['port_shield']

    # recupero il MAC address della scheda che si vuole aggiungere
    status, response = http_get(ip, port, URIPath.URI_MAC)
    print status
    if response is not "":
        mac = response.strip()

        # verifico che la risposta contenga effettivamente un MAC address
        if re.match(commons.REG_EXP_MAC_ADDRESS, mac.lower()):
            current_shield = Shield(mac, "nuova", ip, port)

            output_pin_list = []
            input_pin_list = []

            # recupero i pin di output
            status, response = http_get(ip, port, URIPath.URI_OUTPUT_PIN)
            if response is not "":
                output_pin = json.loads(response)
                for pin in output_pin:
                    current_pin = Pin(pin, "O", "PIN" + str(pin), "NO", "HL", None)
                    output_pin_list.append(current_pin)

                # recupero i pin di input
                status, response = http_get(ip, port, URIPath.URI_INPUT_PIN)
                if response is not "":
                    input_pin = json.loads(response)
                    for pin in input_pin:
                        current_pin = Pin(pin, "I", "PIN" + str(pin), "NO", None, "NL")
                        input_pin_list.append(current_pin)

                    # inserisco gli array di pin in Shield
                    current_shield.input_pin = input_pin_list
                    current_shield.output_pin = output_pin_list
                    schede[current_shield.mac] = current_shield

                    try:
                        mysql_shield_DAO.add_shield(cnx, current_shield)
                        mysql_pin_DAO.add_all_pin(cnx, current_shield, current_shield.output_pin)
                        mysql_pin_DAO.add_all_pin(cnx, current_shield, current_shield.input_pin)
                        schede[current_shield.mac] = current_shield
                        response = formatResponse(200, "Comando eseguito")
                    except mysql.connector.IntegrityError as e:
                        response = formatResponse(commons.ErrorCode.ERROR_SHIELD_ALREADY_EXIST_NUMBER,
                                                  commons.ErrorCode.ERROR_SHIELD_ALREADY_EXIST_MSG)

                else:
                    response = formatResponse(commons.ErrorCode.ERROR_SHIELD_COMMUNICATION_NUMBER,
                                              commons.ErrorCode.ERROR_SHIELD_COMMUNICATION_MSG)
            else:
                response = formatResponse(commons.ErrorCode.ERROR_SHIELD_COMMUNICATION_NUMBER,
                                          commons.ErrorCode.ERROR_SHIELD_COMMUNICATION_MSG)
        else:
            response = formatResponse(commons.ErrorCode.ERROR_INVALID_MAC_NUMBER,
                                      commons.ErrorCode.ERROR_INVALID_MAC_MSG)
    else:
        response = formatResponse(commons.ErrorCode.ERROR_SHIELD_COMMUNICATION_NUMBER,
                                  commons.ErrorCode.ERROR_SHIELD_COMMUNICATION_MSG)
    return response

def aggiungiSystemEmail(json_argument):
    if not systemEmail.isSet():
        received_json_data = json.loads(json_argument)
        if 'address' in received_json_data and 'password' in received_json_data:
            address = received_json_data['address']
            password = received_json_data['password']

            systemEmail.address = address
            systemEmail.password = password

            #aggiungo la nuova email
            mysql_system_email_DAO.add_system_email(cnx, systemEmail)

            response = formatResponse(200, "System Email aggiunta con successo")
        else:
            response = formatResponse(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                      commons.ErrorCode.ERROR_INVALID_BODY_MSG)
    else:
        response = formatResponse(commons.ErrorCode.ERROR_SYSTEM_EMAIL_ALREADY_EXISTS_NUMBER,
                                  commons.ErrorCode.ERROR_SYSTEM_EMAIL_ALREADY_EXISTS_MSG)
    return response
########## MODIFY METHODS ##############

def modificaPin(json_argument):
    # effettuo il parsing degli argomenti
    received_json_data = json.loads(json_argument)
    if 'mac' in received_json_data and 'numero_pin' in received_json_data:
        mac = received_json_data['mac']
        if mac in schede:
            scheda = schede[mac]
            pin = scheda.getPinByNumber(received_json_data['numero_pin'])
            if pin != None:
                if 'usato' in received_json_data:
                    pin.usato = received_json_data['usato']
                if 'nome' in received_json_data:
                    pin.nome = received_json_data['nome']
                if 'out_mode' in received_json_data:
                    pin.out_mode = received_json_data['out_mode']
                if 'in_mode' in received_json_data:
                    pin.in_mode = received_json_data['in_mode']

                # Salvo le modifiche sul database
                mysql_pin_DAO.modify_pin(cnx, scheda, pin)

                response = formatResponse(200, "Comando eseguito")

            else:
                response = formatResponse(commons.ErrorCode.ERROR_PIN_NOT_FOUND_NUMBER,
                                          commons.ErrorCode.ERROR_PIN_NOT_FOUND_MSG)
        else:
            response = formatResponse(commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_NUMBER,
                                      commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_MSG)
    else:
        response = formatResponse(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                  commons.ErrorCode.ERROR_INVALID_BODY_MSG)
    return response

def modificaScheda(json_argument):
    # effettuo il parsing degli argomenti
    received_json_data = json.loads(json_argument)
    if 'mac' in received_json_data:
        mac = received_json_data['mac']
        if mac in schede:
            scheda = schede[mac]

            if 'nome' in received_json_data:
                scheda.nome = received_json_data['nome']
                # Salvo le modifiche sul database
                mysql_shield_DAO.modify_shield(cnx, scheda)

            response = formatResponse(200, "Comando eseguito")

        else:
            response = formatResponse(commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_NUMBER,
                                      commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_MSG)
    else:
        response = formatResponse(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                  commons.ErrorCode.ERROR_INVALID_BODY_MSG)
    return response


######### SET METHODS ##################

def setStatoPin(json_argument):
    # effettuo il parsing degli argomenti
    received_json_data = json.loads(json_argument)
    mac = received_json_data['mac']
    if mac in schede:
        scheda = schede[mac]
        pin = scheda.getPinByNumber(received_json_data['numero_pin'])
        if pin != None and pin.tipo == "O":  # posso settare solo se il pin e' di output
            stato = int(received_json_data['stato'])

            # SET 1 o 0
            if stato == 0 or stato == 1:
                status, response = http_get(scheda.ip, scheda.port,
                                            URIPath.URI_SET_STATUS + "?PIN" + str(pin.numero) + "=" + str(stato))
                if response != "":
                    response = formatResponse(200, "Comando eseguito")
                else:
                    response = formatResponse(commons.ErrorCode.ERROR_SHIELD_COMMUNICATION_NUMBER,
                                              commons.ErrorCode.ERROR_SHIELD_COMMUNICATION_MSG)
            # TOGGLE
            elif stato == 2:
                status, response = http_get(scheda.ip, scheda.port,
                                            URIPath.URI_TOGGLE)  # TODO: modificare il path
                if response != "":
                    response = formatResponse(200, "Comando eseguito")

                else:
                    response = formatResponse(commons.ErrorCode.ERROR_SHIELD_COMMUNICATION_NUMBER,
                                              commons.ErrorCode.ERROR_SHIELD_COMMUNICATION_MSG)
            else:
                response = formatResponse(commons.ErrorCode.ERROR_INVALID_BODY_NUMBER,
                                          commons.ErrorCode.ERROR_INVALID_BODY_MSG)
        else:
            response = formatResponse(commons.ErrorCode.ERROR_PIN_NOT_FOUND_NUMBER,
                                      commons.ErrorCode.ERROR_PIN_NOT_FOUND_MSG)
    else:
        response = formatResponse(commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_NUMBER,
                                  commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_MSG)
    return response


########## DELETE METHODS ###############

def eliminaScheda(mac):
    try:
        scheda = schede[mac]
        mysql_shield_DAO.drop_shield(cnx, scheda)
        del schede[mac]
        response = formatResponse(200, "Scheda rimossa")
    except KeyError:
        response = formatResponse(commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_NUMBER,
                                  commons.ErrorCode.ERROR_SHIELD_NOT_FOUND_MSG)
    return response

def eliminaEvento(id):
    try:
        evento = eventi[id]
        mysql_event_DAO.drop_event(cnx, evento)
        del eventi[id]
        response = formatResponse(200, "Evento rimosso")
    except KeyError:
        response = formatResponse(commons.ErrorCode.ERROR_EVENT_NOT_FOUND_NUMBER,
                                  commons.ErrorCode.ERROR_EVENT_NOT_FOUND_MSG)
    return response

def eliminaSystemEmail():
    mysql_system_email_DAO.drop_system_email(cnx, systemEmail)
    systemEmail.address = None
    systemEmail.password = None
    response = formatResponse(200, "System Email rimossa")
    return response


def eseguiAzione(buf):

    # AZIONE: AGGIUNGI SCHEDA
    if EngineCommands.COMMAND_ADD_SHIELD in buf:
        json_argument = getArgumentLine(buf)
        response = aggiungiScheda(json_argument)


    # AZIONE: RECUPERA INFORMAZIONI SCHEDE
    elif EngineCommands.COMMAND_GET_INFO_SHIELDS in buf:
        response = getJsonSchede()

    # AZIONE: RECUPERA INFORMAZIONI SCHEDE
    elif EngineCommands.COMMAND_GET_INFO_EVENTS in buf:
        response = getJsonEventi()

    # AZIONE: ELIMINA SCHEDA
    elif EngineCommands.COMMAND_DELETE_SHIELD in buf:
        mac = getArgumentLine(buf)
        response = eliminaScheda(mac)

    # AZIONE: ELIMINA EVENTO
    elif EngineCommands.COMMAND_DELETE_EVENT in buf:
        id = getArgumentLine(buf)
        response = eliminaEvento(id)

    # AZIONE: MODIFICA PIN
    elif EngineCommands.COMMAND_MODIFY_PIN in buf:
        json_argument = getArgumentLine(buf)
        response = modificaPin(json_argument)


    #AZIONE: AGGIUNGI EVENTO
    elif EngineCommands.COMMAND_ADD_EVENT in buf:
        json_argument = getArgumentLine(buf)
        response = aggiungiEvento(json_argument)


    # AZIONE: MODIFICA SCHEDA
    elif EngineCommands.COMMAND_MODIFY_SHIELD in buf:
        json_argument = getArgumentLine(buf)
        response = modificaScheda(json_argument)


    # AZIONE: RESTITUISCE LE INFORMAZIONI DELLA SCHEDA
    elif EngineCommands.COMMAND_GET_SHIELD in buf:
        mac = getArgumentLine(buf)
        response = getJsonScheda(mac)


    # AZIONE: SETTA STATO PIN OUTPUT
    elif EngineCommands.COMMAND_SET_PIN_STATE in buf:
        json_argument = getArgumentLine(buf)
        response = setStatoPin(json_argument)


    # AZIONE: GET INFORMAZIONI PIN
    elif EngineCommands.COMMAND_GET_PIN in buf:
        json_argument = getArgumentLine(buf)
        response = getJsonPin(json_argument)

    # AZIONE: GET EMAIL DI SISTEMA
    elif EngineCommands.COMMAND_GET_SYSTEM_EMAIL in buf:
        response = getJsonSystemEmail()

    #AZIONE: AGGIUNGI EMAIL DI SISTEMA
    elif EngineCommands.COMMAND_ADD_SYSTEM_EMAIL in buf:
        json_argument = getArgumentLine(buf)
        response = aggiungiSystemEmail(json_argument)

    #AZIONE: ELIMINA EMAIL DI SISTEMA
    elif EngineCommands.COMMAND_DELETE_SYSTEM_EMAIL in buf:
        response = eliminaSystemEmail()

    #comando non riconosciuto
    else:
        response = formatResponse(commons.ErrorCode.ERROR_COMMAND_NOT_RECOGNIZED_NUMBER,
                                  commons.ErrorCode.ERROR_COMMAND_NOT_RECOGNIZED_MSG)

    return response

def carica_dati_salvati():
    list_shield = mysql_shield_DAO.get_all_shield(cnx)
    for shield in list_shield:
        list_pins = mysql_pin_DAO.get_pins_by_mac_shield(cnx, shield)
        for pin in list_pins:
            if pin.tipo == "O":
                shield.output_pin.append(pin)
            else:
                shield.input_pin.append(pin)
        schede[shield.mac] = shield

    # carico tutti gli eventi registrati
    list_events = mysql_event_DAO.get_all_events(cnx)
    for event in list_events:
        condition = mysql_condition_DAO.get_condition_by_event_id(cnx, event)
        if isinstance(condition, PinStateAlterationCondition):
            # attualmente condition.shield contiene il mac address
            condition.shield = schede[condition.shield]
            condition.pin = condition.shield.getPinByNumber(condition.pin)
        event.condition = condition

        action = mysql_action_DAO.get_action_by_event_id(cnx, event)
        event.action = action

        eventi[event.id] = event

    #carico la mail di sistema usata per inviare notifiche
    email = mysql_system_email_DAO.get_system_email(cnx)
    systemEmail.address = email.address
    systemEmail.password = email.password

def aggiorna_stato_schede():
    for shield in schede.itervalues():
        status, response = http_get(shield.ip, shield.port, URIPath.URI_INPUT_STATUS, timeout=1)
        if response is not "":
            input_status = json.loads(response)
            for pin, stato in zip(shield.input_pin, input_status):
                pin.stato = stato

            time.sleep(0.1)

            status, response = http_get(shield.ip, shield.port, URIPath.URI_OUTPUT_STATUS, 1)
            if response is not "":
                output_status = json.loads(response)
                for pin, stato in zip(shield.output_pin, output_status):
                    pin.stato = stato
            else:
                print "Impossibile comunicare con la scheda: "+shield.mac
        else:
            print "Impossibile comunicare con la scheda: " + shield.mac



################################################## MAIN ####################################

cose = {}
schede = {}
config_dict = {}
eventi = {}
systemEmail = SystemEmail(None, None)

# leggo i valori dal file di configurazione
try:
    with open("config.conf") as myfile:
        for line in myfile:
            name, var = line.partition("=")[::2]
            config_dict[name.strip()] = str(var).strip()
except IOError as e:
    print "Impossibile aprire il file di configurazione"
    exit(1)
except Exception as e:
    print "Controllare che il file di configurazone rispetti la giusta sintassi nome = valore"
    exit(1)

#stabilisco la connessione al database
try:
    cnx = mysql.connector.connect(user=config_dict['user'], password=config_dict['password'], host='127.0.0.1', database=config_dict['db_name'])
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
    exit(1)
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    cnx = mysql.connector.connect(user=config_dict['user'], password=config_dict['password'], host='127.0.0.1')
    mysql_database_init.create_database(cnx.cursor(), config_dict['db_name'])
    print "Database creato con successo"
    cnx.database = config_dict['db_name']
    mysql_database_init.create_table_shields(cnx.cursor())
    print "Tabella shields creata con successo"
    mysql_database_init.create_table_pins(cnx.cursor())
    print "Tabella pins creata con successo"
    mysql_database_init.create_table_events(cnx.cursor())
    print "Tabella events creata con successo"
    mysql_database_init.create_table_conditions(cnx.cursor())
    print "Tabella conditions creata con successo"
    mysql_database_init.create_table_actions(cnx.cursor())
    print "Tabella actions creata con successo"
    mysql_database_init.create_table_system_email(cnx.cursor())
    print "Tabella systememail creata con successo"

  else:
    print(err)
    exit(1)

carica_dati_salvati()


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(1) # become a server socket, maximum 1 connections
serversocket.setblocking(0)

while True:
    print "verifico qualcosa"

    #mi collego alle schede per recuperare lo stato dei pin
    aggiorna_stato_schede()

    #verifico la condizione ed eseguo l'azione associata per ogni evento registrato
    for evento in eventi.keys():
        eventi[evento].checkAndExecute()
        #aggiorno il last_execution_time permanentemente
        mysql_event_DAO.modify_event(cnx, eventi[evento])

    time.sleep(0.5)

    ready_to_read, ready_to_write, in_error = select.select([serversocket], [], [], 1)
    if ready_to_read :
        connection, address = serversocket.accept()

        #la socket e' aperta solo per i processi residenti sulla stessa macchina
        if(address[0] == "127.0.0.1"):
            buf = connection.recv(BUFFER_SIZE)
            if len(buf) > 0:
                response = eseguiAzione(buf)
                connection.send(response)

                '''
                try:
                    response = eseguiAzione(buf)
                except Exception as e:
                    response = "Errore generico: "+ e.message
                connection.send(response)
                '''
        else:
            connection.close()


