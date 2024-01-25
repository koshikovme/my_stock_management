from uuid import UUID, uuid4
from datetime import datetime, timedelta
import csv

users_filepath = "stock_management\\users.csv"
stocks_filepath = "stock_management\\stocks.csv"
items_filepath = "stock_management\\items.csv"
# a = 18.01.2024
# b = 10days
# a + b => 28.01.2024


class Stock:
    def __init__(
        self,
        stock_id: int,
        location: str,
        capacity_sq_m: float,
        owner_id: UUID,
    ):
        self.__stock_id = stock_id
        self.__location = location
        self.__capacity_sq_m = capacity_sq_m
        self.__owner_id = owner_id

    @property
    def owner_id(self):
        return self.__owner_id

    @property
    def stock_id(self):
        return self.__stock_id

    def __repr__(self):
        return f"Stock(id: {self.__stock_id}, owner_id: {self.__owner_id}, location: {self.__location}, capacity: {self.__capacity_sq_m})"


class Item:
    def __init__(
        self,
        item_id: int,
        stock_id: int,
        name: str,
        size: float,
        category: str,
        description: str,
        arrive_at: datetime,
        expiration_time: timedelta,
    ):
        self.__item_id = item_id
        self.__stock_id = stock_id
        self.__name = name
        self.__size = size
        self.__category = category
        self.__description = description
        self.__arrive_at = arrive_at
        self.__expiration_time = expiration_time

    @property
    def stock_id(self):
        return self.__stock_id

    def __repr__(self) -> str:
        return f"Item(item_id: {self.__item_id}, name: {self.__name}, description: {self.__description})"


class User:
    def __init__(self, user_id: UUID, phone: str, username: str, password: str):
        self.__user_id = user_id
        self.__phone = phone
        self.__username = username
        self.__password = password

    def __repr__(self) -> str:
        return f"User(id: {self.__user_id}, username: {self.__username}, phone: {self.__phone})"

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def user_id(self):
        return self.__user_id


class Controller:
    def __init__(self):
        self.__current_user: User = None
        self.__current_stock: Stock = None

    def signup(self):
        user_id = uuid4()
        username = input("Введите ваш ник для регистрации: ")
        password = input("Введите ваш пароль для регистрации: ")
        phone = input("Введите ваш номер телефона для регистрации: ")

        new_user = User(
            user_id=user_id,
            phone=phone,
            username=username,
            password=password,
        )
        database["users"].append(new_user)
        print("Вы успешно зарегистрировались!")

    def auth_user(self):
        while True:
            username = input("Введите ваш ник для входа: ")
            password = input("Введите ваш пароль для входа: ")

            for user in database["users"]:
                if user.username == username and user.password == password:
                    print("Вы вошли в аккаунт!")
                    self.__current_user = user
                    return
            print("Неверно введены данные!")

    def logout(self):
        pass

    def get_stock_information(self):
        if self.__current_user is None:
            print("Сначала надо войти в аккаунт")
            return

        if self.__current_stock is None:
            self.choose_stock()

        stock_id = self.__current_stock.stock_id
        stocks_items = list(
            filter(lambda item: item.stock_id == stock_id, database["items"])
        )
        for item in stocks_items:
            print(item)

    def choose_stock(self):
        if self.__current_user is None:
            print("Сначала надо войти в аккаунт")
            return
        user_id = self.__current_user.user_id
        user_stocks: list[Stock] = list(
            filter(lambda stock: stock.owner_id == user_id, database["stocks"])
        )

        while True:
            print("Выберите склад")
            for index in range(len(user_stocks)):
                print(f"{index + 1}. ID склада: {user_stocks[index].stock_id}")
            selected_stock_index = int(input("Выберите порядковый номер склада: "))

            self.__current_stock = user_stocks[selected_stock_index - 1]
            return

    def add_items_to_stock(self):
        pass

    def remove_items_in_stock(self):
        pass

    def move_item_to_diff_stock(self):
        pass

    def search_available_item(self):
        pass


database = {
    "users": [],
    "stocks": [],
    "items": [],
}

with open(users_filepath, encoding="UTF-8", mode="r") as users_file:
    users = csv.DictReader(users_file)
    types = {
        "user_id": UUID,
        "phone": str,
        "username": str,
        "password": str,
    }
    for key, type in types.items():
        field = users[key]
        try:
            field = types[key](field)
            print(field)
        except ValueError:
            print("Невалидный тип данных")
        database["users"].append(field)

with open(stocks_filepath, encoding="UTF-8", mode="r") as stocks_file:
    stocks = csv.DictReader(stocks_file)
    types = {
        "stock_id": int,
        "location": str,
        "capacity_sq_m": float,
        "owner_id": UUID,
    }
    for key, type in types.items():
        field = users[key]
        try:
            field = types[key](field)
            print(field)
        except ValueError:
            print("Невалидный тип данных")
        database["stocks"].append(field)

with open(items_filepath, encoding="UTF-8", mode="r") as items_file:
    items = csv.DictReader(items_file)
    types = {
        "item_id": int,
        "stock_id": int,
        "name": str,
        "size": float,
        "category": str,
        "description": str,
        "arrive_at": datetime.strptime(items["arrive_at"], "%d.%m.%Y"),
        "expiration_time": timedelta(days=float(items["expiration_time"])),
    }
    for key, type in types.items():
        field = users[key]
        try:
            field = types[key](field)
            print(field)
        except ValueError:
            print("Невалидный тип данных")
        database["items"].append(field)


controller = Controller()
controller.auth_user()
controller.get_stock_information()
