# priklad z prezentace + foto + zkusit copilota a porovnat
class Pet:
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def sound(self):
        print(f"Sound of animal {self.characteristic}")

    def show(self):
        print(f"Name of animal {self.name}")

    def type(self):
        pass




class Dog(Pet):
    count = 0
    def __init__(self, name, characteristic):
        super().__init__(name, characteristic)
        Dog.count += 1

class Cat(Pet):
    def __init__(self, name, characteristic):
        super().__init__(name, characteristic)


class Parrot(Pet):
    def __init__(self, name, characteristic):
        super().__init__(name, characteristic)


class Hamster(Pet):
    def __init__(self, name, characteristic):
        super().__init__(name, characteristic)


dog1 = Dog("Zeryk", "Hafff")
cat1 = Cat("Micka", "Mnau")
parrot1 = Parrot("Karel", "Grrrrrrrh")
Hamster1 = Hamster("Pepa", "Chrrrrrrr")

dog1.sound()
dog1.show()