# To read and modify the csv databases
#


class Data:
    def __init__(self, path, *args) -> None:
        self.path = path
        if not args:
            with open(self.path, "r", encoding="utf-8") as file:
                self.data = [i.split(",") for i in file.read().split("\n")]
                del self.data[-1]
                self.titles = self.data[0]
                self.data = [i.split(",") for i in file.read().split("\n")][:-1]
        else:
            pass


if __name__ == "__main__":
    print(Data("./vocabulary/csv/allemand/t.csv").data)
