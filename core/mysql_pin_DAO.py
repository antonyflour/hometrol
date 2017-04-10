from pin import Pin

ADD_PIN = "INSERT INTO pins " \
          "(mac_shield, numero, tipo, nome, usato, out_mode, in_mode) " \
          "values (%s, %s, %s, %s, %s, %s, %s)"

SELECT_PIN_BY_MAC = "SELECT * FROM pins WHERE mac_shield = %s"

MODIFY_PIN = "UPDATE pins SET " \
             "tipo = %s, " \
             "nome = %s, " \
             "usato = %s, " \
             "out_mode = %s," \
             "in_mode = %s " \
             "WHERE mac_shield = %s AND numero = %s"

def add_pin(cnx, shield, pin):
    pin_tupla = (shield.mac, pin.numero, pin.tipo, pin.nome, pin.usato, pin.out_mode, pin.in_mode)
    cnx.cursor().execute(ADD_PIN, pin_tupla)
    cnx.commit()

def add_all_pin(cnx, shield, pins):
    for pin in pins:
        add_pin(cnx, shield, pin)

def get_pins_by_mac_shield(cnx, shield):
    cursor = cnx.cursor()
    cursor.execute(SELECT_PIN_BY_MAC, (shield.mac,))
    list_pins = []
    for (mac_shield, pin_number, type, name, isused, out_mode, in_mode) in cursor:
        current_pin = Pin(pin_number, type, name, isused, out_mode, in_mode)
        list_pins.append(current_pin)
    return list_pins

def modify_pin(cnx, shield, pin):
    pin_tupla = (pin.tipo, pin.nome, pin.usato, pin.out_mode, pin.in_mode, shield.mac, pin.numero)
    cnx.cursor().execute(MODIFY_PIN, pin_tupla)
    cnx.commit()