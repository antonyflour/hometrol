from condition import ConditionInterface
from pin_state_alteration_condition import PinStateAlterationCondition

ADD_CONDITION = "INSERT INTO conditions " \
          "(id, event, mac_shield, pin_number, expected_state) " \
          "values (%s, %s, %s, %s, %s)"

MODIFY_CONDITION = "UPDATE conditions SET " \
             "id = %s, " \
             "event = %s, " \
             "mac_shield = %s, " \
             "pin_number = %s " \
             "expected_state = %s " \
             "WHERE id = %s"

def add_condition(cnx, event, condition):
    if isinstance(condition, PinStateAlterationCondition):
        condition_tupla = (condition.id, event.id, condition.shield.mac, condition.pin.numero, condition.expected_state)
    cnx.cursor().execute(ADD_CONDITION, condition_tupla)
    cnx.commit()

def modify_event(cnx, event, condition):
    if isinstance(condition, PinStateAlterationCondition):
        condition_tupla = (condition.id, event.id, condition.shield.mac, condition.pin.numero, condition.expected_state, condition.id)
    cnx.cursor().execute(MODIFY_CONDITION, condition_tupla)
    cnx.commit()