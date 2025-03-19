from .IDataBase import IDataBase
from ..Task import Task
import json

class JsonDataBase(IDataBase):
    """ Docstring for JsonDataBase"""
    def __init__(self, URI:str):
        self.URI = URI
        try:
            self.data = self.loadData(URI)
        except FileNotFoundError:
            self.data = self.createData(URI)
             
    def add(self, task_description:str):
        task = Task(self.getLastId(), task_description)
        self.data["tasks"].append(task.to_dict())
        self.data["items"] += 1
        self.saveData()
        pass

    def loadData(self, URI):
            with open(URI, "r") as file:
                data = file.read()
                return json.loads(data)
               

    def createData(self, URI):
            with open(URI, "w") as file:
                 data = {"tasks": [], "items":0}
                 json.dump(data, file )
            return data

    def saveData(self):
        with open(self.URI, "w") as file:
             json.dump(self.data, file, indent= 4)


    def getLastId(self):
        return self.data["items"]
    
    def getLast(self, limit):
        tasks = self.data["tasks"]
        if len(tasks) >= limit:
            return tasks[-limit:]  
        else:
            return tasks  