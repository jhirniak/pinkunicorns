import csv
import pickle

from amadeus.amadeus import Flights

class Airport(object):

    def __init__(self, row):
        self.code = row[0]
        self.airportName = row[1]
        self.nearestCity = row[2]
        self.country = row[3]
        self.countryCode = row[4]
        self.geoloc = {
            'lat': row[5],
            'lng': row[6]
        }


class InspiredFlights:
    def __init__(self):
        self.flights = Flights('s0XN9NBwpcEGmc9cL0NpSKs9rh5FRIpV')

    def where_can_i_fly(self, origin, budget):
        resp = self.flights.inspiration_search(
            origin=origin,
            departure_date="2015-11-20--2015-11-22",
            max_price=budget)

        return resp

    def get_codes(self):
        with open('acodes.pickle') as fh:
            import pickle
            codes = pickle.load(fh)
            return codes

if __name__ == '__main__':
    flights = InspiredFlights()
    print flights.where_can_i_fly('SFO', 300)
    print flights.get_codes()