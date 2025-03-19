from datetime import date


class Task(object):
	"""docstring for Task"""
	def __init__(self, id:int, description: str):
		self.id = id 
		self.description = description
		self.status = 'to-do'
		self.created = date.today()
		self.updated = date.today()

	def to_dict(self)-> dict : 
		dict = {
			"id": self.id,
			"description": self.description,
			"status": self.status,
			"created": self.created.isoformat(),
			"updated": self.updated.isoformat()
		}
		return dict