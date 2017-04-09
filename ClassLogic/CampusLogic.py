from ClassTypes.Campus import *
campusList = []
def AddCampus():
    nameEntry = input("Ingrese el nombre del Recinto:")
    addressEntry = input("Ingrese la dirección del Recinto:")
    codeEntry = input("Ingrese el código del Recinto:")
    newCampus = Campus(nameEntry,addressEntry,codeEntry)
    campusList.append(newCampus)
def DeleteCampus():
    campusNumber = 0
    for campus in campusList:
        campusNumber = campusNumber + 1
        print("Número de Campus: ", campusNumber, " Nombre: ", campus.campusName, " Dirección: ", campus.campusAddress,
              " Código: ", campus.campusCode)
    enterCampusPosition = int(input("Ingrese la posición del Recinto que quiera eliminar:"))
    campusList.remove(campusList[enterCampusPosition])
def ShowCampusList():
    campusNumber = 0
    for campus in campusList:
        campusNumber = campusNumber + 1
        print("Número de Recinto: ",campusNumber," Nombre: ", campus.campusName," Dirección: ",campus.campusAddress ,
              " Código: ",campus.campusCode)
def ModifyCampus():
    enterCampusPosition = int(input("Ingrese el numero del Recinto que quiera Modificar:"))
    for i in range(len(campusList)):
        if campusList[i] == campusList[enterCampusPosition]:
            while True:
                print("1- Para modificar el Nombre:\n"
                      "2- Para modificar la  Dirección:\n"
                      "3- Para modificar el Código:\n"
                      "0- salir:")
                optionsEntry = input("Ingrese la Opción a Escoger")
                if optionsEntry != "0":
                    for campus in campusList:
                        if optionsEntry == "1":
                            campus.campusName = input("Ingrese nuevo nombre")
                        elif optionsEntry == "2":
                            campus.campusAddress = input("Ingrese la nueva Dirección")
                        elif optionsEntry == "3":
                            campus.campusCode = input("Ingrese nuevo Código")
                        else:
                            input("No has pulsado ninguna opción correcta...\n"
                                  "Presione enter Para volver al Menú")
                else:
                    break
                print("\033[;34mNombre:", campus.campusName + "\033[;23m", "\033[;34mDirección:", campus.campusAddress,
                      "\033[;34mCódigo:", campus.campusCode)
def CreateFile():
    campusFile = open("..\Files\Campus.txt", "w")
    campusFile.close()
CreateFile()
def WriteFile():
    campusFile = open("..\Files\Campus.txt", "a")
    campusFile.write(str((campusList)))
    campusFile.close()
WriteFile()
def ReadAsList():
    campusFile = open("..\Files\campus.txt", "r")
    lineas = campusFile.readlines()
    print(lineas)
    campusFile.close()
def CampusMenu():
    print("\033[;34m" + "\nSelecciona una opción\n"
     "\t1 - Agregar Recinto\n"
     "\t2 - Eliminar Recinto\n"
     "\t3 - Ver Recinto\n"
     "\t4 - Modificar Recinto\n"
     "\t0 - Volver al Menú Administrativo" + "\033[;23m")
def CampusMenuOptions():
    while True:
        CampusMenu()
        optionsEntry = input("Ingrese la Opción a Escoger")
        if optionsEntry == "1":
            AddCampus()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "2":
            DeleteCampus()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "3":
            ShowCampusList()
        elif optionsEntry == "4":
            ModifyCampus()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")