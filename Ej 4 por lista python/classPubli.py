class publi:
    __tit: str
    __cat: str
    __pre: float
    
    def __init__(self, t, c,p):
        self.__tit= t
        self.__cat=c
        self.__pre= p
        
    def gettit(self):
        return self.__tit
    def getcat(self):
        return self.__cat
    def getpre(self):
        return self.__pre
    
    def __str__(self):
        return (f"{self.__tit}, {self.__cat}, {self.__pre}")
    
    def calcularimporte(self):
        pass