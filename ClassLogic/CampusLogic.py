#Imports
from ClassTypes.Campus import *
from ClassLogic.CourseLogic import *
import pickle
from pathlib import Path
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
    campusList = GetCampusList()
    codeEntry = input("Ingrese el Código del Recinto: ")
    codeEntry = codeEntry.upper()
    allCodeToCampus = []
    sorterCampusList = sorted(campusList, key=lambda campus: campus.campusCode)
    for code in sorterCampusList:
        allCodeToCampus.append(code.campusCode)
    for j in range(len(allCodeToCampus)):
        if allCodeToCampus[j] == codeEntry:
            print("El Recinto ya Existe.")
            break
    else:
        nameEntry = input("Ingrese el Nombre del Recinto: ")
        addressEntry = input("Ingrese la Dirección del Recinto: ")
        newCampus = Campus(nameEntry,addressEntry,codeEntry)
        campusList = GetCampusList()
        campusList.append(newCampus)
        SetCampusList(campusList)
def DeleteCampus():
    #Validar si el numero ingresado es mayor que el del indice
    campusList = GetCampusList()
    courseList = GetCourseList()
    ShowCampusList()
    enterCampusPosition = input("\nIngrese la posición del Recinto que quiera eliminar: ")
    if not enterCampusPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for course in courseList:
        if campusList[int(enterCampusPosition)].campusCode in course.campusList:
            course.campusList.remove(campusList[int(enterCampusPosition)].campusCode)
    if campusList[int(enterCampusPosition)] in campusList:
        campusList.remove(campusList[int(enterCampusPosition)])
    SetCampusList(campusList)
    SetCourseList(courseList)
def ShowCampusList():
    campusNumber = 0
    campusList = GetCampusList()
    for campus in campusList:
        campusNumber = campusNumber + 1
        print("Número de Recinto: ",campusNumber - 1," **Nombre: ",campus.campusName," **Dirección: ",campus.campusAddress ,
              " **Código: ",campus.campusCode)
def ModifyCampus():
    ShowCampusList()
    enterCampusPosition = int(input("\nIngrese el numero del Recinto que quiera Modificar: "))
    campusList = GetCampusList()
    campusExist = False
    for i in range(len(campusList)):
        if i == enterCampusPosition:
            campusExist = True
            while True:
                print("\t1...Modificar Nombre del Recinto.\n",
                      "\t2...Modifciar Dirección del Recinto.\n",
                      "\t3...Modificar Código del Recinto.\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        campusList[i].campusName = input("Ingrese nuevo Nombre: ")
                    elif optionsEntry == "2":
                        campusList[i].campusAddress = input("Ingrese la nueva Dirección: ")
                    elif optionsEntry == "3":
                        campusList[i].campusCode = input("Ingrese el nuevo Código: ")
                        campusList[i].campusCode = campusList[i].campusCode.upper()
                    else:
                        input("\nNo has pulsado ninguna opción correcta...\n"
                                  "Presione una tecla para volver a las Opciones.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
    if not campusExist:
        print("El Recinto NO Existe.")
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