from classPubli import publi
from classlibro import libro
from classCD import CD
from gestor import gestor

def test():
    g=gestor()
    
    b=True
    
    while b==True:
        print("---MENU DE OPCIONES---")
        print("1. Agregar publicaciones")
        print("2. Encontrar publicacion ")
        print("3. Mostrar cantidad de publicaciones de cada tipo")
        print("4. Mostrar publicaciones ")
        print("5. Finalizar ")
        
        op= int(input("Ingrese opcion: "))
        while op < 1 or op> 5:
            print("Opcion inválida, intente de nuevo")
            op= int(input("Ingrese opcion: "))
        if op==1:
            g.inicializarcd()
            g.inicializarlibro()
            g.mostrar()
            
        elif op== 2:
            g.encontrar()
        elif op== 3:
            g.contarpubli()
        elif op== 4:
            g.mostrartodo()
        elif op== 5:
            print("----MENU CERRADO---")
            b=False 