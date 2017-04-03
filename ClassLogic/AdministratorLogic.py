from ClassTypes.Administrator import *
dataAdmin = Admin("alonso", "123")
def ChangePassword():
    changePasswordEntry = input("Ingrese la nueva contraseña:")
    dataAdmin.password = changePasswordEntry
    print("Tu Contraseña Ha siado Cambiada")
def CreateFile():
    adminFile = open("..\Files\Admin.txt", "w")
    adminFile.close()
CreateFile()
def WriteFile():
    adminFile = open("..\Files\Admin.txt", "a")
    adminFile.write("lol")
    adminFile.close()
WriteFile()
def ReadAsList():
    adminFile = open("..\Files\Admin.txt", "r")
    lineas = adminFile.readlines()
    print(lineas)
    adminFile.close()