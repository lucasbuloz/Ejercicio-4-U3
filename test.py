from Classlibro import libro
from Classlista import lista
from ClassCD import CD

def test():

    L= lista()
    cd= CD("OrgulloyPrejuicio", "Novela", 1300, 130, "Pepeargento")
    lis= libro("OrgulloyPrejuicio", "Novela", 1300, "Pepito", 2015, 177)
    cd1 = CD("los 3 chanchitos", "fabula", 200, 50, "bartolome")
    lis1 = libro("los 3 chanchitos", "fabula", 1200, "juan", 2004, 1000)
    
    while True:
        print("---MENU DE OPCIONES---")
        print("1. Agregar publicaciones")
        print("2. Encontrar publicacion ")
        print("3. Mostrar cantidad de publicaciones de cada tipo")
        print("4. Mostrar publicaciones ")
        print("5. Finalizar ")
        
        op= int(input("Ingrese opcion: "))
        
        if op==1:
            L.agregar(cd)
            L.agregar(lis)
            L.agregar(cd1)
            L.agregar(lis1)
            cd.mostrarcd()
            lis.mostrarli()
            cd1.mostrarcd()
            lis1.mostrarli()
        elif op==2:
            L.instancia()
        elif op==3:
            L.canpubli()
        elif op==4:
            L.mostrartodo()
        elif op==5:
            break