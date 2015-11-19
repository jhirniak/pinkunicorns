from flask.ext import restful
from flask_restful import reqparse
from app.nlp.nlp import NLP

class Analyse(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text')
        args = parser.parse_args()
        nlp = NLP()

        return nlp.get_categories(args['text'])
