class reloj:
    __marca:str
    __color: str
    
    def __init__(self,m,c):
        self.__marca=m
        self.__color=c
        
    def getmarca(self):
        return self.__marca
    def getcolor(self):
        return self.__color
    
    