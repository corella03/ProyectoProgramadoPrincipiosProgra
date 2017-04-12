import pickle
from ClassTypes.ClassRooms import *
from pathlib import Path
def GetClassRoomsList() :
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
    codeEntry= input("Ingrese el Código del Aula: ")
    campusBelongsEntry = input("Ingrese el Campus en el que Pertenece: ")
    newClassRooms= Classrooms (campusBelongsEntry, codeEntry)
    classRoomsList= GetClassRoomsList()
    classRoomsList.append(newClassRooms)
    SetClassRoomsList(classRoomsList)
def DeleteClassRooms():
    classRoomsNumber = 0
    classRoomsList= GetClassRoomsList()
    for classRooms in classRoomsList:
        classRoomsNumber = classRoomsNumber + 1
        print("Número de Aula: ", classRoomsNumber - 1, " Código ", classRooms.classroomsCode,
              " Recinto donde se ubica el Aula: ", classRooms.classroomsCampusBelongs)
    enterClassRoomsPosition= int (input("\nIngrese la posición del Aula que quiera Eliminar :"))
    classRoomsList.remove(classRoomsList[enterClassRoomsPosition])
    SetClassRoomsList(classRoomsList)
def ShowCareerList():
    classRoomsNumber = 0
    classRoomsList = GetClassRoomsList()
    for classRooms in classRoomsList:
        classRoomsNumber = classRoomsNumber + 1
        print("Número de Aula: ", classRoomsNumber - 1, " Código ", classRooms.classroomsCode,
              " Recinto donde se ubica el Aula: ", classRooms.classroomsCampusBelongs)
def ModifyClassRooms():
    enterClassRoomsPosition= int(input("\nIngrese el Aula que quiere Modificar: "))
    classRoomsList= GetClassRoomsList()
    for i in range (len(classRoomsList)):
        if i == enterClassRoomsPosition:
            while True :
                print(" Modificar Código del Aula","\n",
                      "Modificar Lugar donde se encuentra el Aula ", "\n",
                      "SALIR. ")
                optionsEntry= input(" Ingrese una Opcion: ")
                if optionsEntry != "0" :
                    if optionsEntry == "1" :
                        classRoomsList[i].classRooms.classroomsCode = input("Ingrese un Nuevo Código: ")
                    elif optionsEntry == "2" :
                        classRoomsList [i].classRooms.classroomsCampusBelongs =input("Ingrese un Nuevo Recinto del aula: ")
                    else:
                        print("No has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes")
                else:
                    break
                print("Código: ",classRoomsList[i].classroomsCode," Reciento que pertenece: ",
                      classRoomsList[i].classroomsCampusBelongs )
        else:
            print("La posicion de la Carrera no existe.")
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
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddClassRooms()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeleteClassRooms()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "3" :
            ShowCareerList()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "4" :
            ModifyClassRooms()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "0" :
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
ClassRoomsMenuOptions()