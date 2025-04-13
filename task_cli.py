import sys 
from Task import Task

first_argument = sys.argv[1]

saveFilePath = './data/tasks.json'
dataBase = JsonDataBase(saveFilePath)

def addTask(data_path:str, task_description:str): 
	newTask = Task(1, task_description)
	dataBase.add(newTask)



def handle_list():
	return 'La lista esta vacia'


match first_argument:
	case "add":
		print( addTask(saveFilePath, sys.argv[2]))
	case 'list':
		print(handle_list())


