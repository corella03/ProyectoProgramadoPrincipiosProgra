def menu():
    print("\033[;34m"+"\nSelecciona una opción\n"
          "\033[;34m" +"\t1 - Modo Administrador\n"
          "\033[;34m" +"\t2 - Modo Usuario\n"
          "\033[;34m" +"\t0 - Salir"+"\033[;23m")
def escogerOpciones():
    while True:
        # Llamamos al Menú
        menu()
        # Solicitamos al usuario ingresar una Opción
        opcionesMenu = input("Ingrese un número del Menú")
        if opcionesMenu == "1":
            import Logica.Administrador
            Logica.Administrador.Administrador().DatosAdministrador()
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
            print ("....")
escogerOpciones()
