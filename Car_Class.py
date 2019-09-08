class Car():

    def __init__(self, make, model, year):
        #initialize car attributes
        self.make = make
        self.model = model
        self.year = year

        #fuel level and capacity in gallons
        self.fuel_cap = 20
        self.fuel_level = 0

    def fill_tank(self):
        #fill gas to capacity
        self.fuel_level = self.fuel_cap
        print "Fuel tank is full."

    def drive(self):
        #simulate driving
        print "The car is moving."

    def display_carinfo(self):

        print self.make
        print self.model
        print self.year

my_car = Car('Honda', '98', 2018)

#print attribute values functions from car class
print "***** My Car Information ***** "
my_car.display_carinfo()
my_car.fill_tank()
my_car.drive()

my_old_car = Car('Ford', 'Escape', '2002')

#print attribute values functions from my old car class
print "\n***** My Old Car Information *****  "
my_old_car.display_carinfo()
my_old_car.fill_tank()
my_old_car.drive()

