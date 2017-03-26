def DatosAdministrador():
    ID = "alonso"
    contraseña = "123"
    return ID,contraseña
def Login(ID, contraseña):
    ingresoId = input("Digite Usuario")
    ingresoContra = input("Digite Contra")
    if ingresoId == ID and ingresoContra == contraseña:
        print("Bienvenido Mae")
    else:
        print("NO ERES BIENVENIDO")
id,contra = DatosAdministrador()
Login(id,contra)