# priklad z prezentace + foto + zkusit copilota a porovnat
class Pet:
    def __init__(self, name, sound, characteristic):
        self.name = name
        self.sound = sound
        self.characteristic = characteristic

    def sound(self):
        print(f"Sound of animal {self.characteristic}")

    def show(self):
        print(f"Name of animal {self.name}")

    def type(self):
        pass




class Dog(Pet):
    _count = 0
    def __init__(self, name, characteristic):
        super().__init__(name, characteristic)
        Dog._count += 1



dog1 = Dog("Zeryk", "Hafff")


dog1.sound()
dog1.show()