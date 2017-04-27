from core.shield import Shield

ADD_SHIELD = "INSERT INTO shields " \
                "(mac, nome, ip, port) " \
                "VALUES (%s, %s, %s, %s)"

DROP_SHIELD = "DELETE FROM shields WHERE mac = %s"

SELECT_ALL_SHIELD = "SELECT * FROM shields"

MODIFY_SHIELD = "UPDATE shields SET " \
                "mac = %s, " \
                "nome = %s, " \
                "ip = %s, " \
                "port = %s " \
                "WHERE mac = %s"

def add_shield(cnx, shield):
    shield_tupla = (shield.mac, shield.nome, shield.ip, shield.port)
    cnx.cursor().execute(ADD_SHIELD, shield_tupla)
    cnx.commit()

def drop_shield(cnx, shield):
    cnx.cursor().execute(DROP_SHIELD, (shield.mac,)) #se non passo una tupla si incazza
    cnx.commit()

def modify_shield(cnx, shield):
    shield_tupla = (shield.mac, shield.nome, shield.ip, shield.port, shield.mac)
    cnx.cursor().execute(MODIFY_SHIELD, shield_tupla)
    cnx.commit()

def get_all_shield(cnx):
    cursor = cnx.cursor()
    cursor.execute(SELECT_ALL_SHIELD)
    list_shield=[]
    for (mac, nome, ip, port) in cursor:
        current_shield = Shield(mac, nome, ip, port)
        list_shield.append(current_shield)
    return list_shield