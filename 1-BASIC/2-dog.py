class Dog:
    """Class Dog"""
    def __init__(self, name, breed, age) -> None:
        self.name = name
        self.breed = breed
        self.age = age

    def info(self):
        """Info method"""
        return "{}, {}, {}".format(self.name, self.breed, self.age)
  
    def bark(self):
        """Bark method"""
        return "Woof woof"

firulais = Dog("Firulais", "Golden Retriever", "7 meses")
print(firulais.info())
print(firulais.bark())

duque = Dog("Duque", "Lazi", "1 año")
print(duque.info())
print(duque.bark())