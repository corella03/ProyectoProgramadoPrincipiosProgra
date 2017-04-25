from ClassLogic.AdministratorLogic import *
from ClassMenu.SystemMenu import *
from ClassMenu.OperatingMenu import *
from ClassMenu.ReportsMenu import *
def AdminMenu():
    print("\nBienvenido Señor(a)\n"
    "Seleccione una Opción.\n"
    "\t1...Cambiar contraseña.\n"
    "\t2...Menú Administrativo.\n"
    "\t3...Menú Operativo.\n"
    "\t4...Menú de Reportes.\n"
    "\t0...Volver al Menú del Sistema.\n")
def ChooseOption():
    while True:
        # Llamamos al Menú
        AdminMenu()
        # Solicitamos al usuario ingresar una Opción
        AdminMenuOptions = input("Ingrese un número del Menú: ")
        if AdminMenuOptions == "1":
            ChangePassword()
            input("\nPulsa una tecla para continuar.")
        elif AdminMenuOptions == "2":
            MenuOptions()
            input("\nPulsa una tecla para continuar.")
        elif AdminMenuOptions == "3":
            OperatingMenuOptions()
            input("\nPulsa una tecla para continuar.")
        elif AdminMenuOptions == "4":
            ReportsMenuOptions()
            input("\nPulsa una tecla para continuar.")
        elif AdminMenuOptions == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")