from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and price > self.__budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, work_name):
        worker = [w for w in self.workers if w.name == work_name]
        if worker:
            self.workers.remove(worker[0])
            return f"{work_name} fired successfully"
        return "There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_sum = 0
        for worker in self.workers:
            total_sum += worker.salary
        if total_sum <= self.__budget:
            self.__budget -= total_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_sum = 0
        for animal in self.animals:
            total_sum += animal.get_needs()
        if total_sum <= self.__budget:
            self.__budget -= total_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetah = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        result += f"----- {len(lions)} Lions:\n"
        for l in lions:
            result += f"{l}\n"
        result += f"----- {len(tigers)} Tigers:\n"
        for t in tigers:
            result += f"{t}\n"
        result += f"----- {len(cheetah)} Cheetahs:\n"
        for c in cheetah:
            result += f"{c}\n"
        result = result.strip()
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]
        result += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            result += f"{k}\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        for c in caretakers:
            result += f"{c}\n"
        result += f"----- {len(vets)} Vets:\n"
        for v in vets:
            result += f"{v}\n"
        result = result.strip()
        return result


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())

