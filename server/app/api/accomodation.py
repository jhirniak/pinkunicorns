import unirest

class AirBnB:
    def get_accomodation(self, lat, lng):
        response = unirest.get("https://zilyo.p.mashape.com/search?latitude={0}&longitude={1}&provider=airbnb".format(lat,lng),
                               headers={
                                   "X-Mashape-Key": "PZneH0HEG8msh54NEygzesVhOa7Cp1z2Vr3jsnBhXLwVXlH3pO",
                                   "Accept": "application/json"
                               })

        return response.body



if __name__ == '__main__':
    a = AirBnB()
    a.get_accomodation(52.5306438, 13.3830683)


