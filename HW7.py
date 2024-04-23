# 2

class Car:
    color = ""
    speed = 0

    def upSpeed(self,value) :
    
        self.speed += value

# 4

class Horse:
    speed = 0

    def __init__(self) :
        self.speed = 50
        
#6 / Answer: 3

class Car:
    def method(slef):
        print("슈퍼 클래스")

class Sedan(Car) :
    def method(self):
        print("서브 클래스")

myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()

#7
class Car:
    speed = 0

    def upspeed(self,value) :
        self.speed = self.speed + value

class RVCar(Car):
    seatNum = 0

    def getSeatNum(self) :
        return self.seatNum
