from blockClass import blockClass

class wordClass:
    def __init__(self,height, width):
        self.height = height
        self.width = width
        self.map = list()

        for i in range(self.height):
            temp = list()
            for j in range(self.width):
                temp.append(blockClass("land"))
            self.map.append(temp)

    def __str__(self):
        if self.map == "Not set":
            return "Map not set"     
        return "\n".join( [ ", ".join([str(j) for j in i]) for i in self.map ])
