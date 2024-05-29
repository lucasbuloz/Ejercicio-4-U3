from classPubli import publi
from classlibro import libro
from classCD import CD
from gestor import gestor

def test():
    g=gestor
    
    b=True
    
    while b==True:
        print("---MENU DE OPCIONES---")
        print("1. Agregar publicaciones")
        print("2. Encontrar publicacion ")
        print("3. Mostrar cantidad de publicaciones de cada tipo")
        print("4. Mostrar publicaciones ")
        print("5. Finalizar ")
        
        op= int(input("Ingrese opcion: "))
        
        if op==1:
            g.inicializarcd()
            g.inicializarlibro()
            
            
        elif op== 2:
            g