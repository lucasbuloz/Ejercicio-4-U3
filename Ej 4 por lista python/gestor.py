from classCD import CD
from classlibro import libro
from classPubli import publi
import csv

class gestor:
    __lista:list
    
    def __init__(self):
        self.__lista= []
        
    def inicializarcd(self):
        archivo=open("Ejercicio 4/Ej 4 por lista python/archvioCD.csv", "r")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            ncd=CD(fila[0], fila[1], float(fila[2]), int(fila[3]), fila[4])
            self.__lista.append(ncd)
        archivo.close()
            
    def inicializarlibro(self):
        archivo=open("Ejercicio 4/Ej 4 por lista python/archviolibro.csv", "r")
        reader=csv.reader(archivo, delimiter=",")
        for fila in reader:
            nlibro=libro(fila[0], fila[1], float(fila[2]),fila [3],int(fila[4]),int(fila[5]))
            self.__lista.append(nlibro)
        archivo.close()
        
    