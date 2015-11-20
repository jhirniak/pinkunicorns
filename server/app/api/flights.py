import pickle

from amadeus.amadeus import Flights

class InspiredFlights:
    def __init__(self):
        self.flights = Flights('s0XN9NBwpcEGmc9cL0NpSKs9rh5FRIpV')

    def where_can_i_fly(self, origin, budget):
        resp = self.flights.inspiration_search(
            origin=origin,
            departure_date="2015-11-20--2015-11-22",
            max_price=budget)

        with open('acodes.pickle', 'rb') as fh:
            resp['acodes'] = pickle.load(fh)

        return resp


if __name__ == '__main__':
    flights = InspiredFlights()
    print flights.where_can_i_fly('SFO', 300)