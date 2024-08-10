from abc import ABC, abstractmethod
class publi:
    __tit:str
    __cat:str
    __precio:float
    
    def __init__(self, tit, cat, precio):
        self.__tit=tit
        self.__cat=cat
        self.__precio=precio
        
    def gettit(self):
        return self.__tit
    def getcat(self):
        return self.__cat
    def getprecio(self):
        return self.__precio
    
    @abstractmethod
    def importe(self):
        pass