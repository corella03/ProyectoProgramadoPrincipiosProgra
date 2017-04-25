from ClassLogic.ClassroomsLogic import *
from ClassLogic.CourseLogic import *
codeList = []
def ListOfClassRoomsCodes():
    classRoomsList = GetClassRoomsList()
    for j in range(len(classRoomsList)):
        codeList.append(classRoomsList[j].classRoomsCode)
        print("Código de Aula: ", classRoomsList[j].classRoomsCode, " **Recinto donde Pertenezca: ",
              classRoomsList[j].classroomsCampusBelongs)
def AddClassRoomsToCourses():
    courseList = GetCourseList()
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Asignarle un Aula: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            while True:
                print("1...Asignar un Aula a un Curso.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opción: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfClassRoomsCodes()
                        # Validar si el aula no existe
                        addCode = input("\nIngrese Código del Aula a Asignar: ")
                        addCode = addCode.upper()
                        for o in codeList:
                            if o in addCode:
                                for k in courseList[i].classRoomsList:
                                    if k == addCode:
                                        print("El Aula ya se Asignó a este Curso.")
                                        break
                                else:
                                    courseList[i].classRoomsList.append(addCode)
                                    print("Asignación Correcta.\n")
                                    SetCourseList(courseList)
                                    break
                        else:
                            print("El Código del Aula no Existe.\n")
                    elif optionsEntry == "0":
                        break
                    else:
                        print("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes.")
                else:
                    break
def DeletClassRoomsToCourses():
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Eliminarle Aulas: ")
    # Valir si no existes la posicion del curos dar mensaje de error
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    courseList = GetCourseList()
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            ListOfClassRoomsCodes()
            deleteCode = input("\nIngrese el código del Aula que desea Eliminar: ")
            deleteCode = deleteCode.upper()
            if deleteCode in courseList[i].classRoomsList:
                courseList[i].classRoomsList.remove(deleteCode)
                print("Desasignación Correcta.\n")
            else:
                print("No existe ese Curso o no ha sido Asignado.")
    SetCourseList(courseList)
def ClassRoomsToCoursesMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Aula a un Curso.\n"
          "\t2...Desasignar un Aula a un Curso.\n"
          "\t3...Visualizar las asignaciones del Curso.\n"
          "\t0...Volver al Menú Operativo.")
def ClassRoomsToCoursesMenuOptions():
    while True:
        ClassRoomsToCoursesMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddClassRoomsToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeletClassRoomsToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
ClassRoomsToCoursesMenuOptions()