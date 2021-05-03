class Tiger:
    needed_money = 45

    def __init__(self, name, gander, age):
        self.name = name
        self.gender = gander
        self.age = age

    @staticmethod
    def get_needs():
        return Tiger.needed_money

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"