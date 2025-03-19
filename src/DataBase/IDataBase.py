from abc import ABC, abstractmethod
from typing import List
from ..Task import Task

class IDataBase(ABC):
    """Interfaz para guardar y cargar datos de tareas."""
    
    @abstractmethod
    def add(self, task: Task ):
        """Guarda la lista de tareas en un archivo."""
        pass

    @abstractmethod
    def loadData(self) -> List['Task']:
        """Carga la lista de tareas desde un archivo."""
        pass