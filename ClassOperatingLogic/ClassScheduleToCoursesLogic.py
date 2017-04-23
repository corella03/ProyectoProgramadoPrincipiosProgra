from ClassLogic.CourseLogic import *
from ClassLogic.ClassScheduleLogic import *
def AddClassScheduleToCourses():
    ShowCourseList()
    courseList = GetCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Agregarle un Horario: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            while True:
                print("1.. Asignar un Horario a un Curso.\n"
                      "0.. Salir.")
                optionsEntry = input(" Ingrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        classScheduleList = GetClassScheduleList()
                        codeList = []
                        for j in range(len(classScheduleList)):
                            codeList.append(classScheduleList[j].scheduleType)
                            print("Tipo de Horario del Curso: ",classScheduleList[j].scheduleType,
                                  " Hora de Inicio: ", classScheduleList[j].startOfSchedule,
                                  "Hora de Salida: ",classScheduleList[j].endOfSchedule)
                        addCode = input("ingrese el Tipo:")
                        for o in codeList:
                            if o in addCode:
                                for k in courseList[i].classScheduleList:
                                    if k == addCode:
                                        print("El Horario ya se encuentra en esta Carrera.")
                                        break
                                else:
                                    courseList[i].classScheduleList.append(addCode)
                                    print(courseList[i].classScheduleList)
                                    SetCourseList(courseList)
                                    break
                    elif optionsEntry == "0":
                        break
                    else:
                        print("No has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes")
                else:
                    break
def DeleteClassScheduleToCourse():
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Eliminarle un Horario: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    courseList = GetCourseList()
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            deleteCode = input("Ingrese el Tipo que desea eliminar")
            if deleteCode in courseList[i].classScheduleList:
                courseList[i].classScheduleList.remove(deleteCode)
            else:
                print("No existe ese Curso")
    SetCourseList(courseList)
def ClassScheduleToCourseMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Asignar un Horario a un Curso.\n"
          "\t2.. Desasignar un Horario a un Curso.\n"
          "\t0.. Volver al Menú Operativo.")
def ClassScheduleToCourseMenuOptions():
    while True:
        ClassScheduleToCourseMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddClassScheduleToCourses()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeleteClassScheduleToCourse()
        elif optionsEntry == "0" :
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
ClassScheduleToCourseMenuOptions()