class Car(object):
    def __init__(self, name='General', model='GM', vehicle_type=None):
        self.name = name
        self.model = model
        self.vehicle_type = vehicle_type
        self.speed = speed

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.vehicle_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def is_saloon(self):
        if self.vehicle_type is not 'trailer':
            return True
        return False

    def drive(self, moving_speed):
        if moving_speed == 3:
            Car.speed = 1000
        elif moving_speed == 7:
            Car.speed = 77

        return self
