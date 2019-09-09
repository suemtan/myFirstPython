from Car_Class import Car


class ElectricCar(Car):

    def __init__(self, make, model, year):
        # initialize an electric car
        Car.__init__(self, make,model,year)
        #super(ElectricCar, self).__init__(make, model, year)
        # battery capacity in KWH
        self.battery_size = 70
        # charge level in %
        self.charge_level = 0

    def charge(self):
        # fully charge
        self.charge_level = 100
        print "This vehicle is fully charged"


# create instance of electric car
my_newcar = ElectricCar('Tesla', 'model S', 2016)

print "*****My New Car Information*****"
my_newcar.charge()
my_newcar.drive()
