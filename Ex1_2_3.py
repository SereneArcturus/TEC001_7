class Car:
    def __init__(self, reg, max_of_speed):
        self.reg = reg
        self.max_of_speed = max_of_speed
        self.speed = 0
        self.distance = 0
    def show(self):
        print("The registration number of car is:", self.reg, ",",
              self.speed, " is the car's current speed", ",",
              self.max_of_speed, "is the car's max speed", ",",
              "and the amount of distance that this car has travelled is:", self.distance)
    def accelerate(self, change):
        self.speed = max(0, min(self.speed + change, self.max_of_speed))
        print("The speed after this car has accelerated is:", self.speed)
    def drive(self, hours):
        self.distance += self.speed * hours
        print("The distance that this car has travelled is:", self.distance)

car1 = Car("ABC-123", 142)
car1.show()
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.accelerate(-200)
car1.speed = 60
car1.distance = 2000
car1.drive(1.5)