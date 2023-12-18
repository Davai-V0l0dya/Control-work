"""
class Cat:
    def meow(self):
        print("Мяу!")

cat = Cat()
cat.meow()
cat2 = Cat()
cat.meow()

--------------------------------------------------------
"""
"""
class Cat():
    def __int__(self, name):
        self.name = name
    def meow(self):
        print(f"{self.name}: Мяу!")

cat = Cat("Барсик")
cat2 = Cat("Мурзик")
cat.meow()
cat2.meow()
"""
"""
class Student():
    def __init__(self, full_name, age, course):
        self.full_name = full_name
        self.age = age
        self.course = course

    def info(self):
        return f"{self.full_name}, {self.age}, {self.course}"

student = Student(full_name="iv iv iv",age="23",course="5")
student.info()

print(student.info())
"""
"""
class Field:
    def __init__(self):
        self.field = [' '] * 9
    def _check(self, index):
        return self.field[index] == ' '
    def turn(self, index, symbol):
        if self._check(index):
            self.field[index] = symbol
        else:
            print("Ячейка уже занята")
    def print(self):
        print(self.field[:3])
        print(self.field[3:6])
        print(self.field[6:])
        print()

field = Field()
field.print()
field.turn(3, 'X')
field.print()
field.turn(3, '0')
field.print()
"""
from    datetime import date
class Person:
    def __init__(self, first_name, last_name, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def get_age(self):
        return (date.today() - self.birthday).days // 365.25
    def info(self):
        return f"{self.get_full_name()}: {self.get_age()} лет"

sasha = Person("Саша", "Сашин", date(1990, 12, 12))
print(sasha.info())


