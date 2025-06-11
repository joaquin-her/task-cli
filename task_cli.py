import sys 
from src.CLI import CLI
from src.DataBase import JsonDataBase

saveFilePath = 'data/tasks.json' 
dataBase = JsonDataBase(saveFilePath)

app = CLI(dataBase)
app.handle(sys.argv[1:])


