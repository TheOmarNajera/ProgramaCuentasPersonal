class Gastos:    
    def __init__(self, ID, Fecha, Movimiento, Monto):
        self.__ID, self.__Fecha, self.__Movimiento, self.__Monto = ID, Fecha, Movimiento, Monto
#Property
    @property
    def ID(self, ID):
        return self.__ID
    def Fecha(self, Fecha):
        return self.__Fecha
    def Movimiento(self, Movimiento):
        return self.__Movimiento
    def Monto(self, Monto):
        return self.__Monto
    
    def __repr__(self):
        return f'ID: {self.__ID}   |   Fecha: {self.__Fecha}   |   Movimiento: {self.__Movimiento}   |   Monto: ${self.__Monto}'


from os import system,name
def limpiar_pantalla():
    if name == "nt":
        system("cls")
    else:
        system("clear")