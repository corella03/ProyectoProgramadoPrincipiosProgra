from ClassLogic.CourseLogic import *
from ClassLogic.TeacherLogic import *
def AddTeacherToCourses():
    ShowCourseList()
    enterCoursePosition = int(input("\nIngrese el Curso que quiere Asignarle un Aula: "))
    courseList = GetCourseList()
    for i in range(len(courseList)):
        if i == enterCoursePosition:
            while True:
                print("1.. Asignar un Docente a un Curso.\n"
                      "0.. Salir.")
                optionsEntry = input(" Ingrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        teacherList = GetTeacherList()
                        codeList = []
                        for j in range(len(teacherList)):
                            codeList.append(teacherList[j].teacherIdentificationCard)
                            print("Nombre del Docente: ",teacherList[j].teacherName," Cédula del Docente: ",
                                  teacherList[j].teacherIdentificationCard)
                        addCode = input("ingrese Cédula: ")
                        for o in codeList:
                            if o in addCode:
                                courseList[i].teacherList.append(addCode)
                                print(courseList[i].teacherList)
                        SetCourseList(courseList)
                    elif optionsEntry == "0":
                        break
                    else:
                        print("No has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes")
                else:
                    break
def DeleteTeacherLogicToCourses():
    ShowCourseList()
    enterCoursePosition = int(input("\nIngrese el Curso que quiere Eliminarle un Docente: "))
    courseList = GetCourseList()
    for i in range(len(courseList)):
        if i == enterCoursePosition:
            deleteCode = input("Ingrese el codigo que desea eliminar")
            courseList[i].teacherList.remove(deleteCode)
        else:
            print("No existe ese Curso")
    SetCourseList(courseList)
def TeacherToCoursesMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Asignar un Docente a un Curso.\n"
          "\t2.. Desasignar un Docente a un Curso.\n"
          "\t0.. Volver al Menú Operativo.")
def TeacherToCoursesMenuOptions():
    while True:
        TeacherToCoursesMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddTeacherToCourses()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeleteTeacherLogicToCourses()
        elif optionsEntry == "0" :
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")