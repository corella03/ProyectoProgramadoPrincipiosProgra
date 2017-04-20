import pickle
from pathlib import Path
from ClassTypes.ClassSchedule import *
def GetClassScheduleList():
    myClassScheduleFile = Path("..\Files\ClassScheduleFile.pickle")
    if myClassScheduleFile.is_file():
        with open("..\Files\ClassScheduleFile.pickle", "rb") as classScheduleFile:
            classScheduleList = pickle._load(classScheduleFile)
        return classScheduleList
    return []
def SetClassScheduleList(classScheduleList):
    with open("..\Files\ClassScheduleFile.pickle", "wb") as classScheduleFile:
        pickle._dump(classScheduleList, classScheduleFile)
def AddClassSchedule():
    classScheduleList = GetClassScheduleList()
    typeEntry = input("Ingrese el Tipo de Horario: ")
    allTypeClassSchedule = []
    sorterClassScheduleList = sorted(classScheduleList, key=lambda classSchedule: classSchedule.scheduleType)
    for type in sorterClassScheduleList:
        allTypeClassSchedule.append(type.scheduleType)
    for i in range(len(allTypeClassSchedule)):
        if allTypeClassSchedule[i] == typeEntry:
            print("El Horario ya existe")
            break
    else:
        #Si es tarde validar Horas con Ifs
        startOfScheduleEntry = input("Ingrese la Hora de Inicio: ")
        endOfScheduleEntry = input("Ingrese la Horas de Salida: ")
        newClassSchedule = ClassSchedule(typeEntry,startOfScheduleEntry,endOfScheduleEntry)
        classScheduleList.append(newClassSchedule)
        SetClassScheduleList(classScheduleList)
def DeleteClassSchedule():
    classScheduleNumber = 0
    classScheduleList = GetClassScheduleList()
    for classSchedule in classScheduleList:
        classScheduleNumber = classScheduleNumber + 1
        print("Número de Horario: ",classScheduleNumber - 1, " Tipo de Horario: ",classSchedule.scheduleType,
              " Hora de Inicio: ",classSchedule.startOfSchedule," Hora de Salida: ",classSchedule.endOfSchedule)
    enterCampusPosition = int(input("\nIngrese la posición del Horario que quiera eliminar: "))
    classScheduleList.remove( classScheduleList[enterCampusPosition])
    SetClassScheduleList(classScheduleList)
def ShowClassSchedule():
    classScheduleNumber = 0
    classScheduleList = GetClassScheduleList()
    for classSchedule in classScheduleList:
        classScheduleNumber = classScheduleNumber + 1
        print("Número de Horario: ", classScheduleNumber - 1, " Tipo de Horario: ", classSchedule.scheduleType,
              " Hora de Inicio: ", classSchedule.startOfSchedule, " Hora de Salida: ", classSchedule.endOfSchedule)
def ModifyClassSchedule():
    enterClassSchedulePosition = int(input("\nIngrese el numero del Horario que quiera Modificar: "))
    classScheduleList = GetClassScheduleList()
    for i in range(len( classScheduleList)):
        if i == enterClassSchedulePosition:
            while True:
                print("\t1...Modificar Tipo de Horario.", "\n",
                      "\t2...Modifciar Hora de Inicio.", "\n",
                      "\t3...Modificar Hora de Salida.", "\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        classScheduleList[i].scheduleType = input("Ingrese nuevo Tipo: ")
                    elif optionsEntry == "2":
                        classScheduleList[i].startOfSchedule = input("Ingrese nueva Hora de Inicio: ")
                    elif optionsEntry == "3":
                        classScheduleList[i].endOfSchedule = input("Ingrese nueva Hora Salida: ")
                    else:
                        input("No has pulsado ninguna opción correcta...\n"
                                  "Presione una tecla para volver a las Opciones.")
                else:
                    break
                print("Nombre: ",classScheduleList[i].scheduleType," Dirección: ",classScheduleList[i].startOfSchedule,
                      " Código: ",classScheduleList[i].endOfSchedule)
    else:
        print("La posición del Horario no existe.")
    SetClassScheduleList(classScheduleList)
def ClassScheduleMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Agregar Horario.\n"
          "\t2.. Eliminar Horario.\n"
          "\t3.. Ver Horarios.\n"
          "\t4.. Modificar Horario.\n"
          "\t0.. Volver al Menú Administrativo.")
def  ClassScheduleMenuOptions():
    while True:
        ClassScheduleMenu()
        optionsEntry = input("\nIngrese la Opción a Escoger: ")
        if optionsEntry == "1":
            AddClassSchedule()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteClassSchedule()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowClassSchedule()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "4":
            ModifyClassSchedule()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")