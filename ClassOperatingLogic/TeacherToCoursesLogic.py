from ClassLogic.TeacherLogic import *
from ClassLogic.CourseLogic import *
teacherIdentificationCardList = []
def ListOfTeacherIdentificationCard():
    teacherList = GetTeacherList()
    for j in range(len(teacherList)):
        teacherIdentificationCardList.append(teacherList[j].teacherIdentificationCard)
        print("Nombre del Docente: ", teacherList[j].teacherName, " **Cédula del Docente: ",teacherList[j].teacherIdentificationCard)
def AddTeacherToCourses():
    ShowCourseList()
    courseList = GetCourseList()
    careerList = GetCareerList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Asignarle un Docente: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            while True:
                print("1...Asignar un Docente a un Curso.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfTeacherIdentificationCard()
                        addIdentificationCard = input("\nIngrese número de Cédula del Docente a Asignar: ")
                        addIdentificationCard = addIdentificationCard.upper()
                        for o in teacherIdentificationCardList:
                            if o in addIdentificationCard:
                                for k in courseList[i].teacherList:
                                    if k == addIdentificationCard:
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
                                        if not addIdentificationCard in careerList[careerIndexes[0]].teacherList:
                                            careerList[careerIndexes[0]].teacherList.append(addIdentificationCard)
                                    else:
                                        print("A cual carrera quiere asignar el docente")
                                        for e in careerIndexes:
                                            print(e, careerList[i].name)
                                        careerseleted = int(input("digite la posicion de la carrera"))
                                        # validate not repeat students
                                        if not addIdentificationCard in careerList[careerseleted].teacherList:
                                            careerList[careerseleted].teacherList.append(addIdentificationCard)
                                        else:
                                            print("El estudiante ya esta matriculado en esta carrera")
                                    courseList[i].teacherList.append(addIdentificationCard)
                                    print(courseList[i].teacherList)
                                    SetCourseList(courseList)
                                    SetCareerList(careerList)
                                    break
                        else:
                            print("La Cédula del Docente no Existe.\n")
                    elif optionsEntry == "0":
                        break
                    else:
                        print("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciones.")
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
            ListOfTeacherIdentificationCard()
            deleteCode = input("Ingrese el codigo que desea eliminar")
            deleteCode = deleteCode.upper()
            if deleteCode in courseList[i].teacherList:
                courseList[i].teacherList.remove(deleteCode)
        else:
            print("No existe ese Curso")
    SetCourseList(courseList)
def TeacherToCoursesMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Docente a un Curso.\n"
          "\t2...Desasignar un Docente a un Curso.\n"
          "\t3...Visualizar las asignaciones del Cursos.\n"
          "\t0...Volver al Menú Operativo.")
def TeacherToCoursesMenuOptions():
    while True:
        TeacherToCoursesMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddTeacherToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteTeacherLogicToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
TeacherToCoursesMenuOptions()