import pymongo  

def save(name,std,age):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")

    mydb = myclient["mydatabase"]
    
    collection = mydb['StudentData']

    if len(list(collection.find({'Name':name.lower()})))==0:
        collection.insert_one({'Name':name.lower() ,'Std':std,'Age':age})
        myclient.close()
        return 1
    return 0
    
    
def show(name=None):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["mydatabase"]
    collection = mydb['StudentData']
    # data=collection.find()
    if name==None:
        data=collection.find({},{'_id':0})
    else:
        data=collection.find({'Name':name.lower()},{'_id':0})
    dic={}
    for i in data:
        dic[str(i.get('Name'))]=i
    return dic
    
def update(id,name,std,age):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["mydatabase"]
    collection = mydb['StudentData']
    cursor=collection.find({'Name':id.lower()},{'_id':0})
    data=list(cursor)
    if len(data)!=0:
        collection.update_one({'Name':id.lower()},{'$set':{'Name':name,'std':std,'age':age}})
        return "Updated !!"
    else:
        return "Don't Exists"
    
def delete(name:str):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["mydatabase"]
    collection = mydb['StudentData']
    cursor=collection.find({'Name':name.lower()},{'_id':0})
    data=list(cursor)
    if len(data)!=0:
        collection.delete_many({'Name':name.lower()})
        return "Deleted !!"
    else:
        return "Don't Exists"
   
