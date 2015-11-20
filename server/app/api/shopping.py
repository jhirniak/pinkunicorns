from amazon.api import AmazonAPI


class Amazon:
    def __init__(self):
        self.amazon = AmazonAPI('AKIAJTMXQEFQVV7SEF5Q', 'CwNQ/cKQNXckNMhfb7oQ0KTmBoaJNPqSFqzKtubf',
                                'fbhackcom0d-21', region='UK')

    def search_for(self, text, top=3):
        try:
            products = self.amazon.search(Keywords=text, SearchIndex='All')

            top_products = []

            product_titles = {}

            for product in products:
                if product.title is not None and product.price_and_currency is not None:
                    title = product.title
                    # if len(title) > 50:
                    #     title = title[:50] + "..."

                    product_titles[product.offer_url] = title
                    top_products.append({
                        'offer_url': product.offer_url,
                        'name': product.title,
                        'image': product.medium_image_url,
                        'price': product.price_and_currency[0],
                        'currency': product.price_and_currency[1],
                    })
                    top -= 1
                    if top == 0:
                        break

            return top_products
        except:
            return []

if __name__ == '__main__':

    a = Amazon()
    print a.search_for('macbook')