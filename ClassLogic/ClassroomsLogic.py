import pickle
from ClassTypes.ClassRooms import *
from pathlib import Path
def GetClassRoomsList():
    myClassRoomsFile = Path ("..\Files\ClassRoomsFile.pickle")
    if myClassRoomsFile.is_file():
        with open("..\Files\ClassRoomsFile.pickle", "rb") as classRoomsFile:
            classRoomsList = pickle._load(classRoomsFile)
        return classRoomsList
    return[]
def SetClassRoomsList(classRoomsList):
    with open("..\Files\ClassRoomsFile.pickle", "wb") as classRoomsFile:
        pickle._dump(classRoomsList, classRoomsFile)
def AddClassRooms():
    classRoomsList = GetClassRoomsList()
    codeEntry = input("Ingrese el Código del Aula: ")
    allCodeToClassRooms = []
    sorterClassRoomsList = sorted(classRoomsList, key=lambda classRooms: classRooms.classRoomsCode)
    for code in sorterClassRoomsList:
       allCodeToClassRooms.append(code.classRoomsCode)
    for i in range(len(allCodeToClassRooms)):
        if allCodeToClassRooms[i] == codeEntry:
            print("La Aula ya Existe.")
            break
    else:
        campusBelongsEntry = input("Ingrese el Campus en el que Pertenece: ")
        newClassRooms = Classrooms(codeEntry,campusBelongsEntry)
        classRoomsList = GetClassRoomsList()
        classRoomsList.append(newClassRooms)
        SetClassRoomsList(classRoomsList)
def DeleteClassRooms():
    ShowCareerList()
    classRoomsList = GetClassRoomsList()
    enterClassRoomsPosition = int(input("\nIngrese la posición del Aula que quiera Eliminar: "))
    classRoomsList.remove(classRoomsList[enterClassRoomsPosition])
    SetClassRoomsList(classRoomsList)
def ShowCareerList():
    classRoomsList = GetClassRoomsList()
    classRoomsNumber = 0
    for classRooms in classRoomsList:
        classRoomsNumber = classRoomsNumber + 1
        print("Número de Aula: ", classRoomsNumber - 1, " **Código: ", classRooms.classRoomsCode,
              " **Recinto donde se ubica el Aula: ", classRooms.classroomsCampusBelongs)
def ModifyClassRooms():
    ShowCareerList()
    enterClassRoomsPosition= int(input("\nIngrese el Aula que quiere Modificar: "))
    classRoomsList= GetClassRoomsList()
    classRoomsExist = False
    for i in range (len(classRoomsList)):
        if i == enterClassRoomsPosition:
            classRoomsExist = True
            while True :
                print("\t1...Modificar Código del Aula.\n",
                      "\t2...Modificar Lugar donde se encuentra el Aula.\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                if optionsEntry != "0" :
                    if optionsEntry == "1":
                        classRoomsList[i].classRoomsCode = input("Ingrese un Nuevo Código: ")
                    elif optionsEntry == "2":
                        classRoomsList[i].classroomsCampusBelongs = input("Ingrese un Nuevo Recinto del aula: ")
                    else:
                        input("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
    if not classRoomsExist:
        print("El Aula NO Existe.")
    SetClassRoomsList(classRoomsList)
def ClassRoomsMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Agregar Aula.\n"
          "\t2.. Eliminar Aula.\n"
          "\t3.. Ver Aulas.\n"
          "\t4.. Modificar Aulas.\n"
          "\t0.. Volver al Menú Administrativo.")
def ClassRoomsMenuOptions():
    while True:
        ClassRoomsMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddClassRooms()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeleteClassRooms()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "3" :
            ShowCareerList()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "4":
            ModifyClassRooms()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "0" :
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")