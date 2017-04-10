import pickle
from pathlib import Path
from ClassTypes.Campus import *
def GetCampusList():
    myCampusFile = Path("..\Files\CampusFile.pickle")
    if myCampusFile.is_file():
        with open("..\Files\CampusFile.pickle", "rb") as campusFile:
            campusList = pickle._load(campusFile)
        return campusList
    return []
def SetCampusList(campusList):
    with open("..\Files\CampusFile.pickle", "wb") as campusFile:
        pickle._dump(campusList, campusFile)
def AddCampus():
    nameEntry = input("Ingrese el Nombre del Recinto: ")
    addressEntry = input("Ingrese la Dirección del Recinto: ")
    codeEntry = input("Ingrese el Código del Recinto: ")
    newCampus = Campus(nameEntry,addressEntry,codeEntry)
    campusList = GetCampusList()
    campusList.append(newCampus)
    SetCampusList(campusList)
def DeleteCampus():
    campusNumber = 0
    campusList = GetCampusList()
    for campus in campusList:
        campusNumber = campusNumber + 1
        print("Número de Recinto: ",campusNumber - 1, " Nombre: ",campus.campusName, " Dirección: ",campus.campusAddress,
              " Código: ",campus.campusCode)
    enterCampusPosition = int(input("\nIngrese la posición del Recinto que quiera eliminar: "))
    campusList.remove(campusList[enterCampusPosition])
    SetCampusList(campusList)
def ShowCampusList():
    campusNumber = 0
    campusList = GetCampusList()
    for campus in campusList:
        campusNumber = campusNumber + 1
        print("Número de Recinto: ",campusNumber - 1," Nombre: ",campus.campusName," Dirección: ",campus.campusAddress ,
              " Código: ",campus.campusCode)
def ModifyCampus():
    enterCampusPosition = int(input("\nIngrese el numero del Recinto que quiera Modificar: "))
    campusList = GetCampusList()
    for i in range(len(campusList)):
        if i == enterCampusPosition:
            while True:
                print("\t1...Modificar Nombre del Recinto.", "\n",
                      "\t2...Modifciar Dirección del Recinto.", "\n",
                      "\t3...Modificar Código del Recinto.", "\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        campusList[i].campusName = input("Ingrese nuevo Nombre: ")
                    elif optionsEntry == "2":
                        campusList[i].campusAddress = input("Ingrese la nueva Dirección: ")
                    elif optionsEntry == "3":
                        campusList[i].campusCode = input("Ingrese el nuevo Código: ")
                    else:
                        input("No has pulsado ninguna opción correcta...\n"
                                  "Presione una tecla para volver a las Opciones.")
                else:
                    break
                print("Nombre: ",campusList[i].campusName," Dirección: ",campusList[i].campusAddress,
                      " Código: ",campusList[i].campusCode)
    else:
        print("La posición del Recinto no existe.")
    SetCampusList(campusList)
def CampusMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Agregar Recinto.\n"
          "\t2.. Eliminar Recinto.\n"
          "\t3.. Ver Recintos.\n"
          "\t4.. Modificar Recinto.\n"
          "\t0.. Volver al Menú Administrativo.")
def CampusMenuOptions():
    while True:
        CampusMenu()
        optionsEntry = input("\nIngrese la Opción a Escoger: ")
        if optionsEntry == "1":
            AddCampus()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteCampus()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowCampusList()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "4":
            ModifyCampus()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")