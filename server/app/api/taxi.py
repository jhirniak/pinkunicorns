import requests


class Uber:
    def __init__(self):
        self.access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsicmVxdWVzdCJdLCJzdWIiOiJmNTA1NTc0Zi1lM2IxLTQwMWQtOGY0My1jOTZmNDczMTJkY2EiLCJpc3MiOiJ1YmVyLXVzMSIsImp0aSI6ImQ1OTliMDNiLWMzNjMtNGY0ZS1hYjAxLWRiYjIyMTdkYjY3NiIsImV4cCI6MTQ1MDU5MDI5MiwiaWF0IjoxNDQ3OTk4MjkyLCJ1YWN0IjoiallKMkcxektSZ3l5RHZHa3pHT0huQVFPTnc2bDZIIiwibmJmIjoxNDQ3OTk4MjAyLCJhdWQiOiJvaGtaOHJzcUtHOE1xTHhEZFBKSm5Vb09QenFXZjgwTCJ9.GN7QAGCPBISv2Y56M-SJsce7z5oB_IP8Kv2DWItJOy_MsMFQIrZ8B8zadBlvXDXRfX4gw7XsxJGjj_ORN9QLSnVmOAbHHz2YYmwdVucLGpnvX_TXznx_0phZWr56V9hHCpTddnu6eFca6dUnvhI2YZjHS2DAN0j24Fri6bTD7jV2eVUMQ3VgfbBRICLax_L8w8u4en6VhKXuLsQy1cGwXoap6BFuNpqIzF8LjuMF11Ez2-BYouFUajvvVfcTPJC3YuUwMVeL7afy2ENk9G9GtFUVyYxdE0cprs5cYtbM6xqE4N_lGsseyYXZHH1cbgKwr5ySlUjxAhPgf3BHYjxTGw'

    def get_products(self, lat, lng):
        url = 'https://api.uber.com/v1/products'

        parameters = {
            'server_token': 'I6P26-c3RWNlzWHykbtuNb2tCMEHuEnjaz8W9NMB',
            'latitude': lat,
            'longitude': lng,
        }

        response = requests.get(url, params=parameters)

        data = response.json()

        return [x['product_id'] for x in data['products'] if x['display_name'] == 'uberX']

    def book_taxi(self, lat, lng, end_lat, end_lng):
        url = 'https://sandbox-api.uber.com/v1/requests'
        product_id = self.get_products(lat, lng)[0]

        parameters = {
            'start_latitude': lat,
            'start_longitude': lng,
            'end_latitude': end_lat,
            'end_longitude': end_lng,
            'product_id': product_id
        }

        response = requests.post(url, headers={
            'Authorization': 'Bearer %s' % self.access_token,
            'Content-Type': 'application/json'
        }, json=parameters)

        data = response.json()

        return data

    def update_booking(self, request_id):
        url = 'https://sandbox-api.uber.com/v1/sandbox/requests/' + request_id

        parameters = {
            'status': 'accepted'
        }

        response = requests.put(url, headers={
            'Authorization': 'Bearer %s' % self.access_token,
        }, json=parameters)

        return response

    def get_estimate(self, lat, lng, end_lat, end_lng):
        url = 'https://api.uber.com/v1/estimates/price'

        parameters = {
            'start_latitude': lat,
            'start_longitude': lng,
            'end_latitude': end_lat,
            'end_longitude': end_lng,
        }

        response = requests.get(url, headers={
            'Authorization': 'Bearer %s' % self.access_token,
        }, data=parameters)

        data = response.json()

        for i in range(0, len(data['prices'])):
            data['prices'][i]['duration'] /= 60
            data['prices'][i]['duration'] = str(data['prices'][i]['duration']) + 'min'
            data['prices'][i]['low_estimate'] = str(data['prices'][i]['low_estimate'])

        return data


if __name__ == '__main__':
    u = Uber()
    print u.get_estimate(37.7833, -122.4167, 37.8833,-122.5167)
