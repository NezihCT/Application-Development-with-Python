import pymongo
from bson import ObjectId
#from Person import Person

__DATABASE_NAME = "PhoneBookDB"
__COLLECTION_NAME = "People"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ConnectAtlas():
    return pymongo.MongoClient(
        "mongodb+srv://root:Password1@cluster0.cxr6y.mongodb.net/PhoneBookDB?retryWrites=true&w=majority",
        ssl_cert_reqs='CERT_NONE')


def Add(person):
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTION_NAME]
    myCollection.insert_one(person.__dict__)


def Delete(param):
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTION_NAME]
    query = {"_id": ObjectId(param)}
    myCollection.delete_one(query)


def List():
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTION_NAME]
    print(f"{'_id':30}{'FirstName':30}{'LastName':30}{'Phone':30}{'Mail':30}")
    print("_" * 150, "\n")

    for x in myCollection.find():
        body = ""
        for key, value in x.items():
            body += f"{str(value):30}"
        print(body)
    print("\n\n")

def Update(person):
    pass
