# dopsat dle prezentace a porovnat, + foto, zkusit napsat bez instancí, bude se to
# poodbat funkcnimu programovani

import pickle

class IntegerListManager:
    def __init__(self, filename="data.pkl"):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, "wb") as file:
            pickle.dump(data, file)

    def load_data(self):
        with open(self.filename, "rb") as file:
            return pickle.load(file)

