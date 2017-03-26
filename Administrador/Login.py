class Administrador:
    def __init__(self):
        self.ID = "alonso"
        self.contraseña = "123"
    def  DatosAdministrador(self):
        ingresoId = input("Digite Usuario")
        ingresoContra = input("Digite Contra")
        while True:
            if ingresoId == self.ID and ingresoContra == self.contraseña:
                print("\033[;34m" +"Bienvenido ADMIN \n")
                print("\033[;34m" + "\nSelecciona una opción\n"
                    "\t1 - Cambiar contra\n"
                    "\t0 - Salir\n" + "\033[;23m")
                while True:
                    opcionesAdministrador = input("Ingrese opcion Admin")
                    if opcionesAdministrador == "1":
                        ingresoNuevaContraseña = input("Ingrese la nueva Contraseña")
                        self.contraseña = ingresoNuevaContraseña
                        input("Haz cambiado de Contraseña\n"
                              "pulsa una tecla para continuar")
                    elif opcionesAdministrador == "0":
                        break
                    else:
                        print("")
                        input("No has pulsado ninguna opción correcta...\n"
                              "Presione enter Para volver al Menú")
            elif opcionesAdministrador == "0":
                break
            else:
                print("NO ERES BIENVENIDO")
#x = Administrador()
#x.DatosAdministrador()