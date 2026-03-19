from random import randint
class Car:
    def __init__(self, reg, max_of_speed):
        self.reg = reg
        self.max_of_speed = max_of_speed
        self.speed = 0
        self.distance = 0
    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_of_speed:
            self.speed = self.max_of_speed
        if self.speed < 0:
            self.speed = 0
    def drive(self, hours):
        self.distance += self.speed * hours

cars = []
for i in range(10):
    plate = "ABC-" + str(i+1)  
    max_of_speed = randint(150, 200)
    cars.append(Car(plate, max_of_speed))
while max(car.distance for car in cars) < 10000:
    for car in cars:
        car.accelerate(randint(-10, 15))
        car.drive(1)
print("Regis Number".ljust(12), "|", 
      "Max Speed".ljust(10), "|", 
      "Speed".ljust(8), "|", 
      "Distance".ljust(10))
print("-" * 50)
for car in cars:
    print(car.reg.ljust(12), "|",
          str(car.max_of_speed).ljust(10), "|",
          str(car.speed).ljust(8), "|",
          str(int(car.distance)).ljust(10))