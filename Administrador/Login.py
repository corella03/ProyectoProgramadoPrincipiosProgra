class Administrador:
    def __init__(self):
        self.ID = "alonso"
        self.contraseña = "123"
    def lol (self):
        print("ok")
    def  DatosAdministrador(self):
        while True:
            ingresoId = input("Digite Usuario")
            ingresoContra = input("Digite Contra")
            if ingresoId == self.ID and ingresoContra == self.contraseña:
                print("Bienvenido ADMIN \n")
                print("\nSelecciona una opción\n"
                      "\t1 - Cambiar contra\n"
                      "\t0 - Salir\n")
                opcionesAdministrador = input("Ingrese opcion Admin")
                if opcionesAdministrador == "1":
                    ingresoNuevaContraseña = input("Ingrese la nueva Contraseña")
                    self.contraseña = ingresoNuevaContraseña
                    input("\npulsa una tecla para continuar")
                elif opcionesAdministrador == "0":
                    break
                else:
                    print("")
                    input("No has pulsado ninguna opción correcta...\n"
                          "Presione enter Para volver al Menú")
            else:
                print("NO ERES BIENVENIDO")

#x = Administrador()
#x.DatosAdministrador()