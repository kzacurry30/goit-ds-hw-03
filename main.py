import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi

# Підключення до MongoDB
client = MongoClient(
    "mongodb+srv://kolyaput34:08012003@cluster1.01m4r.mongodb.net/)", server_api=ServerApi('1'))



# Вибір бази даних і колекції
db = client["cats_database"]
collection = db["cats"]

# Функція для виведення всіх записів із колекції
def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)

# Функція для пошуку кота за ім'ям
def find_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кіт на ім'я {name} не знайдений.")
# Функція для створення нового кота
def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    result = collection.insert_one(cat)
    print(f"Кіт доданий з _id: {result.inserted_id}")

# Функція для оновлення віку кота за ім'ям
def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count > 0:
        print(f"Вік кота {name} оновлено.")
    else:
        print(f"Кіт на ім'я {name} не знайдений.")

# Функція для додавання нової характеристики до списку features кота за ім'ям
def add_feature_to_cat(name, new_feature):
    result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    if result.matched_count > 0:
        print(f"Характеристика '{new_feature}' додана коту {name}.")
    else:
        print(f"Кіт на ім'я {name} не знайдений.")

# Функція для видалення кота за ім'ям
def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кіт на ім'я {name} видалений.")
    else:
        print(f"Кіт на ім'я {name} не знайдений.")

# Функція для видалення всіх записів із колекції
def delete_all_cats():
    result = collection.delete_many({})
    print(f"Видалено {result.deleted_count} записів.")

try:
    # виклик функцій, наприклад:
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
except pymongo.errors.ConnectionError:
    print("Не вдалося підключитися до MongoDB.")
except pymongo.errors.PyMongoError as e:
    print(f"Сталася помилка: {e}")


