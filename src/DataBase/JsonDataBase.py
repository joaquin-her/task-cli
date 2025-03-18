from .IDataBase import IDataBase

class JsonDataBase(IDataBase):
    """ Docstring for JsonDataBase"""


    def __init__(self, URI:str):
        self.URI = URI

    def add(self, task):
        pass

    def load(self):
        pass