from ClassLogic.AdministratorLogic import *
from ClassMenu.SystemMenu import *
from ClassMenu.OperatingMenu import *
from ClassMenu.ReportsMenu import *
def AdminMenu():
    print("\033[;34m" + "\nBienvenido Señor(a) \n"
    "Seleccione una Opción\n"
    "\t1 - Cambiar contraseña\n"
    "\t2 - Menú Administrativo\n"
    "\t3 - Menú Operativo\n"
    "\t4 - Menú de Reportes\n"
    "\t0 - Volver al Menú del Sistema\n" + "\033[;23m")
def ChooseOption():
    while True:
        # Llamamos al Menú
        AdminMenu()
        # Solicitamos al usuario ingresar una Opción
        AdminMenuOptions = input("Ingrese un número del Menú")
        if AdminMenuOptions == "1":
            ChangePassword()
            input("\npulsa una tecla para continuar")
        elif AdminMenuOptions == "2":
            MenuOptions()
            input("\npulsa una tecla para continuar")
        elif AdminMenuOptions == "3":
            OperatingMenuOptions()
            input("\npulsa una tecla para continuar")
        elif AdminMenuOptions == "4":
            ReportsMenuOptions()
        elif AdminMenuOptions == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")
            print ("....")