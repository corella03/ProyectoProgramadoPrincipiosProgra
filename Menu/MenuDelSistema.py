
#
def menu():
    print("\nSelecciona una opción")
    print("\t1 - Modo Administrador")
    print("\t2 - Modo Usuario")
    print("\t0 - Salir")
def escogerOpciones():
    while True:
        # Llamamos al Menú
        menu()
        # Solicitamos al usuario ingresar una Opción
        opcionesMenu = input("Ingrese un número del Menú")
        if opcionesMenu == "1":
            import Administrador.Login
            id,contra = Administrador.Login.DatosAdministrador()
            Administrador.Login.Login(id, contra)
            input("\npulsa una tecla para continuar")
        elif opcionesMenu == "2":
            print("")
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")
        elif opcionesMenu == "4":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")
escogerOpciones()