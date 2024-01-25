import csv
from uuid import UUID
from datetime import datetime
from datetime import timedelta

users_filepath = "./users.csv"
stocks_filepath = "./stocks.csv"
items_filepath = "./items.csv"

with open(users_filepath, encoding="UTF-8", mode="r") as users_file:
    users = csv.DictReader(users_file)
    types = {
        "user_id": UUID,
        "phone": str,
        "username": str,
        "password": str,
    }
    for key, type in types:
        field = users[key]
        try:
            field = types[key](field)
            print(field)
        except ValueError:
            print("Невалидный тип данных")

with open(stocks_filepath, encoding="UTF-8", mode="r") as stocks_file:
    stocks = csv.DictReader(stocks_file)
    types = {
        "stock_id": int,
        "location": str,
        "capacity_sq_m": float,
        "owner_id": UUID,
    }
    for key, type in types:
        field = users[key]
        try:
            field = types[key](field)
            print(field)
        except ValueError:
            print("Невалидный тип данных")

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
    for key, type in types:
        field = users[key]
        try:
            field = types[key](field)
            print(field)
        except ValueError:
            print("Невалидный тип данных")
