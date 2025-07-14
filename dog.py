class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


    def __str__(self):
        return f'This is a {self.age} year old {self.breed} named {self.name}'
    
