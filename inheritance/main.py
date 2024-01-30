import datetime
import math


class Person:
    def __init__(self, name: str, sname: str, birthday: datetime, phone: str) -> None:
        self.name = name
        self.sname = sname
        self.birthday = birthday
        self.phone = phone


class Accountant(Person):
    pass


class Programmer(Person):
    pass


# a = Accountant("Bobik", "BOBO", datetime(year=2000, month=10, day=3), "8705 777 ")


# 1. Создайте класс "Фигура" с методами для вычисления площади и периметра.
# Затем реализуйте подклассы "Прямоугольник" и "Круг", чтобы наследовать базовый функционал и переопределить методы, специфичные для каждой фигуры.

# 2. Напишите класс "Транспортное средство" с общими характеристиками. Затем создайте подклассы "Автомобиль" и "Велосипед", унаследовав их от базового класса и добавив уникальные свойства.

# 3. Реализуйте класс "Сотрудник" с атрибутами "Имя", "Возраст" и методом "Печать информации". Создайте подклассы "Менеджер" и "Разработчик", наследующиеся от "Сотрудника", и добавьте им специфичные методы.

# 4. Создайте класс "Банковский счет" с атрибутами "Баланс" и методами "Пополнение" и "Снятие". Реализуйте подклассы "Текущий счет" и "Сберегательный счет" с дополнительными функциями.


class Figure:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Rectangle(Figure):
    def __init__(self, a: int, b: int, c: int) -> None:
        try:
            self.a = a
            self.b = b
            self.c = c
        except ValueError:
            print("Invalid values")

    def perimeter(self) -> int:
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter()
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


class Circle(Figure):
    def __init__(self, r: int) -> None:
        self.r = r

    def perimeter(self):
        return 2 * self.r * math.pi

    def area(self):
        return math.pi * (self.r) ** 2


circle = Circle(5)
p = circle.perimeter()
a = circle.area()
print(f"Perimeter: {p}, Area: {a}")
rect = Rectangle(10, 5, 2)
p2 = rect.perimeter()
a2 = rect.area()
print(f"Perimeter: {p2}, Area: {a2}")


# 2. Напишите класс "Транспортное средство" с общими характеристиками. Затем создайте подклассы "Автомобиль" и "Велосипед", унаследовав их от базового класса и добавив уникальные свойства.
class Transport:
    def __init__(self, color: str, wheels: int) -> None:
        self.color = color
        self.wheels = wheels

    def move(self):
        raise NotImplementedError


class Bicycle(Transport):
    def move(self):
        print("Bicycle is moving :)")


class Car(Transport):
    def __init__(self, color: str, wheels: int, horse_power: int) -> None:
        super().__init__(color, wheels)
        self.horse_power = horse_power

    def move(self):
        print("Car is moving :)")


car = Car("red", 4, 500)
bicycle = Bicycle("black", 2)
car.move()
print(bicycle.move())

# 3. Реализуйте класс "Сотрудник" с атрибутами "Имя", "Возраст" и методом "Печать информации". Создайте подклассы "Менеджер" и "Разработчик", наследующиеся от "Сотрудника", и добавьте им специфичные методы.


class Worker:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        raise NotImplementedError


class Developer(Worker):
    def __init__(self, name: str, age: int, id: int) -> None:
        super().__init__(name, age)
        self.stack: list[str] = []
        self.id = id

    def refactor(self):
        print("Developer is refactoring")

    def add_new(self, tech: str):
        self.stack.append(tech)

    def __repr__(self) -> str:
        return f"""Developer {self.name} is {self.age} old. His stack consists of: {self.stack}"""


class Manager(Worker):
    def __repr__(self) -> str:
        return f"Manager {self.name} is {self.age} old."

    def hire(self):
        print("Manager hired someone!")

    def fire(self):
        print("Manager fired someone!")


dev = Developer("Alim", 19, 1)
dev.add_new("Spring")
dev.add_new("Java Core")
dev.add_new("SQL and MySQL high knowledge")
print(dev)

snager = Manager("Bob", 39)
snager.fire()
snager.hire()


