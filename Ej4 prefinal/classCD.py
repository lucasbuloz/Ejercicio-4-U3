from classpubli import publi


class CD(publi):
    __trep:int
    __nomnarr:str
    
    def __init__(self, tit, cat, precio, trep, nomnarr):
        super().__init__(tit, cat, precio)
        self.__trep=trep
        self.__nomnarr=nomnarr
        
    def gettrep(self):
        return self.__trep
    def getnomnarr(self):
        return self.__nomnarr
    
    def __str__(self):
        return (f"titulo: {self.gettit()}, categoria: {self.getcat()}, precio: {self.getprecio()}, trep: {self.gettrep()}, nomnarr: {self.getnomnarr()} \n")
        
    def imp(self):
        impcd= self.getprecio()*1.10
        return impcd