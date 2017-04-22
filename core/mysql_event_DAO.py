from evento import Evento

ADD_EVENT = "INSERT INTO events " \
          "(id, repetition_interval, enabled, last_exec_time) " \
          "values (%s, %s, %s, %s)"

MODIFY_EVENT = "UPDATE events SET " \
             "id = %s, " \
             "repetition_interval = %s, " \
             "enabled = %s, " \
             "last_exec_time = %s " \
             "WHERE id = %s"

def add_event(cnx, event):
    if event.enabled is True:
        enabled = 1
    else:
        enabled = 0

    if event.lastExecutionTime is None:
        date = None
    else:
        date =  event.lastExecutionTime.strftime('%Y-%m-%d %H:%M:%S')

    event_tupla = (event.id, event.repetitionInterval, enabled, date)
    cnx.cursor().execute(ADD_EVENT, event_tupla)
    cnx.commit()

def modify_event(cnx, event):
    if event.enabled is True:
        enabled = 1
    else:
        enabled = 0

    if event.lastExecutionTime is None:
        date = None
    else:
        date = event.lastExecutionTime.strftime('%Y-%m-%d %H:%M:%S')

    event_tupla = (event.id, event.repetitionInterval, enabled, date, event.id)
    cnx.cursor().execute(MODIFY_EVENT, event_tupla)
    cnx.commit()