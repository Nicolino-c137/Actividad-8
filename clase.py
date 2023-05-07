class Conjunto:
    __conjunto= None
    
    def __init__(self,elementos):
        self.__conjunto= set(elementos)        
        
    def __add__(self,otro):
        nuevo_conj= self.__conjunto.union(otro.__conjunto)
        return nuevo_conj
    
    def __sub__(self,otro):
        nuevo_conj= self.__conjunto.difference(otro.__conjunto)
        return nuevo_conj
    
    def __eq__(self,otro):
        return self.__conjunto == otro
    
    