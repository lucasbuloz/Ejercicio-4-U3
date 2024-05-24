from Classnodo import nodo

class lista:
    __comienzo: nodo
    
    def __init__(self):
        self.__comienzo=None
        
    def agregar(self, P):
        nodo = nodo(P)
        nodo.setsig(self.__comienzo)
        self.__comienzo
        