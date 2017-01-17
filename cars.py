# A car class that can be used to instantiate various vehicles.
# It takes in arguments that depict the type, model, and name of the vehicle, provided they are set.
class Car(object):
# defined function that differentiates vehicles according to their specs.
	def __init__(self, name='General', generation='Sixth' ,car_type='lexus' ):
        self.car_type = car_type
        self.generation = generation
        self.name = name
        self.speed = 0

        if name== 'Harrie' or name== 'Avensis':
            self.num_of_cylinders = 6
        else:
            self.num_of_doors = 4

        if car_type == 'saloon':
            self.horse_power = 200
        else:
            self.horse_power = 450

# A fuction that seperates saloon cars from trailers using boolean values.
	def is_saloon(self):
        if self.car_type ==  'trailer':
            return False
        else:
            return True





























