from classCD import CD
from classlibro import libro
from classPubli import publi
import csv

class gestor:
    __lista:list
    
    def __init__(self):
        self.__lista= []
        
    def inicializarcd(self):
        archivo=open("C:/Users/Buloz/Documents/Lucas/Facultad/LCC/POO/Unidad 3/Codigos U3/Ejercicio-4-U3/Ej 4 por lista python/archvioCD.csv", "r")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            ncd=CD(fila[0], fila[1], float(fila[2]), int(fila[3]), fila[4])
            self.__lista.append(ncd)
        archivo.close()
            
    def inicializarlibro(self):
        archivo=open("C:/Users/Buloz/Documents/Lucas/Facultad/LCC/POO/Unidad 3/Codigos U3/Ejercicio-4-U3/Ej 4 por lista python/archviolibro.csv", "r")
        reader=csv.reader(archivo, delimiter=",")
        for fila in reader:
            nlibro=libro(fila[0], fila[1], float(fila[2]),fila [3],int(fila[4]),int(fila[5]))
            self.__lista.append(nlibro)
        archivo.close()
     
    def mostrar(self):
        for publi in self.__lista:
            print (publi)
    
    def encontrar(self):
        pos=int(input("Ingrese posicion: "))
        while pos<0 or pos>=len(self.__lista):
            print("Poisicion fuera de rango, vuelva a intentar. ")
            pos=int(input("Ingrese posicion: "))
        if True:
            item=self.__lista[pos]
            if isinstance(item,libro):
                print(f"La publicacion en la posicion {pos} es un libro. \n")
            elif isinstance(item, CD):
                print(f"La publicacion en la posicion {pos} es un CD. \n")
            else:
                print(f"La publicacion en la posicion {pos} es de tipo desconocido. \n")
    
    def contarpubli(self):
        ccd=0
        cli=0
        for publi in self.__lista:
            if isinstance(publi,libro):
                cli+=1
            elif isinstance(publi,CD):
                ccd+=1
        print(f"Hay {ccd} cds y {cli} libros")

    def mostrartodo(self):
        for publi in self.__lista:
            print(f"titulo: {publi.gettit()}, categoria: {publi.getcat()}, precio: {publi.calcularimporte():.2f}")


#El ":.2f" que se muestra en el renglon de arriba para "{publi.calcularimporte():.2f}" sirve para mostrar solo 2 decimales dsp de la coma en los float