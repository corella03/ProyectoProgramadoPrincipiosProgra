import ClassMenu.AdministrativeMenu
import ClassTypes.Administrator
dataAdmin = ClassTypes.Administrator.admin("alonso","123")
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
    idEntry = input("Digite Usuario")
    passwordEntry = input("Digite Contra")
    if idEntry == dataAdmin.id and passwordEntry == dataAdmin.password:
        ClassMenu.AdministrativeMenu.ChooseOption()
    else:
        print("Usuario o Contraseña Incorreta")
DataManager()