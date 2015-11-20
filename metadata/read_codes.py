#!/usr/bin/python

import csv
import json
import pickle

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


if __name__ == "__main__":
    acodes = dict()

    with open('/home/ravanave/Repos/pinkunicorns/metadata/aircodes2geo.csv', 'rb') as csvfile:
        codes = csv.reader(csvfile)

        for row in codes:
            acode = {
                'code': row[0],
                'airportName': row[1],
                'nearestCity': row[2],
                'country': row[3],
                'countryCode': row[4],
                'geoloc': {
                    'lat': row[5],
                    'lng': row[6]
                }
            }
            acodes[acode['code']] = acode


    with open('acodes.json', 'w') as fh:
        json.dump(acodes, fh)

    # print acodes['SFO'].airportName, acodes['SFO'].geoloc
