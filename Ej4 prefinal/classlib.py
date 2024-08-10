from classpubli import publi

class libro(publi):
    __nomaut:str
    __edicion:int
    _cpag:int
    
    def __init__(self, tit, cat, precio, nomaut, edicion, cpag):
        super().__init__(tit, cat, precio)
        self.__nomaut=nomaut
        self.__edicion=edicion
        self._cpag=cpag
        
    def getnomaut(self):
        return self.__nomaut
    def getedicion(self):
        return self.__edicion
    def getcpag(self):
        return self._cpag
    def __str__(self):
        return (f"autor: {self.__nomaut}, edicion: {self.__edicion}, cantpag: {self._cpag}, titulo: {self.gettit()}, categ: {self.getcat()}, precio: {self.getprecio()} \n")
    
    def imp(self):
        antig=2024-int(self.getedicion())
        implib= float(((antig/100)*self.getprecio()))
        return implib