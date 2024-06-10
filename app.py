from ecommerce.joe import Person

class Student(Person):
    def __init__(self,first_name, last_name, age, address, classes):
        super().__init__(first_name, last_name, age)
        self.classes = classes
        self.address = address

    def greeting(self):
        text = f' and I\'m {self.age} years old'
        print(f'Hi I\'{self.first_name} {self.last_name} , I\' student in {self.classes}, I live at {self.address}'+text)


student = Student(first_name='John', last_name='WELBECK', age=22, address='Thies, Lalane', classes='L1 INFO')

student.greeting()
