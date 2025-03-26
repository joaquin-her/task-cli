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
        """Aniade una tarea a la base de datos"""

        task = Task(self.getLastId(), task_description)
        self.data["tasks"].append(task.to_dict())
        self.data["items"] += 1
        self.saveData()
        pass

    def loadData(self, URI):
        """Lee el archivo y carga sus datos"""
        with open(URI, "r") as file:
            data = file.read()
            return json.loads(data)
            

    def createData(self, URI):
        """Crea el archivo vacio para guardar tareas si en la ruta no hay ningun elemento"""

        with open(URI, "w") as file:
            data = {"tasks": [], "items":0}
            json.dump(data, file )
        return data

    def saveData(self):
        """Guarda su contenido de .data en la ruta de self.URI"""
        with open(self.URI, "w") as file:
            json.dump(self.data, file, indent= 4)


    def getLastId(self):
        """Devuelve el valor del ultimo Id de sus tareas"""
        return self.data["items"]
    
    def getItems(self):
        """Devuelve el listado de objetos almacenados"""
        return self.data["tasks"]

    def getLast(self, limit):
        """Devuelve los ultimos 'limit' elementos de la base de datos"""
        tasks = self.data["tasks"]
        if len(tasks) >= limit:
            return tasks[-limit:]  
        else:
            return tasks  