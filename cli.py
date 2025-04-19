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
        return (lambda rand: (self.data[rand], rand))(randint(1, len(self.data) - 1))

    def exercice(self):
        print(
            "mettre une virgule et un espace entre chaque mot (et les mettre dans l'ordre)"
        )
        while len(self.data) > 1:
            to_guess, line = self.choose_line()
            which = randint(0, len(to_guess) - 1)
            print(f"Quel sont les autres formes de {to_guess[which]} ?")
            answer = input().split(", ")
            answer = answer[0:which] + to_guess[which] + answer[which:]
            if answer == to_guess:
                print("C'est bon")
                del self.data[line]
                self.found += to_guess


if __name__ == "__main__":
    a = exo(path="./vocabulary/csv/allemand/verbes-forts.csv")
