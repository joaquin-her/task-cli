from abc import ABC, abstractmethod
from typing import List


class IDataBase(ABC):
    """Interfaz para guardar y cargar datos de tareas."""
    
    @abstractmethod
    def add(self, task_description: str):
        """Guarda la tarea."""
        pass

    @abstractmethod
    def getLast(self, limit:int) -> List[dict]:
        """Devuelve una lista de tareas en los ultimos lugares. La cantidad a devolver es pasada por el atrributo 'limit'."""
        pass

    @abstractmethod
    def updateStatus(self, index:int, task_description: str):
        """Modifica el status de la tarea."""
        pass
