from flask.ext import restful
from flask_restful import reqparse
from app.nlp.nlp import NLP
from app.api.social import Facebook
from app.api.shopping import Amazon


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


class RunTask(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('category')
        parser.add_argument('text')
        args = parser.parse_args()

        if args['category'] == 'shopping':
            facebook = Facebook(
                'CAAGyweZCX3VUBANuYII15rall8Qg4mhjibqu8euyup8e68Wail44pWM8sGyEhgvkmhqJYZBJ4ZBTYs58CcP3vfAMM6U3LXYl2wJvbxwLZA6mAeQl2WQAcZC8kzkFbDfF5rQsCB0ppspRug4sVHX4o9N8wAZAwv7bUxBh8i0JNFP1sZAO5cHKPKfWDGZA0FVOWHepwn4XZCh29LOuw6OATZAGhu')
            likes = facebook.get_likes(args['text'])
            print likes
            amazon = Amazon()

            products = {}

            for like in likes:
                items = amazon.search_for(like)
                if len(items) == 2:
                    products[like] = items[1]

            return products
