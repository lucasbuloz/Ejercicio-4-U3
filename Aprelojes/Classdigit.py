from Classreloj import reloj

class digital(reloj):
    __bateria: str
    __tl:str
    
    def __init__(self, m, c, b, tl):
        super().__init__(m,c)
        self.__bateria=b
        self.__tl= tl
        
    