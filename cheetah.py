class Cheetah:
    needed_money = 60

    def __init__(self, name, gander, age):
        self.name = name
        self.gender = gander
        self.age = age

    @staticmethod
    def get_needs():
        return Cheetah.needed_money

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"