from requests import get

API_URL = 'http://opentable.herokuapp.com/api/'


def get_restaurants(city, address, zip, country=None):

    if city.has_key('location'):
        city = city['location'][0]['value'];

    params = {
        'country': country or 'US',
    }

    if city:
        params['city'] = city

    if city.strip() == "near me":
        params['city'] = "1 Hacker Way, Menlo Park"

    if zip:
        params['zip'] = zip

    response = get(API_URL + 'restaurants', params=params)

    return response.json()['restaurants']


if __name__ == '__main__':
    print get_restaurants('san francisco', None, None, None)
