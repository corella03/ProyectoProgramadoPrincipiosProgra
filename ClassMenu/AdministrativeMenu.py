import ClassLogic.AdministratorLogic
import ClassMenu.SystemMenu
import sys
def AdminMenu():
    print("\033[;34m" + "\nBienvenido Señor(a) \n"
    "Seleccione una Opción\n"
    "\t1 - Cambiar contraseña\n"
    "\t2 - Menú Administrativo\n"
    "\t3 - Menú Operativo\n"
    "\t4 - Menú de Reportes\n"
    "\t0 - Salir\n" + "\033[;23m")
def ChooseOption():
    while True:
        # Llamamos al Menú
        AdminMenu()
        # Solicitamos al usuario ingresar una Opción
        MenuOptions = input("Ingrese un número del Menú")
        if MenuOptions == "1":
            ClassLogic.AdministratorLogic.ChangePassword()
            input("\npulsa una tecla para continuar")
        elif MenuOptions == "2":
            ClassMenu.SystemMenu.MenuOptions()
            input("\npulsa una tecla para continuar")
        elif MenuOptions == "0":
            sys.exit()
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")
            print ("....")