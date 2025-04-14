""" CLI.py
    This module contains the CLI class, which is responsible for handling the command line interface of the application.
    It takes a list of arguments and executes the corresponding command. The commands are as follows:
    - list: Lists all tasks or filters them based on the provided argument.
    - add: Adds a new task to the database.
    - mark-in-progress: Marks a task as in-progress.
    - mark-done: Marks a task as done.
    - update: Updates a task's field with the provided value.
    - delete: Deletes a task from the database.
"""


from typing import List
from ..DataBase import IDataBase
from ..Task import Task
class CLI(object):
    def __init__(self, database: IDataBase):
        """ Creates a CLI Ibject with a data source to save and  """
        self.database = database
    
    def handle(self, args: List[str]):
        """ handles the console args. Args must be a list of Strings """
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

    def executeCommand(self, command: str, first_arg:str='10', second_arg:str='', third_arg:str=''):
        """ Determines and executes a command"""
        match command:
            case 'list':
                self.handleListCommand(first_arg)
            case 'add':
                self.addTask(first_arg)
            case 'mark-in-progress':
                self.updateTask(first_arg, 'status', 'in-progress')
            case 'mark-done':
                self.updateTask(first_arg, 'status', 'done')
            case 'update':
                self.updateTask(first_arg, second_arg, third_arg)
            case 'delete':
                self.deleteTask(first_arg)
            case default:
                raise ValueError(f"Comando desconocido: {command}")


    def updateTask(self, id:str, field:str, value:str):
        """ Updates a task in the database """
        self.database.update(id, field, value)

    def addTask(self, task_description:str): 
        """ appends a task to the database"""
        self.database.add(task_description)
        print(task_description + ": aniadida correctamente")
        
    def handleListCommand(self, first_arg:str):
        """ Handles the list command """
        if not first_arg.isnumeric():
            self.filterTasks(first_arg)
        elif first_arg == '':
            self.listAllTasks()
        elif first_arg > '0':
            self.listLastTasks(first_arg)
        else:
            raise ValueError("El argumento no es valido")

    def listLastTasks(self, limit:str):
        """ Lists the last tasks in the database """
        items = self.database.getLast(int(limit))
        self.printTasks(items)

    def listAllTasks(self):
        """ Lists all the tasks in the database """
        items = self.database.getItems()
        self.printTasks(items)

    def filterTasks(self, filter:str):
        """ Filters the tasks in the database """
        items = self.database.getItems(filter)
        if len(items) == 0:
            print("No se han encontrado tareas")
            return
        self.printTasks(items)

    def printTasks(self, items:List[dict]):
        """ Prints the tasks in the database """
        for item in items:
            print(f"\n{item["id"]}:\t")
            print(Task.fromDict(item))
        
    def deleteTask(self, id:str):
        self.database.removeItem(int(id))
        print(f"Tarea {id} eliminada correctamente")

