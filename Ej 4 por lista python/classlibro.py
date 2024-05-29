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
        
    