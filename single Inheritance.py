class vehicle:
    def start(self):
        print("vehicle has started")
class car(vehicle):
    def drive(self):
        print("car is driving")
c=car()
c.start()
c.drive()