# 4. Создайте класс "Банковский счет" с атрибутами "Баланс" и методами "Пополнение" и "Снятие". Реализуйте подклассы "Текущий счет" и "Сберегательный счет" с дополнительными функциями.
class BankAccount:
    def __init__(self, balance: int) -> None:
        self.balance = balance

    def add(self):
        raise NotImplementedError

    def withdraw(self):
        raise NotImplementedError


class CurrentAccount(BankAccount):
    def __init__(self, balance: int) -> None:
        super().__init__(balance)
        self.credits: list[str] = []

    def get_a_loan(self, sum: int, period: int):
        self.credits.append(f"Loan taked on ${sum} on {period} year/s")

    def get_credit_history(self):
        for credit in self.credits:
            print(credit)


class SavingAccount(CurrentAccount, BankAccount):
    def add_interest(self):
        self.balance += self.balance * 0.05
        print(f"Right now {self.balance}, {self.balance * 0.05} have been added!")

    # def credits_history() -> None:
    #     for


curr = CurrentAccount(100000)
curr.get_a_loan(5000000, 10)
curr.get_credit_history()

sav = SavingAccount(100000)
sav.add_interest()


# Создайте базовый класс "Утка" с атрибутами "Имя" и методами "Крякать" и "Плавать". Реализуйте эти методы, выводя соответствующие сообщения.

# Создайте подклассы "ДикаяУтка" и "ДомашняяУтка", которые наследуются от базового класса "Утка".
#  Расширьте функциональность каждого подкласса, добавив уникальные методы, такие как "Мигрировать" для дикой утки и "ПринестиЯйцо" для домашней утки.

# Добавьте еще один подкласс "РезиноваяУтка", который также наследуется от базового класса "Утка". Реализуйте метод "Прыгать", который выводит сообщение о прыжке резиновой утки.

# Создайте объекты для каждого из подклассов и вызовите их методы,


class Duck:
    def __init__(self, name: str) -> None:
        self.name = name

    def quack(self):
        print(f"{self.name} is quacking")

    def swim(self):
        print(f"{self.name} is swimming")


class WildDuck(Duck):
    def migrate(self, where_migrate: str):
        print(f"{self.name} migrated to {where_migrate}")


class HomeDuck(Duck):
    def bring_egg(self):
        print(f"{self.name} brought egg")


class RubberDuck(Duck):
    def jump(self):
        print(f"{self.name} jumped")


wild = WildDuck("Tarzan")
wild.migrate("Africa")

rub = RubberDuck("Bob")
rub.jump()
rub.quack()


# Создать класс-родитель Database, child-классы SQLDatabase, MongoDatabase, NeoDatabase.
#  У родителя будут методы connect, get_row_by_id(id: int), get_all. Каждый child должен иметь свою реализацию методов get_row_by_id, get_all


class Database:
    def __init__(self) -> None:
        self.database: list[Developer] = [
            Developer("Bobik", 38, 1),
            Developer("Robert", 19, 2),
            Developer("Adam", 23, 3),
        ]

    def get_row_by_id(id: int):
        raise NotImplementedError

    def get_all(id: int):
        raise NotImplementedError


class Mongo(Database):
    def __init__(self, nested_collections: int) -> None:
        super().__init__()
        self.nested_collections = nested_collections

    def get_row_by_id(self, id: int):
        print(f"I tooked {self.database[id]} using using embedded query")

    def get_all(self):
        print(f"I tooked data using using embedded query: {self.database}")


class SQLDatabase(Database):
    def get_row_by_id(self, id: int):
        print(f"I tooked {self.database[id]} using using SQL query")

    def get_all(self, id: int):
        print(f"I tooked data using using SQL query: {self.database}")


class NeoDatabase(Database):
    def get_row_by_id(self, id: int):
        print(f"I tooked {self.database[id]} using using neo-query")

    def get_all(self):
        print(f"I tooked data using using neo-query: {self.database}")


mongo = Mongo(5)
mongo.get_all()
mongo.get_row_by_id(2)

neo = NeoDatabase()
neo.get_all
