from gestor import gestor
from classpubli import publi

def test():
    g=gestor()
    b=True

    while b==True:
        print ("---MENU DE OPCIONES---")
        print("0. Cargarpublicaciones")
        print("1. Agregar publicaciones")
        print("2. Encontrar posición")
        print("3. Contar publicaciones")
        print("4. Mostrar algunos datos")
        print("5.Salir")
        opi=int(input('Ingrese opcion: '))
        
        if opi==0:
            g.inicializarcd()
            g.inicializarlibro()
            g.mostrar()
        elif opi==1:
            g.agregar()
            g.mostrar()
        
        elif opi==2:
            g.encontrar()
            
        elif opi==3:
            g.contarpublic()
            
        elif opi==4:
            g.mostraralgunosdatos()
            
        elif opi==5:
            b=False
            print("---Menu CERRADO---")
        elif opi>5:
            while opi<0 or opi>5:
                print("Opcion invalida")
                op=int(input("Ingrese opcion nuevamente: "))
            