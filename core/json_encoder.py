import json
from pin_state_alteration_condition import PinStateAlterationCondition
from print_action import PrintAction
class JsonConditionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, PinStateAlterationCondition):
            return {"id" : obj.id,
                    "mac_shield": obj.shield.mac,
                    "pin_number" : obj.pin.numero,
                    "expected_state" : obj.expected_state,
                    }

        return json.JSONEncoder.default(self, obj)


class JsonActionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, PrintAction):
            return {"id" : obj.id,
                    "msg": obj.msg,
                    }

        return json.JSONEncoder.default(self, obj)