from abc import ABC, abstractmethod

class Nodo(ABC):
    def __init__(self, token, id_nodo):
        self.nombre = token.type