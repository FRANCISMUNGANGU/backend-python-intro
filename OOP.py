class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def sound_produced(self):
        print("I don't know who I am")


class Cat(Pet):
    def __init__(self, name, age, color, sound):
        super().__init__(name, age, color)
        self.sound = sound
    def sound_produced(self):
        print(f"My name is {self.name} and my age is {self.age} and im {self.color}. I say {self.sound}")

class Dog(Pet):
    def __init__(self, name, age, color, sound):
        super().__init__(name, age, color)
        self.sound = sound
    def sound_produced(self):
        print(f"My name is {self.name} and my age is {self.age} and im {self.color}. I say {self.sound}")
class Fish(Pet):
    pass



pet1 = Cat("Tim", 13, "brown", "meow")
pet2 = Dog("Billy", 14, "orange", "bark")
pet3 = Fish("Drown", 2, "Gold")
pet1.sound_produced()
pet2.sound_produced()
pet3.sound_produced()