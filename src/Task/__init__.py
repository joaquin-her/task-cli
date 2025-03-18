import os 


class Task(object):
	"""docstring for Task"""
	def __init__(self, id:int, description: str):
		self.id = id 
		self.description = description
		self.status = 'to-do'
		self.created = os.timestamp()
		self.updated = os.timestamp()

		