class robot:
    
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y 
    
    def __str__(self):
        return "robot " + self.name + ", " + "with coordinate x = " + str(self.x) + " and y = " + str(self.y)                            