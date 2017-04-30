from core.system_email import SystemEmail

ADD_SYSTEM_EMAIL = "INSERT INTO systememail " \
                "(email, password) " \
                "VALUES (%s, %s)"

DROP_SYSTEM_EMAIL = "DELETE FROM systememail WHERE email = %s"

SELECT_SYSTEM_EMAIL = "SELECT * FROM systememail"

MODIFY_SYSTEM_EMAIL = "UPDATE systememail SET " \
                "email = %s, " \
                "password = %s, " \
                "WHERE email = %s"

def add_system_email(cnx, systemEmail):
    email_tupla = (systemEmail.address, systemEmail.password)
    cnx.cursor().execute(ADD_SYSTEM_EMAIL, email_tupla)
    cnx.commit()

def drop_system_email(cnx, systemEmail):
    cnx.cursor().execute(DROP_SYSTEM_EMAIL, (systemEmail.address,)) #se non passo una tupla si incazza
    cnx.commit()

def modify_system_email(cnx, systemEmail):
    tupla = (systemEmail.address, systemEmail.password, systemEmail.address)
    cnx.cursor().execute(MODIFY_SYSTEM_EMAIL, tupla)
    cnx.commit()

def get_system_email(cnx):
    cursor = cnx.cursor()
    cursor.execute(SELECT_SYSTEM_EMAIL)
    data = cursor.fetchone()
    if data == None:
        return SystemEmail(None, None)
    else:
        return SystemEmail(data[0], data[1])
