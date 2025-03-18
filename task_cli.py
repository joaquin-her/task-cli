import sys 

from src.CLI import CLI
from src.DataBase.JsonDataBase import JsonDataBase

saveFilePath = 'tasks.json'
database = JsonDataBase(saveFilePath)

cli = CLI(database)

cli.handle(sys.argv[1:])

