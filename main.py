import time
import os
from worldClass import wordClass
from creatureClass import creatureClass
from blockClass import blockClass

world = wordClass(10,10)

c = creatureClass(type = "unknwon creature!")
pid = os.fork()

if pid == 0:
    c.start()
else:
    time.sleep(2)
    print("????/")
    while True:
        try:
            d = creatureClass(id = str(c.id))
            print(str(d))
            time.sleep(2)
        except:
            os.wa