from condition import ConditionInterface
from pin_state_alteration_condition import PinStateAlterationCondition

ADD_CONDITION = "INSERT INTO conditions " \
          "(id, event, type, mac_shield, pin_number, expected_state) " \
          "values (%s, %s, %s, %s, %s, %s)"

MODIFY_CONDITION = "UPDATE conditions SET " \
             "id = %s, " \
             "event = %s, " \
             "type = %s, " \
             "mac_shield = %s, " \
             "pin_number = %s " \
             "expected_state = %s " \
             "WHERE id = %s"

SELECT_CONDITION_BY_EVENT_ID = "SELECT * FROM conditions WHERE event = %s"


def add_condition(cnx, event, condition):
    if isinstance(condition, PinStateAlterationCondition):
        condition_tupla = (condition.id, event.id, PinStateAlterationCondition.__name__, condition.shield.mac, condition.pin.numero, condition.expected_state)
    cnx.cursor().execute(ADD_CONDITION, condition_tupla)
    cnx.commit()

def modify_event(cnx, event, condition):
    if isinstance(condition, PinStateAlterationCondition):
        condition_tupla = (condition.id, event.id, PinStateAlterationCondition.__name__, condition.shield.mac, condition.pin.numero, condition.expected_state, condition.id)
    cnx.cursor().execute(MODIFY_CONDITION, condition_tupla)
    cnx.commit()

def get_condition_by_event_id(cnx, event):
    cursor = cnx.cursor()
    cursor.execute(SELECT_CONDITION_BY_EVENT_ID, (event.id,))
    list_conditions = []
    for (id, event, type, mac_shield, pin_number, expected_state) in cursor:
        if type == PinStateAlterationCondition.__name__:
            #per il momento inserisco il mac shield al posto dell'oggetto Shield e il numero di pin al posto dell'oggetto Pin
            current_pin = PinStateAlterationCondition(id, mac_shield, pin_number, expected_state)
        list_conditions.append(current_pin)
    return list_conditions[0]