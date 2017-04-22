from action import ActionInterface
from print_action import PrintAction

ADD_ACTION = "INSERT INTO actions " \
          "(id, event, type, mac_shield, pin_number, state, email, msg) " \
          "values (%s, %s, %s, %s, %s, %s, %s, %s)"

MODIFY_ACTION = "UPDATE actions SET " \
             "id = %s, " \
             "event = %s, " \
             "type = %s, " \
             "mac_shield = %s, " \
             "pin_number = %s " \
             "state = %s " \
             "email = %s " \
             "msg = %s " \
             "WHERE id = %s"

def add_action(cnx, event, action):
    if isinstance(action, PrintAction):
        action_tupla = (action.id, event.id, "PrintAction", None, None, None, None, action.msg)
    cnx.cursor().execute(ADD_ACTION, action_tupla)
    cnx.commit()

def modify_event(cnx, event, action):
    if isinstance(action, PrintAction):
        action_tupla = (action.id, event.id, "PrintAction", None, None, None, None, action.msg, action.id)
    cnx.cursor().execute(MODIFY_ACTION, action_tupla)
    cnx.commit()