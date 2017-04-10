import threading
import time
class Evento():

    def stampa(self):
        while 1:
            print "avviso qualcuno"
            time.sleep(1)

    def check(self):
        thread = threading.Thread(target=self.stampa)
        thread.start()



