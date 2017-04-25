from ClassLogic.CampusLogic import *
from ClassLogic.CourseLogic import *
codeList = []
def ListOfCampusCodes():
    campusList = GetCampusList()
    for j in range(len(campusList)):
        codeList.append(campusList[j].campusCode)
        print("Nombre del Recinto: ", campusList[j].campusName, " **Código del Recinto: ", campusList[j].campusCode)
def AddCampusToCourses():
    courseList = GetCourseList()
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Agregarle Recintos: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            while True:
                print("1...Asignar un Recinto a un Curso.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opción: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfCampusCodes()
                        #Validar si el Recinto no existe print("La posición del Recinto no Existe.\n")
                        addCode = input("\nIngrese Código del Recinto a Asignar: ")
                        addCode = addCode.upper()
                        for o in codeList:
                            if o in addCode:
                                for k in courseList[i].campusList:
                                    if k == addCode:
                                        print("El Recinto ya se Asignó a este curso.")
                                        break
                                else:
                                    courseList[i].campusList.append(addCode)
                                    print("Asignación Correcta.\n")
                                    SetCourseList(courseList)
                                    break
                        else:
                            print("El Código del Recinto no Existe.\n")
                    elif optionsEntry == "0":
                        break
                    else:
                        print("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciones.")
                else:
                    break
def DeleteCampusToCourse():
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Eliminarle Recintos: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    courseList = GetCourseList()
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            ListOfCampusCodes()
            deleteCode = input("\nIngrese el código del Recinto que desea Eliminar: ")
            deleteCode = deleteCode.upper()
            if deleteCode in courseList[i].campusList:
                courseList[i].campusList.remove(deleteCode)
                print("Desasignación Correcta.\n")
            else:
                print("No existe ese Curso o no ha sido Asignado.")
    SetCourseList(courseList)
def CampusToCourseMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Recinto a un Curso.\n"
          "\t2...Desasignar un Recinto a un Curso.\n"
          "\t3...Visualizar las asignaciones del Curso.\n"
          "\t0...Volver al Menú Operativo.")
def CampusToCourseMenuOptions():
    while True:
        CampusToCourseMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry== "1":
            AddCampusToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteCampusToCourse()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
CampusToCourseMenuOptions()