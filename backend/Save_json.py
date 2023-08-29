import Json


class Save:

    def __init__(self):

        self.data = None

    def save(self):
        with open('Json/Value.json', 'r') as laod:

