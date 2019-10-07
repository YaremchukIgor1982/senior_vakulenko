from pymongo import MongoClient


def collection(db, table):
    return(db.collection['{}'.format(table)])


class MongoDBConnectionManager():

    def __init__(self):
        self.client = MongoClient('localhost',27017)


    def db(self,db_name):
        return (self.client['{}'.format(db_name)])

    def close(self,):
        self.client.close()

    # connecting with a localhost
