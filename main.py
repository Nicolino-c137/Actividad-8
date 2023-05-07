from menu import Menu as M
from clase import Conjunto as C

def cargarConjunto():
    datos= input("Ingrese los elementos que desea que tenga el conjunto separados por coma: ")
    elementos= [int(e.strip()) for e in datos.split(',')]
    Un_conjunto= C(elementos)
    return Un_conjunto

if __name__ == '__main__':
    conjunto1= cargarConjunto()
    conjunto2= cargarConjunto()
    menu= M(conjunto1,conjunto2)
    menu.generarMenu()
    