class Car(object):
    def __init__(self, carid, carname, size):
        self .carid = carid
        self. carname = carname
        self. size = size

    def __str__(self):
        return 'carid = %d, carname = %s, sise = %d' % (self.carid, self.carname, self.size)


class Cars(object):
    def __init__(self, cars=[], last=1):
        self.cars = cars
        self.last = last

    def __getitem__(self, carid):
        for car in self.cars:
            if car.carid == carid:
                return car
        raise Exception("Product with pid={} doesn't exist!".format(carid))

    def add(self, car):
        self.cars.append(car)
        self.last += 1

    def delete(self, carid):
        ind = -1
        for index, car in enumerate(self.cars):
            if car.carid == carid:
                ind = index
            if ind > -1:
                self.cars.pop(ind)

    def find(self, n):
        for car in self.cars:
            if n == car.size:
                return car.carname
            else:
                return ''

    def exist(self, carid):
        for car in self.cars:
            if carid == car.carid:
                return True
        return False

    def empty(self):
        return not self.cars

    def __str__(self):
        return '\n '.join(str(car) for car in self.cars)
