from Classpubli import publi
class CD (publi):
    __min: int
    __narrador: str
    
    def __init__(self,t,c,p,m,n):
        super().__init__(t,c,p)
        self.__min=m
        self.__narrador=n
        