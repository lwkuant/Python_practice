import math

class shape(object):
    def __init__(self):
        print("call __init__ from shape class")
    
    def calaulate_area(self):
        print("calling calculate_area() from shape class")
        return 0
        
class circle(shape):
    def __init__(self, r):
        print("call __init__ from circle class")
        self.r = r 
    
    def calculate_area(self):
        print("calling calculate_area from circle class")
        return math.pi * math.pow(self.r, 2)                                            
    
class rectangle(shape):
    def __init__(self, l, w):
        print('call __init__ from rectangle class')
        self.l = l
        self.w = w
        
    def calculate_area(self):
        print('calling calculate_area() from rectangle class')
        return self.l * self.w
                                                        