import json


class Load:

    def __init__(self):

        self.data = None

    @staticmethod
    def load():

        with open('backend/Json/Value.Json', 'r') as load:
            loadding = json.load(load)

            return loadding



