class Gastos:    
    def __init__(self, ID, Fecha, Movimiento, Monto):
        self.__ID, self.__Fecha, self.__Movimiento, self.__Monto = ID, Fecha, Movimiento, Monto

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
        return f'ID: {self.__ID}   |   Fecha: {self.__Fecha}   |   Movimiento: {self.__Movimiento}   |   Monto: {self.__Monto}'

from os import system,name
def limpiar_pantalla():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def main():
    ListaMovimiento = []
    OpUsuario = 0
    ID = 0
    total = 0
    while OpUsuario != 3:
        OpUsuario = input("Programa de cuentas\n¿Qué desea hacer?\n1.- Consultar Movimientos\n2.- Realizar nuevo movimiento\n3.- Salir\n")
        limpiar_pantalla()
        if OpUsuario == "2":
            ID = ID + 1
            Fecha, Movimiento = input("Fecha: "), input("Movimiento: ")
            Monto = int(input("Monto: $"))
            Mov = Gastos(ID, Fecha, Movimiento, Monto)
            ListaMovimiento.append(Mov)
            total = total + Monto
            limpiar_pantalla()

        elif OpUsuario == "1":
            for objeto in ListaMovimiento:
                print(objeto)
            print(f'Total: ${total}')
        elif OpUsuario == "3":
            print("Proceso Terminado")
            OpUsuario = int(OpUsuario)
        else:
            print("Opcion Inválida")

main()