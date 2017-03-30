import ClassTypes.Administrator
def ChangePassword():
    dataAdmin = ClassTypes.Administrator.admin("alonso", "123")
    changePasswordEntry = input("Ingrese la nueva contraseña:")
    dataAdmin.password = changePasswordEntry
    print("Tu Contraseña Ha siado Cambiada")