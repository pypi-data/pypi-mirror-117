# client = pymongo.MongoClient("mongodb+srv://root:<password>@cluster0.ooglx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
import pymongo
from . import DBInterface


class MongoDBInterface(DBInterface, dict):
    def __init__(self, account_label, user="root", pws="root", collection="auth"):
        super().__init__()

        self.client = pymongo.MongoClient(
            f"mongodb://{user}:{pws}@cluster0-shard-00-00.{account_label}.mongodb.net:27017,cluster0-shard-00-01.{account_label}.mongodb.net:27017,cluster0-shard-00-02.ooglx.{account_label}.net:27017/{collection}?ssl=true&authSource=admin"
        )
        self.table = None

    def select_table(self, database, table_name):
        self.table = self.client[database][table_name]

    def __insert__(self, key, value, e=RuntimeError("key exist")):
        if self.__select__(key) is None:
            return self.table.insert_one({
                "key": key,
                **value
            })
        else:
            raise e

    def __select__(self, key):
        result = self.table.find_one({'key': key})
        if result is None:
            return result
        result = dict(result)
        del result["_id"]
        return result

    def __update__(self, key, value):
        if self.__select__(key) is None:
            raise RuntimeError(f"key is not existed: {key}")
        select_filter = {"key": key}
        value = {"$set": value}
        return self.table.update_one(select_filter, value)

    def __remove__(self, key):
        if self.__select__(key) is None:
            raise RuntimeError(f"key is not existed: {key}")

        select_filter = {"key": key}
        return self.table.delete_one(select_filter)



