from ClassTypes.ClassSchedule import *
from ClassLogic.CourseLogic import *
import pickle
from pathlib import Path
allTypeClassSchedule = []
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
    typeEntry = typeEntry.upper()
    sorterClassScheduleList = sorted(classScheduleList, key=lambda classSchedule: classSchedule.scheduleType)
    for type in sorterClassScheduleList:
        allTypeClassSchedule.append(type.scheduleType)
    for i in range(len(allTypeClassSchedule)):
        if allTypeClassSchedule[i] == typeEntry:
            print("El Horario ya Existe.")
            break
    else:
        if typeEntry == "MAÑANA":
            startOfScheduleEntry = "8:00"
            endOfScheduleEntry = "11:30"
        elif typeEntry == "TARDE":
            startOfScheduleEntry = "1:00"
            endOfScheduleEntry = "4:30"
        elif typeEntry == "NOCHE":
            startOfScheduleEntry = "6:00"
            endOfScheduleEntry = "9:30"
        newClassSchedule = ClassSchedule(typeEntry,startOfScheduleEntry,endOfScheduleEntry)
        classScheduleList.append(newClassSchedule)
        SetClassScheduleList(classScheduleList)
def DeleteClassSchedule():
    ShowClassSchedule()
    courseList = GetCourseList()
    classScheduleList = GetClassScheduleList()
    enterClassSchedulePosition = input("\nIngrese la posición del Horario que quiera eliminar: ")
    if not enterClassSchedulePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for course in courseList:
        if (classScheduleList[int(enterClassSchedulePosition)]).scheduleType in course.classScheduleList:
            course.classRoomsList.remove(classScheduleList[int(enterClassSchedulePosition)].scheduleType)
    if classScheduleList[int(enterClassSchedulePosition)] in classScheduleList:
        classScheduleList.remove(classScheduleList[int(enterClassSchedulePosition)])
    SetClassScheduleList(classScheduleList)
    SetCourseList(courseList)
def ShowClassSchedule():
    classScheduleNumber = 0
    classScheduleList = GetClassScheduleList()
    for classSchedule in classScheduleList:
        classScheduleNumber = classScheduleNumber + 1
        print("Número de Horario: ", classScheduleNumber - 1, " **Tipo de Horario: ", classSchedule.scheduleType,
              " **Hora de Inicio: ", classSchedule.startOfSchedule, " **Hora de Salida: ", classSchedule.endOfSchedule)
def ModifyClassSchedule():
    ShowClassSchedule()
    enterClassSchedulePosition = int(input("\nIngrese el numero del Horario que quiera Modificar: "))
    classScheduleList = GetClassScheduleList()
    classScheduleExist = False
    for i in range(len(classScheduleList)):
        if i == enterClassSchedulePosition:
            classScheduleExist = True
            while True:
                print("\t1...Modificar Tipo de Horario.\n"
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        for i in range(len(allTypeClassSchedule)):
                            classScheduleList[i].scheduleType = input("Ingrese nuevo Tipo: ")
                            classScheduleList[i].scheduleType = classScheduleList[i].scheduleType.upper()
                            if allTypeClassSchedule[i] == classScheduleList[i].scheduleType:
                                print("El Horario ya existe")
                                break
                            else:
                                break
                        if classScheduleList[i].scheduleType == "MAÑANA":
                            classScheduleList[i].startOfSchedule = "8:00"
                            classScheduleList[i].endOfSchedule = "11:30"
                        elif classScheduleList[i].scheduleType == "TARDE":
                            classScheduleList[i].startOfSchedule = "1:00"
                            classScheduleList[i].endOfSchedule = "4:30"
                        elif classScheduleList[i].scheduleType == "NOCHE":
                            classScheduleList[i].startOfSchedule = "6:00"
                            classScheduleList[i].endOfSchedule = "9:30"
                    else:
                        input("\nNo has pulsado ninguna opción correcta...\n"
                                  "Presione una tecla para volver a las Opciones.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
    if not classScheduleExist:
        print("El Horario NO Existe.")
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