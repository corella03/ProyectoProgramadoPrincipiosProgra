from ClassLogic.CourseLogic import *
from ClassLogic.TeacherLogic import *
from ClassLogic.CourseLogic import *
def AddTeacherToCourses():
    ShowCourseList()
    courseList = GetCourseList()
    careerList = GetCareerList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Asignarle un Aula: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
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
                                for k in courseList[i].teacherList:
                                    if k == addCode:
                                        print("Este Docente ya está Registrado en este Curso.")
                                        break
                                else:
                                    careerIndexes = []
                                    for q in range(len(careerList)):
                                        for careerCourse in careerList[q].courseList:
                                            if careerCourse == courseList[i].courseCode:
                                                careerIndexes.append(q)
                                    if len(careerIndexes) == 0:
                                        print("Este curso no esta asignado a ninguna carrera, por favor asignarlo, antes de asignarle un Docente.")
                                        break
                                    elif len(careerIndexes) == 1:
                                        if not addCode in careerList[careerIndexes[0]].teacherList:
                                            careerList[careerIndexes[0]].teacherList.append(addCode)
                                    else:
                                        print("A cual carrera quiere asignar el docente")
                                        for e in careerIndexes:
                                            print(e, careerList[i].name)
                                        careerseleted = int(input("digite la posicion de la carrera"))
                                        # validate not repeat students
                                        if not addCode in careerList[careerseleted].teacherList:
                                            careerList[careerseleted].teacherList.append(addCode)
                                        else:
                                            print("El estudiante ya esta matriculado en esta carrera")
                                    courseList[i].teacherList.append(addCode)
                                    print(courseList[i].teacherList)
                                    SetCourseList(courseList)
                                    SetCareerList(careerList)
                                    break
                    elif optionsEntry == "0":
                        break
                    else:
                        print("No has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes")
                else:
                    break
def DeleteTeacherLogicToCourses():
    ShowCourseList()
    courseList = GetCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Eliminarle un Docente: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            deleteCode = input("Ingrese el codigo que desea eliminar")
            if deleteCode in courseList[i].teacherList:
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
TeacherToCoursesMenuOptions()