from googlemaps import Client

def getGeocode(location):
	c = Client("AIzaSyAGfQB9o_UWdN6NNn9L0jv_6ppXgW4W-uo")
	return c.geocode(location)[0]["geometry"]["location"]