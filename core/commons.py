
REG_EXP_MAC_ADDRESS = "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$"


class EngineCommands:
    COMMAND_ADD_SHIELD = "addShield"
    COMMAND_GET_INFO_SHIELDS= "getShields"
    COMMAND_DELETE_SHIELD = "deleteShield"
    COMMAND_MODIFY_PIN = "modifyPin"
    COMMAND_GET_SHIELD = "getShield"
    COMMAND_GET_PIN = "getPin"
    COMMAND_SET_PIN_STATE = "setPinState"
    COMMAND_MODIFY_SHIELD = "modifyShield"
    COMMAND_ADD_EVENT = "addEvent"
    COMMAND_GET_INFO_EVENTS = "getEvents"
    COMMAND_DELETE_EVENT = "deleteEvent"
    COMMAND_GET_SYSTEM_EMAIL = "getSystemEmail"
    COMMAND_ADD_SYSTEM_EMAIL = "addSystemEmail"
    COMMAND_DELETE_SYSTEM_EMAIL = "deleteSystemEmail"

class URIPath:

    URI_MAC = "/arduino_emulate/mac.php"
    URI_OUTPUT_PIN = "/arduino_emulate/output_pin.php"
    URI_INPUT_PIN = "/arduino_emulate/input_pin.php"
    URI_INPUT_STATUS ="/arduino_emulate/input_status.php"
    URI_OUTPUT_STATUS ="/arduino_emulate/output_status.php"
    URI_SET_STATUS ="/arduino_emulate/set_out.php"
    URI_TOGGLE = "/arduino_emulate/toggle.php"


    '''
    URI_MAC = "/mac"
    URI_OUTPUT_PIN = "/output_pin"
    URI_INPUT_PIN = "/input_pin"
    URI_INPUT_STATUS = "/input_status"
    URI_OUTPUT_STATUS = "/output_status"
    URI_SET_STATUS = "/setout"
    URI_TOGGLE = "/toggle"
    '''


class ErrorCode:
    ERROR_NOT_FOUND_NUMBER = 404
    ERROR_NOT_FOUND_MSG = "Not found"

    ERROR_INVALID_BODY_NUMBER = 901
    ERROR_INVALID_BODY_MSG = "Invalid body"

    ERROR_INVALID_CONTENT_TYPE_NUMBER = 902
    ERROR_INVALID_CONTENT_TYPE_MSG = "Invalid content-type : only application/json is supported"

    ERROR_INVALID_MAC_NUMBER = 903
    ERROR_INVALID_MAC_MSG = "Invalid MAC Address"

    ERROR_INVALID_MAC_PIN_NUMBER = 904
    ERROR_INVALID_MAC_PIN_MSG = "Invalid MAC Address or Pin Number"

    ERROR_PIN_NOT_FOUND_NUMBER = 905
    ERROR_PIN_NOT_FOUND_MSG = "Pin not found"

    ERROR_SHIELD_NOT_FOUND_NUMBER = 905
    ERROR_SHIELD_NOT_FOUND_MSG = "Shield not found"

    ERROR_SHIELD_COMMUNICATION_NUMBER = 906
    ERROR_SHIELD_COMMUNICATION_MSG = "Impossible to connect to the shield"

    ERROR_SHIELD_ALREADY_EXIST_NUMBER = 907
    ERROR_SHIELD_ALREADY_EXIST_MSG = "The shield already exist"

    ERROR_GENERIC_NUMBER = 908
    ERROR_GENERIC_MSG = "Generic Error"

    ERROR_COMMAND_NOT_RECOGNIZED_NUMBER = 909
    ERROR_COMMAND_NOT_RECOGNIZED_MSG = "Command not recognized"

    ERROR_CONDITION_TYPE_NOT_RECOGNIZED_NUMBER = 910
    ERROR_CONDITION_TYPE_NOT_RECOGNIZED_MSG = "Condition type not recognized"

    ERROR_ACTION_TYPE_NOT_RECOGNIZED_NUMBER = 911
    ERROR_ACTION_TYPE_NOT_RECOGNIZED_MSG = "Action type not recognized"

    ERROR_EVENT_NOT_FOUND_NUMBER = 912
    ERROR_EVENT_NOT_FOUND_MSG = "Event not found"

    ERROR_SYSTEM_EMAIL_ALREADY_EXISTS_NUMBER = 913
    ERROR_SYSTEM_EMAIL_ALREADY_EXISTS_MSG = "System email already exists, please first remove the old one"