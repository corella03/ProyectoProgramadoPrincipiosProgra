import pickle
from pathlib import Path
from ClassTypes.Administrator import *
def GetAdministratorLogin():
    myAdministratorLogin = Path("..\Files\AdministratorFile.pickle")
    if myAdministratorLogin.is_file():
        with open("..\Files\AdministratorFile.pickle", "rb") as administratorFile:
            administratorLogin = pickle._load(administratorFile)
        return administratorLogin
    return[]
def SetAdministratorLogin(administratorLogin):
    with open("..\Files\AdministratorFile.pickle", "wb") as administratorFile:
        pickle._dump(administratorLogin, administratorFile)
def ChangePassword():
    administratorLogin = Admin("karlonso", "123")
    administratorLogin = GetAdministratorLogin()
    changePasswordEntry = input("Ingrese la nueva contraseña:")
    administratorLogin.password = changePasswordEntry
    SetAdministratorLogin(administratorLogin)
    print("Tu Contraseña Ha siado Cambiada")