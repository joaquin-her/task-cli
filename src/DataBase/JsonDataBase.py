from .IDataBase import IDataBase
from ..Task import Task
from .DataBaseExceptions import UnknownIndexException
import json

class JsonDataBase(IDataBase):
    """ Docstring for JsonDataBase"""
    def __init__(self, URI:str):
        self.URI = URI
        try:
            self.data = self.loadData(URI)
        except FileNotFoundError:
            self.data = self.createData(URI)

    def loadData(self, URI):
        """Lee el archivo y carga sus datos"""
        with open(URI, "r") as file:
            content = file.read()
            data = json.loads(content)
            return data

    def createData(self, URI):
        """Crea el archivo vacio para guardar tareas si en la ruta no hay ningun elemento"""

        with open(URI, "w") as file:
            data = {"tasks": {}, "items":0}
            json.dump(data, file )
        return data

    def saveData(self):
        """Guarda su contenido de .data en la ruta de self.URI"""
        with open(self.URI, "w") as file:
            json.dump(self.data, file, indent= 4)
        return

    def add(self, task_description:str):
        """Aniade una tarea a la base de datos"""
        task = Task(task_description)
        id = self.getLastId()
        self.data["tasks"][str(id)] = task.to_dict()
        self.data["items"] += 1
        self.saveData()
        pass

    def getItem(self, index:int)-> dict:
        """Devuelve un diccionario del objeto solicitado con ese indice """
        if self.exists(index):
            return self.data["tasks"][str(index)]

    def getLastId(self)-> int:
        """Devuelve el valor del ultimo Id de sus tareas"""
        return self.data["items"]
    
    def getItems(self)-> dict:
        """Devuelve el listado de objetos almacenados"""
        return self.data["tasks"]

    def getLast(self, limit):
        """Devuelve los ultimos 'limit' elementos de la base de datos"""
        tasks = self.data["tasks"]
        if len(tasks) >= limit:
            return tasks[-limit:]  
        else:
            return tasks  
    
    def removeItem(self, index):
        """Se elimina el objeto en el indice de la Clase y de su persistencia"""
        self.exists(index)
        tasks = self.data["tasks"]
        del tasks[str(index)]
        self.saveData()
        return

    def updateStatus(self, index:int, status:str):
        """Se convierte el indice del diccionario a Objeto, se modifica, y se guarda su modificado"""
        if (self.exists(index)):
            requestedTask = self.getItem(index)
            updatedTask = Task.fromDict(requestedTask)
            updatedTask.setStatus(status)
            self.saveTask(index, updatedTask)
            self.saveData()

    def saveTask(self, index:int, task:Task):
        self.data["tasks"][str(index)] = task.to_dict()


    def exists(self, index:int)->bool:
        if (str(index) in self.data["tasks"]):
            return True
        raise UnknownIndexException(f"El indice {index} no pudo encontrarse")
   