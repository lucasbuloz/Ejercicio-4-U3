from classCD import CD
from classlib import libro
from classpubli import publi
import csv

class gestor:
    __lista:list
    
    def __init__(self):
        self.__lista= []
        
    def inicializarcd(self):
        archivo= open("C:/Users/lucas/OneDrive/Documents/Lucas/Facultad/POO/Unidad 3/Ejercicio 4/Ej4 prefinal/archvioCD.csv")
        reader=csv.reader (archivo, delimiter=",")
        for fila in reader:
            ncd=CD(fila[0], fila[1], float(fila[2]), int(fila[3]), fila[4])
            self.__lista.append(ncd)
        archivo.close()
        
    def inicializarlibro(self):
        archivo=open("C:/Users/lucas/OneDrive/Documents/Lucas/Facultad/POO/Unidad 3/Ejercicio 4/Ej4 prefinal/archviolibro.csv")
        reader=csv.reader(archivo, delimiter=",")
        for fila in reader:
            nlibro=libro(fila[0], fila[1], float(fila[2]),fila [3],int((fila[4])),int(fila[5]))
            self.__lista.append(nlibro)
        archivo.close()
        

    def agregar(self):
        op=int(input("Que desea agregar? 1 para CD - 2 para libro: "))
        while 1>op or op>2:
            print("Opcion invalida")
            op=int(input("Ingrese opcion nuevamente: "))
        tit=input("Titulo: ")
        cat=input("Categoria: ")
        precio=float(input("Precio: "))
        
        if op==1:
            trep=int(input("Tiempo de reproduccion: "))
            nomnarr=input("Nombre de narrador: ")
            ncd=CD(tit, cat, precio, trep, nomnarr)
            self.__lista.append(ncd)
        elif op==2:
            naut=input("Nombre de autor: ")
            ed=input("Editorial: ")
            cpag=input("Cant de pags: ")
            nlibro=libro(tit, cat, precio, naut, ed, cpag)
            self.__lista.append(nlibro)
            
    def mostrar(self):
        for publi in self.__lista:
            print (publi)
            
    def encontrar(self):
        pos=int(input("Ingrese posicion: "))
        while pos<0 or pos >= len(self.__lista):
            print ("Posición incorrecta, intente nuevamente")
            pos=int(input("Ingrese posicion: "))
        if True:
            item=self.__lista[pos]
            if isinstance(item,libro):
                print(f"La publicacion en la posicion {pos} es un libro. \n")
            elif isinstance(item, CD):
                print(f"La publicacion en la posicion {pos} es un CD. \n")
            else:
                print(f"La publicacion en la posicion {pos} es de tipo desconocido. \n")
    
    def contarpublic(self):
        ccd=0
        Cli=0
        for publi in self.__lista:
            if isinstance(publi,CD):
                ccd+=1
            elif isinstance(publi,libro):
                Cli+=1
        print(f"Hay {ccd} CDs y {Cli} libros en el libro")
    
    def mostraralgunosdatos(self):
        for publi in self.__lista:
            print(f"Titulo: {publi.gettit()}, Precio: {publi.imp():.2f}, Categoria: {publi.getcat()}")