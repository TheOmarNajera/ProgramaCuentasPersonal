#Llamando a las clases y funciones
from ClassFunction import Gastos
from ClassFunction import limpiar_pantalla
#Definiendo el Main()
def main():
    ListaMovimiento = []
    OpUsuario = 0
    ID = 0
    total = 0
    
    while True:
        while True:
            #Validacion de datos
            try:    
                OpUsuario = int(input("Programa de cuentas\n¿Qué desea hacer?\n1.- Consultar Movimientos\n2.- Realizar nuevo movimiento\n3.- Salir\n"))
                limpiar_pantalla()
                break
            except ValueError:
                limpiar_pantalla()
                print("Opción no válida. Intente de nuevo.")
        
        if OpUsuario <= 0 or OpUsuario >= 4:
                    print("Opción no válida. Intente de nuevo.")
        
        elif OpUsuario == 2:
            ID = ID + 1
            Fecha, Movimiento = input("Fecha: "), input("Movimiento: ")
            
            while True:
                #validacion de monto
                try:
                    Monto = int(input("Monto: $"))
                    break
                except ValueError:
                    print("Dato no válido. Intente de nuevo.")

            Mov = Gastos(ID, Fecha, Movimiento, Monto)
            ListaMovimiento.append(Mov)
            total = total + Monto
            limpiar_pantalla()
        

        elif OpUsuario == 1:
            for objeto in ListaMovimiento:
                print(objeto)
            print(f'Total: ${total}')
        
        else:
            print("Proceso Terminado")
            break