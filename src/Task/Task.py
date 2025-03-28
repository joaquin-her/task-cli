from datetime import datetime

STATUS_VALUES = ["to-do", "done", "in-progress"]

class Task(object):
	"""docstring for Task"""
	def __init__(self, description: str):
		self.description = description
		self.status = 'to-do'
		self.created = datetime.now().isoformat()
		self.updated = datetime.now().isoformat()

	def to_dict(self)-> dict : 
		dict = {
			"description": self.description,
			"status": self.status,
			"created": self.created,
			"updated": self.updated
		}
		return dict
	
	def setStatus(self, status:str):
		if status in STATUS_VALUES:
			self.status = status
			self.updated = datetime.now().isoformat()
			return
		raise UnknownStatusException(status)

	@classmethod
	def fromDict(cls, dict: dict) :
		task = Task(dict["description"])
		for key, value in dict.items():
			if hasattr(task, key):
				setattr(task, key, value)
		return task
	
class UnknownStatusException(Exception):
	"""Excepcion que se lanza cuando se ingresa un Status desconocido"""
	def __init__(self, status):
		super().__init__(f"El status '{status}' no es valido o es deconocido ")
		
