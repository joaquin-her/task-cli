from typing import List
from .. import Task
from ..DataBase.IDataBase import IDataBase

class CLI(object):
    """ Creates a CLI Ibject with a data source to save and  """
    def __init__(self, database: IDataBase):
        self.database = database
    
    """ handles the console args. Args must be a list of Strings """
    def handle(self, args: List[str]):
        print(len(args))
        print(args)
        if len(args) >= 2: 
            command = args[1]
            match command:
                case 'add':
                    print("add requested for "+ args[2])
                    # self.add_task(args[1])

    # """ appends a task to the database"""
    # def add_task(self, task_description:str): 
    #     newTask = Task(id=self.database.getLastId(), description=task_description )
    #     self.database.add(newTask)

