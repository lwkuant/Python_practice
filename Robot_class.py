class Robot(object):

    def __init__(self, speed):
        self.speed = speed

    def operate(self, work_load):
        print "It needs %f hour(s) to finish the work." %(work_load/float(self.speed))


class Robot1(Robot):

    pass

class Robot2(Robot):

    def __init__(self, speed, battery_time):
        Robot.__init__(self, speed)
        self.battery_time = battery_time

    def remained_battery(self, work_hours):
        print "The remained battery time is %f." %(self.battery_time-float(work_hours*0.35))
        
    
