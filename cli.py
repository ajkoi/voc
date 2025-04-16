import csv_database as csv
from random import randint


class exo:
    def __init__(self, **kwargs):
        if "path" in kwargs.keys():
            self.data = csv.Data(kwargs["path"])
            self.found = []
        else:
            pass

    def choose_line(self):
        return self.data[randint(1, len(self.data) - 1)]

    def exercice(self):
        while len(self.data) > 1:
            self.to_guess = self.choose_line()
            self.which = randint(0, len(self.to_guess))
