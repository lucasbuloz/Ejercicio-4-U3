from Classpubli import publi
class nodo:
    __publi: publi
    __siguiente:None
        
    def __init__ (self, P): 
        self.__publi=P
        self.__siguiente= None
        
    def setsig(self,sig):
        self.__siguiente=sig
        
    def getsig(self):
        return self.__siguiente
    
    def getdato(self):
        return self.__publi