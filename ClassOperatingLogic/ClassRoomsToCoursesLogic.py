from ClassLogic.CourseLogic import *
from ClassLogic.ClassroomsLogic import *
def AddClassRoomsToCourses():
    ShowCourseList()
    courseList = GetCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Asignarle un Aula: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            while True:
                print("1.. Asignar un Aula a un Curso.\n"
                      "0.. Salir.")
                optionsEntry = input(" Ingrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        classRoomsList = GetClassRoomsList()
                        codeList = []
                        for j in range(len(classRoomsList)):
                            codeList.append(classRoomsList[j].classRoomsCode)
                            print("Código de Aula: ",classRoomsList[j].classRoomsCode," Recinto donde Pertenezca: ",
                                  classRoomsList[j].classroomsCampusBelongs)
                        addCode = input("ingrese codigo")
                        for o in codeList:
                            if o in addCode:
                                for k in courseList[i].classRoomsList:
                                    if k == addCode:
                                        print("El Aula ya se encuentra en este Curso.")
                                        break
                                else:
                                    courseList[i].classRoomsList.append(addCode)
                                    print(courseList[i].classRoomsList)
                                    SetCourseList(courseList)
                                    break
                    elif optionsEntry == "0":
                        break
                    else:
                        print("No has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes")
                else:
                    break
def DeletClassRoomsToCourses():
    ShowCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Eliminarle un Aula: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    courseList = GetCourseList()
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            deleteCode = input("Ingrese el codigo que desea eliminar")
            if deleteCode in courseList[i].classRoomsList:
                courseList[i].classRoomsList.remove(deleteCode)
            else:
                print("No existe ese Curso")
    SetCourseList(courseList)
def ClassRoomsToCoursesMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Asignar un Aula a un Curso.\n"
          "\t2.. Desasignar un Aula a un Curso.\n"
          "\t0.. Volver al Menú Operativo.")
def ClassRoomsToCoursesMenuOptions():
    while True:
        ClassRoomsToCoursesMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddClassRoomsToCourses()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeletClassRoomsToCourses()
        elif optionsEntry == "0" :
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
ClassRoomsToCoursesMenuOptions()