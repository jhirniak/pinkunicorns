import facebook


class Facebook:
    def __init__(self, access_token):
        self.graph = facebook.GraphAPI(access_token=access_token)

    def get_likes(self, name):
        friends = self.graph.get_connections(id='me', connection_name='friends')['data']
        print friends
        for friend in friends:
            if friend['name'] == name:
                friend_id = friend['id']
                likes = self.graph.get_connections(id=friend_id, connection_name='likes')['data']

                return [x['name'] for x in likes]


if __name__ == '__main__':
    f = Facebook(
        'CAAGyweZCX3VUBANuYII15rall8Qg4mhjibqu8euyup8e68Wail44pWM8sGyEhgvkmhqJYZBJ4ZBTYs58CcP3vfAMM6U3LXYl2wJvbxwLZA6mAeQl2WQAcZC8kzkFbDfF5rQsCB0ppspRug4sVHX4o9N8wAZAwv7bUxBh8i0JNFP1sZAO5cHKPKfWDGZA0FVOWHepwn4XZCh29LOuw6OATZAGhu')
    f.get_likes('Konrad Martins')
