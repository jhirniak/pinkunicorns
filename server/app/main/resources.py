from flask.ext import restful


class Analyse(restful.Resource):
    def get(self):
        return 'hello'
