import sys, os
from clase import Conjunto as C

class Menu:
    __elecciones= {}
    __conjunto1= None
    __conjunto2= None
    
    def __init__(self,conjunto1,conjunto2):
        self.__conjunto1= conjunto1
        self.__conjunto2= conjunto2
        self.__elecciones= {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '0': self.salir
        }
        
    def mostrarMenu(self):
        print("""
MENU PRINCIPAL

1. Calcular unión entre dos conjuntos
2. Calcular diferencia entre dos conjuntos
3. Verificar si los conjuntos son iguales
0. Salir
""")
        
    def generarMenu(self):
        while True:
            self.mostrarMenu()
            op= input("Seleccion alguna opción: ")
            os.system("cls")
            ejecutar= self.__elecciones.get(op)
            if ejecutar:
                ejecutar()
            else: 
                print("Opcion no valida, vuelva a intentarlo")
                os.system("pause")
            
    def opcion1(self):
        print("1. Calcular unión entre dos conjuntos")
        print()
        union= self.__conjunto1 + self.__conjunto2
        print("La unión de los conjuntos es: ")
        for e in union:
            print(e)   
        os.system("pause")         
           
    def opcion2(self):
        print("2. Calcular diferencia entre dos conjuntos")
        print()
        diferencia= self.__conjunto1 - self.__conjunto2
        print("La diferencia de los conjuntos es: ")
        for e in diferencia:
            print(e)
        os.system("pause")
    
    def opcion3(self):
        print("3. Verificar si los conjuntos son iguales")
        print()
        if self.__conjunto1 == self.__conjunto2:
            print("Ambos conjuntos son iguales")
        else: print("Los conjuntos no son iguales")
        os.system("pause")
    
    def salir(self):
        sys.exit(0)