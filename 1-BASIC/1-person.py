class Person:
    """Class Person"""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hi, I'm {self.name}"

juan = Person("Juan", 15, "M")
print(juan.greet())
print(juan.age)
print(juan.gender)
