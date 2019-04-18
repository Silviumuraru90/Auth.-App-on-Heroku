import requests, random, string, json


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

headers = {"Content-Type": "application/json"}


class Post_api():
    @staticmethod
    def posting(thing):

    payload = {
    "price": thing['Price'],
    "store_id": thing['Id']
    }

    requests.post("https://ecnaoptriha.herokuapp.com/item/{}".format(id_generator()), data=json.dumps(payload), headers=headers)
