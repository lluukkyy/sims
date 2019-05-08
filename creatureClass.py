import uuid
import os

class creatureClass:
    def __init__(self, id="None" ,type = "None"):
        if str(id) in os.listdir("creature"):
            self.load(str(id))
        else:
            self.id = uuid.uuid4()
            self.type = type
            self.save()
        
    def save(self):
        file = open("creature/"+str(self.id),"w+")
        file.write(self.__str__())
        file.close()

    def load(self,id):
        file = open("creature/"+id,"r")
        self.id, self.type = file.readline().strip().split(" ")
        self.id = uuid.UUID(self.id)
        file.close()

    def __str__(self):
        result = " ".join([str(self.id), self.type])
        return result

    def start(self):
        pass
        
    