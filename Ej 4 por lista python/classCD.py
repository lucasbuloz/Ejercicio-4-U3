from classPubli import publi
class CD (publi):
    __min: int
    __narrador: str

    def __init__(self, t, c, p, m,n):
        super().__init__(t, c, p)
        self.__min=m
        self.__narrador=n
    
    def getmin(self):
        return self.__min
    def getnarrador(self):
        return self.__narrador
    
    def mostrarcd (self):
        print (f"min: {self.__min}, narrador: {self.__narrador}, tit: {self.gettit()}, categ: {self.getcat()}, precio: {self.getpre()} \n")