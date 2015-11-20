from amadeus.amadeus import Flights

class InpiredFlights:
    def __init__(self):
        self.flights = Flights('s0XN9NBwpcEGmc9cL0NpSKs9rh5FRIpV')

    def where_can_i_fly(self, origin, budget):
        resp = self.flights.inspiration_search(
            origin=origin,
            departure_date="2015-11-25--2015-11-30",
            max_price=budget)

        return resp


if __name__ == '__main__':
    flights = InpiredFlights()
    print flights.where_can_i_fly('SFO', 300)