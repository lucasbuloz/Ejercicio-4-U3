from classPubli import publi
class libro(publi):
    __nom: str
    __fecha: int
    __cantpag: int
    
    def __init__(self, t, c, p, nom, f,cp):
        super().__init__(t, c, p)
        self.__nom= nom
        self.__fecha=f
        self.__cantpag=cp
        
    def __str__(self):
        return (f"titulo: {self.gettit()}, cat: {self.getcat()}, prec: {self.getpre()}, nom: {self.__nom}, fecha: {self.__fecha}, cantpag: {self.__cantpag} ")
    
    def getfecha(self):
        return self.__fecha

    def calcularimporte(self):
        diferencia=2024 - self.getfecha()
        implib= float(((diferencia/100)*self.getpre()))
        return implib