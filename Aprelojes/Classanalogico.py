from Classreloj import reloj

class analogico(reloj):
    __mat: str
    
    def __init__(self, m, c, mat):
        super().__init__(m, c)
        self.__mat= mat
        