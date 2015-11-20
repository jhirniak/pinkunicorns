from alchemyapi import AlchemyAPI


class NLP:
    def __init__(self):
        self.alchemyapi = AlchemyAPI()

    def get_categories(self, text):
        response = self.alchemyapi.taxonomy('text', text)

        if response['status'] == 'OK' and len(response['taxonomy']) > 0:
            taxonomy = response['taxonomy'][0]
            tokens = taxonomy['label'].split('/')
            return tokens[1]

    def get_keywords(self, text):
        response = self.alchemyapi.keywords('text', text)

        if response['status'] == 'OK' and len(response['keywords']) > 0:
            return [x['text'] for x in response['keywords']]
