from flask.ext import restful


class PopularShows(restful.Resource):
    series_list = ['Supernatural', 'Gotham', 'Flash', 'Suits', 'Arrow']

    def get(self):
        return series_list

