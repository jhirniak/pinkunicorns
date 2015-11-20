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
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text')
        args = parser.parse_args()

        data = parse(args['text'])

        if data['intent'] == 'birthdays':
            facebook = Facebook(
                'CAAGyweZCX3VUBADbeZBCJJjNKomgCzaKFVRQ09WQaSZCKvySnqyuqcejWULDR3wcuiAZAzb9aXX85gLHQRaK9KzrOatjez8Df4rTiHHN5TYPMWoHEn52kwbIZBGkGQTy4KflbRXjO2iQCRs5x3AIGpZCsszzNAHDIzHAcOQTtsoBnrcZC26bRx9Om1QT8ZCB5XNOz9EgBM1UrqR6usfZB8PKz')
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

            return response

        elif data['intent'] == 'travel':
            response = {'travel':{}}

            rome2rio = get_rome_rio('Menlo Park', data['entities']['location'][0]['value'])
            response['travel']['plan'] = rome2rio[0][0]
            response['travel']['places'] = rome2rio[1]

            pos = rome2rio[1][1]['pos'].split(',')


            if response['travel']['plan']['distance'] > 200:
                airbnb = AirBnB()
                response['accomodation'] = airbnb.get_accomodation(pos[0], pos[1])
            else:
                uber = Uber()

                start = rome2rio[1][0]['pos'].split(',')

                response['taxi'] = uber.get_estimate(start[0], start[1], pos[0], pos[1])



            return response
