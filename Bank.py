class Bank():
    CHIPS = {
        'White': 5,
        'Green': 10,
        'Blue': 25,
        'Red': 50,
        'Black': 100,
        'W_Blue': 500,
    }

    def __init__(self, starting=0):
        self.__total = starting

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, amount):
        self.__total = amount
