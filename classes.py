class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hello, my name is {self.name} and i can talk 😀')


person1 = Person('AFANA'.upper())
person1.talk()
