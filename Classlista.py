from Classlibro import libro
from ClassCD import CD
from Classpubli import publi
from Classnodo import Nodo

class lista:
    __comienzo: Nodo
    
    def __init__(self):
        self.__comienzo=None
        
    def agregar(self, P):
        nodo = Nodo(P)
        nodo.setsig(self.__comienzo)
        self.__comienzo= nodo
        
    def mostrar (self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.getdato())
            aux=aux.getsig()
    
    def instancia(self):
        pos=int(input("Ingrese posicion: "))
        aux= self.__comienzo
        i=0
        
        while aux !=None and i<pos:
            aux=aux.getsig()
            i+=1
        if aux is None:
            print("Posicion incorrecta \n")
        else:
            publi=aux.getdato()
            if isinstance(publi,libro):
                print(f"La publicacion en la posicion {pos} es un libro.")
            elif isinstance(publi,CD):
                print(f"La publicacion en la posicion {pos} es un CD.")
            else:
                print(f"La publicacion en la posicion {pos} es de tipo desconocido.")
                
                