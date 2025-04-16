# To read and modify the csv databases
# 

class Data:
    def __init__(self, path, *args) -> None:
        self.path = path
        with open(self.path, "r", encoding="utf-8") as file:
            self.data = file.split("\n").split(",")
            
