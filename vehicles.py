class Vehicle:
    def __init__(self, wheels, speed):
        self.wheels = wheels
        self.speed = speed
    
modelX= Vehicle(4, 5)
print("The number of wheels are", modelX.wheels)
print("The speed of the vehicle is", modelX.speed)