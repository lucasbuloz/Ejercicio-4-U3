from Classpubli import publi

class libro(publi):
    __nom: str
    __fecha: int
    __cantpag: int
    
    def __init__(self, t, c, p, nom, f, cp):
        super().__init__(t, c, p)
        self.__nom= nom
        self.__fecha=f
        self.__cantpag= cp
    
    def getnom(self):
        return self.__nom
    def getfecha(self):
        return self.__fecha
    def getcantpag(self):
        return self.__cantpag
    
    def mostrarli(self):
        print (f"autor: {self.__nom}, fecha: {self.__fecha}, cantpag: {self.__cantpag}, titulo: {self.gettit()}, categ: {self.getcat()}, precio: {self.getpre()} \n")
        
    def calcularimporte(self):
        diferencia=2024 - publi.getfecha()
        implib= float(((diferencia/100)*publi.getpre()))
        return implib