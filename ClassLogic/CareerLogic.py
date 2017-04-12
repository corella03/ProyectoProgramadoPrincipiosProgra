import pickle
from ClassTypes.Career import *
from pathlib import Path
from ClassTypes.Career import Career
def GetCareerList() :
    myCareerFile = Path ("..\Files\CareerFile.pickle")
    if myCareerFile.is_file():
        with open("..\Files\CareerFile.pickle", "rb") as careerFile:
            careerList = pickle._load(careerFile)
        return careerList
    return[]
def SetCareerList(careerList):
    with open("..\Files\CareerFile.pickle", "wb") as careerFile:
        pickle._dump(careerList, careerFile)
def AddCareer():
    nameEntry = input("Ingrese el Nombre de la Carerra: ")
    codeEntry = input("Ingrese el Código de la Carrera: ")
    newCareer = Career (nameEntry, codeEntry)
    careerList = GetCareerList()
    careerList.append(newCareer)
    SetCareerList(careerList)
def DeleteCareer():
    careerNumber = 0
    careerList= GetCareerList()
    for career in careerList:
        careerNumber = careerNumber + 1
        print("Número de Carrera: ", careerNumber - 1, " Name: ", career.name, " Código: ", career.code)
    enterCareerPosition= int (input("\nIngrese la posición de la Carrera que quiera Eliminar :"))
    careerList.remove(careerList[enterCareerPosition])
    SetCareerList(careerList)
def ShowCareerList():
    careerNumber = 0
    careerList = GetCareerList()
    for career in careerList:
        careerNumber = careerNumber + 1
        print("Número de Carrera: ", careerNumber - 1, " Name: ", career.name, " Código: ", career.code," Cursos de la Carrera: ",
              career.courseList)
def ModifyCareer():
    enterCareerPosition= int(input("\nIngrese la Carrera que quiere Modificar: "))
    careerList= GetCareerList()
    for i in range (len(careerList)):
        if i == enterCareerPosition:
            while True :
                print(" Modificar Nombre de la Carrera","\n",
                      "Modificar Código de la Carrerra", "\n",
                      "SALIR. ")
                optionsEntry= input(" Ingrese una Opcion: ")
                if optionsEntry != "0" :
                    if optionsEntry == "1" :
                        careerList[i].career.name = input("Ingrese un nuevo Nombre: ")
                    elif optionsEntry == "2" :
                        careerList [i].career.code = input("Ingrese un nuevo Código: ")
                    else:
                        print("No has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes")
                else:
                    break
                print("Nombre: ",careerList[i].name," Código: ", careerList[i].code)
    else:
        print("La posicion de la Carrera no existe.")
    SetCareerList(careerList)
def CareerMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Agregar Carrera.\n"
          "\t2.. Eliminar Carrera.\n"
          "\t3.. Ver Carrera.\n"
          "\t4.. Modificar Carrera.\n"
          "\t0.. Volver al Menú Administrativo.")
def CareerMenuOptions():
    while True:
        CareerMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddCareer()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeleteCareer()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "3" :
            ShowCareerList()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "4" :
            ModifyCareer()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "0" :
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")