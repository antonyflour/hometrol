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

SELECT_ACTION_BY_EVENT_ID = "SELECT * FROM actions WHERE event = %s"


def add_action(cnx, event, action):
    if isinstance(action, PrintAction):
        action_tupla = (action.id, event.id, PrintAction.__name__, None, None, None, None, action.msg)
    cnx.cursor().execute(ADD_ACTION, action_tupla)
    cnx.commit()

def modify_action(cnx, event, action):
    if isinstance(action, PrintAction):
        action_tupla = (action.id, event.id, PrintAction.__name__, None, None, None, None, action.msg, action.id)
    cnx.cursor().execute(MODIFY_ACTION, action_tupla)
    cnx.commit()


def get_action_by_event_id(cnx, event):
    cursor = cnx.cursor()
    cursor.execute(SELECT_ACTION_BY_EVENT_ID, (event.id,))
    list_actions = []
    for (id, event, type, mac_shield, pin_number, state, email, msg) in cursor:
        if type == PrintAction.__name__:
            current_pin = PrintAction(id, msg)
        list_actions.append(current_pin)
    return list_actions[0]