from typing import List
from ..DataBase import IDataBase
from ..Task import Task
class CLI(object):
    """ Creates a CLI Ibject with a data source to save and  """
    def __init__(self, database: IDataBase):
        self.database = database
    
    """ handles the console args. Args must be a list of Strings """
    def handle(self, args: List[str]):
        argument_amount = len(args)
        if argument_amount > 0 :
            command = args[0]
        else:
            raise ValueError("Cantidad de argumentos invalida")
        match argument_amount:
            case 1:
                self.executeCommand(command)
            case 2:
                self.executeCommand(command, args[1])
            case 3:
                self.executeCommand(command, args[1], args[2])
            case 4:
                self.executeCommand(command, args[1], args[2], args[3])

    """ determines and executes a command"""
    def executeCommand(self, command: str, first_arg:str='10', second_arg:str='', third_arg:str=''):
        match command:
            case 'list':
                self.listTasks(first_arg)
            case 'add':
                self.addTask(first_arg)
            case 'mark-in-progress':
                self.updateTask(first_arg, 'status', 'in-progress')
            case 'mark-done':
                self.updateTask(first_arg, 'status', 'done')
            case 'update':
                self.updateTask(first_arg, second_arg, third_arg)

    def updateTask(self, id:str, field:str, value:str):
        self.database.update(id, field, value)

    """ appends a task to the database"""
    def addTask(self, task_description:str): 
        self.database.add(task_description)
        print(task_description + ": aniadida correctamente")
        
    """ lists the last 10 tasks in the database"""
    def listTasks(self, amount):
        items = self.database.getLast(int(amount))
        for item in items:
            print(f"\n{item["id"]}:\t")
            print(Task.fromDict(item))