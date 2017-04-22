import pickle
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
    careerList = GetCareerList()
    codeEntry = input("Ingrese el Código de la Carrera: ")
    codeEntry = codeEntry.upper()
    allCodeToCareer = []
    sorterCareerList = sorted(careerList, key=lambda career: career.code)
    for codeCareer in sorterCareerList:
        allCodeToCareer.append(codeCareer.code)
    for i in range(len(allCodeToCareer)):
        if allCodeToCareer[i] == codeEntry:
            print("Esta Carrera ya Existe.")
            break
    else:
        nameEntry = input("Ingrese el Nombre de la Carerra: ")
        newCareer = Career(nameEntry, codeEntry)
        careerList.append(newCareer)
        SetCareerList(careerList)
def DeleteCareer():
    ShowCareerList()
    careerList= GetCareerList()
    enterCareerPosition= int (input("\nIngrese la posición de la Carrera que quiera Eliminar: "))
    careerList.remove(careerList[enterCareerPosition])
    SetCareerList(careerList)
def ShowCareerList():
#Preguntar si tiene que imprimir Lista de Estudiantes, Docentes y Cursos.
    careerNumber = 0
    careerList = GetCareerList()
    for career in careerList:
        careerNumber = careerNumber + 1
        print("Número de Carrera: ", careerNumber - 1, " **Nombre: ", career.name, " **Código: ", career.code)
def ModifyCareer():
    ShowCareerList()
    enterCareerPosition= int(input("\nIngrese la Carrera que quiere Modificar: "))
    careerList = GetCareerList()
    careerExist = False
    for i in range (len(careerList)):
        if i == enterCareerPosition:
            careerExist = True
            while True :
                print("\t1...Modificar Nombre de la Carrera.\n",
                      "\t2...Modificar Código de la Carrerra.\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                if optionsEntry != "0" :
                    if optionsEntry == "1" :
                        careerList[i].name = input("Ingrese un nuevo Nombre: ")
                    elif optionsEntry == "2" :
                        careerList[i].code = input("Ingrese un nuevo Código: ")
                        careerList[i].code = careerList[i].code.upper()
                    else:
                        input("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
    if not careerExist:
        print("La Carrera NO Existe.")
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
        optionsEntry = input("\nIngrese la opción a Escoger: ")
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