from typing import List
from ..DataBase import IDataBase

class CLI(object):
    """ Creates a CLI Ibject with a data source to save and  """
    def __init__(self, database: IDataBase):
        self.database = database
    
    """ handles the console args. Args must be a list of Strings """
    def handle(self, args: List[str]):
        if len(args) >= 2: 
            command = args[0]
            description = str(args[1])
            match command:
                case 'add':
                    self.addTask(description)
        if args[0] == 'list':
            self.listTasks(args[1:])

    # """ appends a task to the database"""
    def addTask(self, task_description:str): 
        self.database.add(task_description)
        print(task_description + ": aniadida correctamente")
        
    def listTasks(self, args):
        if len(args) == 0:
            items = self.database.getLast(10)
            for item in items:
                print(item)