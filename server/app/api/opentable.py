from requests import get

API_URL = 'http://opentable.herokuapp.com/api/'


def get_restaurants(city, address, zip, country=None):
    params = {
        'address': address,
        'country': country or 'US',
    }

    if city:
        params['city'] = city

    if zip:
        params['zip'] = zip

    response = get(API_URL + 'restaurant', params=params)

    return response.json().restaurants
