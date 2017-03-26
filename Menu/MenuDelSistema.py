def menu():
    print("\nSelecciona una opción\n"
          "\t1 - Modo Administrador\n"
          "\t2 - Modo Usuario\n"
          "\t0 - Salir")
def menuAdmin():
    print("\nSelecciona una opción\n"
          "\t1 - Cambiar contra\n"
          "\t2 - Salir\n")
def escogerOpciones():
    while True:
        # Llamamos al Menú
        menu()
        # Solicitamos al usuario ingresar una Opción
        opcionesMenu = input("Ingrese un número del Menú")
        if opcionesMenu == "1":
            import Administrador.Login
            Administrador.Login.Administrador().DatosAdministrador()
            input("\npulsa una tecla para continuar")
        elif opcionesMenu == "2":
            print("")
            input("\npulsa una tecla para continuar")
        elif opcionesMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")
escogerOpciones()