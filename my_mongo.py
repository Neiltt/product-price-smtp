from pymongo import MongoClient
import datetime

MONGODB_URL = ''
DATABASE_NAME = 'neil'
COLLECTION_NAME = "min_price"

def init_mongo():
    client = MongoClient(MONGODB_URL)
    db = client[DATABASE_NAME]
    return db

def get_min_price(name):
    db = init_mongo()
    prices = db.prices
    prices = db.prices.find({"product_name": name})
    if prices[0] and prices[0]['price']:
        return prices[0]['price']

def set_min_price(name, price):
    db = init_mongo()
    # pymongo
    price_dict = {
        "product_name": name,
        "price": price,
        "date": datetime.datetime.utcnow()
    }
    prices = db.prices
    new_values = {"$set": price_dict}
    my_query = {"product_name": name}
    prices.update_one(my_query, new_values)

def init_product_price(name, price):
    db = init_mongo()
    price_dict = {
        "product_name": name,
        "price": price,
        "date": datetime.datetime.utcnow()
    }
    # 存取 db 資料庫中的 prices 集合（Collection），並將其儲存到變數 prices 中。
    # 使用insert_one 方法將 price_dict 插入 prices 集合中。
    # 獲取插入的文件的 ObjectID（唯一標識符），並將其儲存到變數 price_id 中。
    prices = db.prices
    price_id = prices.insert_one(price_dict).inserted_id

# 測試
# init_product_price("Nintendo S", 20000)
# set_min_price("Nintendo S", 70000)