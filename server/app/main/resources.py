from flask.ext import restful
from flask_restful import reqparse
from app.nlp.nlp import NLP
from app.api.social import Facebook
from app.api.shopping import Amazon
# from app.api.gcal import GCal
import json
from app.api.jarvis import *
from app.api.rome_to_rio import *
from app.api.accomodation import AirBnB
from app.api.taxi import Uber
from app.api.opentable import *
from app.api.flights import InspiredFlights
import os.path
from app.api.rentals import CarRental


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


class Analyse(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text')
        args = parser.parse_args()

        nlp = NLP()

        data = {}

        data['category'] = nlp.get_categories(args['text'])
        data['keywords'] = nlp.get_keywords(args['text'])

        return data


class GoogleCalendar(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('query')
        args = parser.parse_args()
        query = json.loads(args['query'])
        response = []
        for q in query:
            response.append({"id": q['id'], "html": "<div>Hello " + q['id'] + "</div>"})

        return json.dumps(response)


class RunTask(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('category')
        parser.add_argument('text')
        args = parser.parse_args()

        if args['category'] == 'shopping':
            facebook = Facebook(
                'CAAGyweZCX3VUBAFUgJTDxFBVCUG1vux1mF5j1BfTUUGWTDqnc0VzRPn1hg0ZCtmv1S9StPpi5iSF4GGqD4YsMVA3f0oEf3YRG7hLDXSPxx0OvTI5ZA9MbiUCjlHy7lBa83kjZAVO52Py1u6nQFIyZBxwn2P86ITYYjaK2D0tAraFdqG8csbuoLDMUPef3eN9bDVJXX78s7JEXB82WBpa7')
            likes = facebook.get_likes(args['text'])
            print likes
            amazon = Amazon()

            products = {}

            for like in likes:
                items = amazon.search_for(like)
                if len(items) == 2:
                    products[like] = items[1]

            return products


class Jarvis(restful.Resource):
    def __init__(self):
        self.cache = {}

        self.load_cache()
        self.load_codes()

    def save_cache(self):
        f = open('cache.json', 'w+')
        f.write(json.dumps(self.cache))
        f.close()

    def load_cache(self):
        if os.path.exists('cache.json'):
            f = open('cache.json')
            self.cache = json.loads(f.read())
            f.close()
        else:
            self.cache = {}

    def load_codes(self):
        import json

        if os.path.exists('acodes.json'):
            with open('acodes.json') as fh:
                self.codes = json.load(fh)
        else:
            self.codes = {}

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text')
        parser.add_argument('access_token')
        args = parser.parse_args()

        if args['text'].lower() in self.cache:
            return self.cache[args['text'].lower()]

        data = parse(args['text'])

        response = {}

        if data['intent'] == 'birthdays':
            facebook = Facebook(args['access_token'])
            likes = facebook.get_likes(data['entities']['contact'][0]['value'])

            amazon = Amazon()

            products = {}

            for like in likes:
                items = amazon.search_for(like)
                products[like] = items
                print items

            response = {
                'products': products,
                'name': data['entities']['contact'][0]['value'],
            }



        elif data['intent'] == 'travel':
            response = {'travel': {}}

            try:
                rome2rio = get_rome_rio('Menlo Park', data['entities']['location'][0]['value'])
            except:
                print "Error"
                return {'error': True};
            response['travel']['plan'] = rome2rio[0][0]
            response['travel']['places'] = rome2rio[1]

            pos = rome2rio[1][1]['pos'].split(',')
            start = rome2rio[1][0]['pos'].split(',')


            if response['travel']['plan']['distance'] > 200:
                airbnb = AirBnB()
                response['accomodation'] = airbnb.get_accomodation(pos[0], pos[1])

                cars = CarRental()
                response['rental'] = cars.get_cars(start[0], start[1])
            else:
                uber = Uber()


                response['taxi'] = uber.get_estimate(start[0], start[1], pos[0], pos[1])





        elif data['intent'] == 'restaurant_booking':
            response = {}
            try:
                response['restaurants'] = get_restaurants(data['entities'], None, None, None)
            except:
                print "Error"
                return {'error': True};


        elif data['intent'] == 'flights':
            response = {}
            flights = InspiredFlights()

            response['flights'] = flights.where_can_i_fly(data['entities']['location'][0]['value'],
                                                          data['entities']['amount_of_money'][0]['value'])


        response['type'] = data['intent']
        response['codes'] = self.codes

        import json
        # TODO

        self.cache[args['text'].lower()] = response
        self.save_cache()
        return response
