#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

#README - An application to manage vehicles demo

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
        
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed
        
class Cars(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Cars")
        
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype
        
    def drive(self, speed):
            super().drive(speed)
            print("Driving my ", self.enginetype, " car at a speed of ", self.speed )
        
class Motorcycles(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycles")
        
        if(hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.door = 0
        self.enginetype = enginetype
        
    def drive(self, speed):
            super().drive(speed)
            print("Driving my ", self.enginetype, " motorcycle at a speed of ", self.speed )
        
car1 = Cars("gas")
car2 = Cars("electric")
motor = Motorcycles("gas", True)

print(car1.wheels)
print(car2.enginetype)
print(motor.wheels)

car1.drive(30)
car1.drive(40)
motor.drive(50)
