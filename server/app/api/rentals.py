from amadeus.amadeus import Cars


class CarRental:

    def __init__(self):
        self.cars = Cars('s0XN9NBwpcEGmc9cL0NpSKs9rh5FRIpV')

    def get_cars(self, lat, lng):
        resp = self.cars.search_circle(
        pick_up='2015-11-25',
        drop_off='2015-11-30',
        latitude=lat,
        longitude=lng,
        radius=70,
        currency='USD',
        lang='EN')

        return resp



if __name__ == '__main__':
    cars = CarRental()

    print cars.get_cars(35.07057, -114.58937)