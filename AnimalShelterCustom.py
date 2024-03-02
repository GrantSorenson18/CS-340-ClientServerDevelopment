from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,user,passwd,host,port,db,col):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        # Connection Variables:
        USER = user
        PASS = passwd
        HOST = host
        PORT = port
        DB = db
        COL = col
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

#Create data entry method
#One argument data:should be dict of table entry with compatible values
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary     
            return True        
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
        
#Read data entry
#One argument data:key/value pair of entry eing searched for
    def read(self, data):
    	#result = self.database.animals.find(data)
    	if data is not None:
    	    return self.database.animals.find(data)
    	else:
            raise Exception("Data not found")
            return false
#Update data entry
#two arguments data: entry to be updated, newData:data to replacing old data
    def update(self, data, newData):
        newValues = {"$set":newData}
        if data is not None:
            x = self.database.animals.update_many(data,newValues)
            print(x.modified_count, "documents updated")
            return x.modified_count
        else:
            print("document not found")
            return 0
#Delete data entry
#one argument data:key/value pair of entry to be deleted
    def delete(self,data):
        if data is not None:
            x = self.database.animals.delete_many(data)
            print(x.deleted_count, "documents deleted")
            return x.deleted_count
        else:
            print("document not found")
            return 0


    
    