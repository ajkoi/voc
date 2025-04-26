import csv_database as csv
from random import randint
from time import time


class exo:
    def __init__(self, **kwargs):
        if "path" in kwargs.keys():
            self.data = csv.Data(kwargs["path"])
            self.not_found = self.data.data
            self.found = []
        else:
            pass

    def choose_line(self):
        return (lambda rand: (self.not_found[rand], rand))(
            randint(1, len(self.not_found) - 1)
        )

    def exercice(self):
        print(
            "Mettre une virgule et un espace entre chaque mot (et les mettre dans l'ordre) les ß"
        )
        time_start = time()
        while len(self.data.data) > 1:
            to_guess, line = self.choose_line()
            which = randint(0, len(to_guess) - 1)
            print(f"Quel sont les autres formes de {to_guess[which]} ?")
            answer = input().split(", ")
            answer = answer[0:which] + [to_guess[which]] + answer[which:]
            if answer == to_guess:
                print("C'est bon")
                del self.not_found[line]
                self.found += to_guess
            else:
                print(f"Faux, la réponse était {to_guess}\nTu as mis {answer}")
        print(f"Tu as fini, tu as trouvé en {round(time() - time_start, 1)} secondes.")


if __name__ == "__main__":
    a = exo(path="./vocabulary/csv/allemand/verbes-forts.csv")
    a.exercice()
