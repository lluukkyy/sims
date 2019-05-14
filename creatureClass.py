import uuid
import os
import time

class creatureClass:
    def __init__(self, id="None" ,type = "None"):
        if str(id) in os.listdir("creature"):
            self.load(str(id))
        else:
            self.id = uuid.uuid4()
            self.type = type
            self.time = 0
            self.save()

    def save(self):
        file = open("creature/"+str(self.id), "w+")
        file.write(self.__str__())
        file.close()

    def load(self,id):
        file = open("creature/"+id)
        self.id, self.type,self.time = file.readline().strip().split("😀")
        self.id = uuid.UUID(self.id)
        file.close()

    def __str__(self):
        result = "😀".join([str(self.id), self.type, str(self.time)])
        return result

    def start(self):
        while True:
            self.time += 1
            print("Turn", self.time)
            self.save()
            time.sleep(1)
        
        
    