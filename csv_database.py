# To read and modify the csv databases
#


class Data:
    def __init__(self, path, *args) -> None:
        self.path = path
        if not args:
            with open(self.path, "r", encoding="utf-8") as file:
                self.data = [i.split(",") for i in file.split("\n")]
        else:
            pass
