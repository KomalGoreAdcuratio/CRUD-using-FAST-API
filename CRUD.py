from fastapi import FastAPI
#from .models import Student

import pymongo
import json 

app=FastAPI()


from Models import Student
from database import *
 
@app.post('/EnrollStudent')
def enrollStudent(request: Student):
    responce=save(request.name,request.std, request.age)
    if responce:
        return request
    else:
        return {"error":"Name Already Exist"}

@app.get('/get')
def getStudents():
    data=show()
    print(data)
    return {'data':data}

@app.get('/get/{name:str}')
def getStudent(name:str):
    data=show(name=name)
    print(data)
    return {'data':data}

@app.put('/update/{id:str}')
def updateStudent(id:str,request: Student):
    responce= update(id,request.name,request.std,request.age)
    return {'Result':responce}

@app.delete('/delete/')
def deleteStudent(name:str):
    data=delete(name=name)
    print(data)
    return {'data':data}