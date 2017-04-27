from core.evento import Evento

ADD_EVENT = "INSERT INTO events " \
          "(id, repetition_interval, enabled, last_exec_time) " \
          "values (%s, %s, %s, %s)"

MODIFY_EVENT = "UPDATE events SET " \
             "id = %s, " \
             "repetition_interval = %s, " \
             "enabled = %s, " \
             "last_exec_time = %s " \
             "WHERE id = %s"

SELECT_ALL_EVENTS = "SELECT * FROM events"

DROP_EVENT = "DELETE FROM events WHERE id = %s"


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

def get_all_events(cnx):
    cursor = cnx.cursor()
    cursor.execute(SELECT_ALL_EVENTS)
    list_events=[]
    for (id, repetition_interval, enabled, last_exec_time) in cursor:
        current_event = Evento(id, None, None, repetitionInterval=repetition_interval)

        if int(enabled) == 1:
            current_event.enabled = True
        else:
            current_event.enabled = False

        if last_exec_time!= None:
            current_event.lastExecutionTime = last_exec_time#datetime.datetime.strptime('%Y-%m-%d %H:%M:%S', last_exec_time)
        list_events.append(current_event)
    return list_events

def drop_event(cnx, event):
    cnx.cursor().execute(DROP_EVENT, (event.id,))  # se non passo una tupla si incazza
    cnx.commit()