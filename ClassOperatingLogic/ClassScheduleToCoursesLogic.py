from ClassLogic.ClassScheduleLogic import *
from ClassLogic.CourseLogic import *
typeList = []
def ListOfClassSchedulesTypes():
    classScheduleList = GetClassScheduleList()
    for j in range(len(classScheduleList)):
        typeList.append(classScheduleList[j].scheduleType)
        print("Tipo de Horario del Curso: ", classScheduleList[j].scheduleType,
              " **Hora de Inicio: ", classScheduleList[j].startOfSchedule,
              " **Hora de Salida: ", classScheduleList[j].endOfSchedule)
def AddClassScheduleToCourses():
    courseList = GetCourseList()
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Agregarle un Horario: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            while True:
                print("1...Asignar un Horario a un Curso.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfClassSchedulesTypes()
                        addType = input("\nIngrese el Tipo del Horario a Asignar: ")
                        addType = addType.upper()
                        for o in typeList:
                            if o in addType:
                                for k in courseList[i].classScheduleList:
                                    if k == addType:
                                        print("El Horario ya se encuentra en esta Carrera.")
                                        break
                                else:
                                    courseList[i].classScheduleList.append(addType)
                                    print("Asignación Correcta.\n")
                                    SetCourseList(courseList)
                                    break
                        else:
                            # Validar por que si ya asine el curso me sale El Horario ya se encuentra en esta Carrera. y igaul en todas las demas
                            # El Código del Recinto no Existe.
                            print("El Código del Recinto no Existe.\n")
                    elif optionsEntry == "0":
                        break
                    else:
                        print("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciones.")
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
            ListOfClassSchedulesTypes()
            deleteType = input("\nIngrese el Tipo del Horario que desea Eliminar: ")
            deleteType = deleteType.upper()
            if deleteType in courseList[i].classScheduleList:
                courseList[i].classScheduleList.remove(deleteType)
                print("Desasignación Correcta.\n")
            else:
                print("No existe ese Curso o no ha sido Asignado.")
    SetCourseList(courseList)
def ClassScheduleToCourseMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Horario a un Curso.\n"
          "\t2...Desasignar un Horario a un Curso.\n"
          "\t3...Visualizar las asignaciones del Curso.\n"
          "\t0...Volver al Menú Operativo.")
def ClassScheduleToCourseMenuOptions():
    while True:
        ClassScheduleToCourseMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry== "1":
            AddClassScheduleToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteClassScheduleToCourse()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
ClassScheduleToCourseMenuOptions()