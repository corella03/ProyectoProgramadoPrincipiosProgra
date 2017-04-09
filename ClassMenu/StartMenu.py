from ClassMenu.AdministrativeMenu import *
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
    idEntry = input("Digite Usuario\n--->")
    passwordEntry = input("Digite Contra\n--->")
    if idEntry == dataAdmin.id and passwordEntry == dataAdmin.password:
        ChooseOption()
    else:
        print("Usuario o Contraseña Incorreta")
DataManager()