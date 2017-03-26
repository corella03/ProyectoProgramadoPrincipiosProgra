class Administrador:
    def __init__(self):
        self.ID = "alonso"
        self.contraseña = "123"
    def  DatosAdministrador(self):
        ingresoId = input("Digite Usuario")
        ingresoContra = input("Digite Contra")
        if ingresoId == self.ID and ingresoContra == self.contraseña:
            print("Bienvenido ADMIN \n")
        else:
            print("NO ERES BIENVENIDO")
    def cambioContraseña(self,):
        ingresoNuevaContraseña = input("Ingrese la nueva Contraseña")
        self.contraseña = ingresoNuevaContraseña