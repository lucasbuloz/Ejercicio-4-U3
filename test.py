from Classlibro import libro
from Classlista import lista
from ClassCD import CD

def test():

    L= lista()
    CD1= CD("OrgulloyPrejuicio", "Novela", 1300, 130, "Pepeargento")
    lis1= libro("OrgulloyPrejuicio", "Novela", 1300, "Pepito", 2015, 177)
    
    while True:
        print("---MENU DE OPCIONES---")
        print("1. Agregar publicaciones")
        print("2. Encontrar publicacion ")
        print("3. Mostrar cantidad de publicaciones de cada tipo")
        print("4. Mostrar publicaciones ")
        
        op= int(input("Ingrese opcion: "))
        
        if op==1:
            L.agregar(CD)
            L.agregar(lis1)
            L.mostrar()
            