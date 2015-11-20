import wit
import json

access_token = 'VK56CWXRPOGGD75K6VXUKIW4XPNR2ENC'
wit.init()

def parse(text):
    response = json.loads(wit.text_query(text, access_token))
    if 'contact' in response['outcomes'][0]['entities']:
        for i in range(0, len(response['outcomes'][0]['entities']['contact'])):
            if str(response['outcomes'][0]['entities']['contact'][i]['value']).lower() == 'i':
                del response['outcomes'][0]['entities']['contact'][i]
                break

    print response['outcomes'][0]
    return response['outcomes'][0]

