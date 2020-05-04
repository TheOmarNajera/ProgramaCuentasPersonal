#Llamando a las clases y funciones
from ClassFunction import Gastos
from ClassFunction import limpiar_pantalla
#Definiendo el Main()
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