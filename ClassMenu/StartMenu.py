from ClassMenu.AdministrativeMenu import *
from ClassLogic.AdministratorLogic import *
import getpass
#passwordEntry = input(getpass.getpass("Digite Contra\n--->"))
def Menu():
    print("==================================\n"
          " Gestion de Elementons Principales\n"
          " Respecto a la Educación de la UTN\n"
          "==================================\n"
          "             Ingrese              \n"
          "              * *                 \n"
          "              * *                 \n"
          "            *** ***               \n"
          "              ***                 \n"
          "               *                  \n")

def DataManager():
    Menu()
    idEntry = input("Digite Usuario\n---> ")
    passwordEntry = input("Digite Contra\n---> ")
    administratorLogin = GetAdministratorLogin()
    if idEntry == administratorLogin.id and passwordEntry == administratorLogin.password:
        SetAdministratorLogin(administratorLogin)
        ChooseOption()
    else:
        print("Usuario o Contraseña Incorreta.")
DataManager()