from ClassLogic.StudentLogic import *
from ClassLogic.CourseLogic import *
from ClassLogic.CareerLogic import *
studentIdentificationCardsList = []
def ListOfStudentIdentificationCard():
    studentList = GetStudenList()
    for j in range(len(studentList)):
        studentIdentificationCardsList.append(studentList[j].identificationCard)
        print("Nombre del Estudiante: ", studentList[j].name," **Cédula : ", studentList[j].identificationCard)
def AddStudenLogicToCourses():
    ShowCourseList()
    courseList = GetCourseList()
    careerList = GetCareerList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Agregarle a un Estudiante: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            while True:
                print("1...Asignar un Estudiante a un Curso.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfStudentIdentificationCard()
                        addIdentificationCard = input("\nIngrese número de Cédula del Estudiante a Asignar: ")
                        addIdentificationCard = addIdentificationCard.upper()
                        for o in studentIdentificationCardsList:
                            if o in addIdentificationCard:
                                for k in courseList[i].studentList:
                                    if k == addIdentificationCard:
                                        print("El Estudiante ya está Matriculado en este Curso.")
                                        break
                                else:
                                    careerIndexes = []
                                    for q in range(len(careerList)):
                                        for careerCourse in careerList[q].courseList:
                                            if careerCourse == courseList[i].courseCode:
                                                careerIndexes.append(q)
                                    if len(careerIndexes) == 0:
                                        print("Este curso no esta asignado a ninguna carrera porfavor asignarlo antes de matricular estudiantes")
                                        break
                                    elif len(careerIndexes) == 1:
                                        #validate not repeat students
                                        if not addIdentificationCard in careerList[careerIndexes[0]].studentList:
                                            careerList[careerIndexes[0]].studentList.append(addIdentificationCard)
                                            print("Asignación Correcta.\n")
                                    else:
                                        print("A cual carrera quiere asignar el estudiente")
                                        for e in careerIndexes:
                                            print(e, careerList[i].name)
                                        careerseleted = int(input("digite la posicion de la carrera"))
                                        #validate not repeat students
                                        if not addIdentificationCard in careerList[careerseleted].studentList:
                                            careerList[careerseleted].studentList.append(addIdentificationCard)
                                        else:
                                            print("El estudiante ya esta matriculado en esta carrera")
                                    courseList[i].studentList.append(addIdentificationCard)
                                    print("Asignación Correcta.\n")
                                    SetCourseList(courseList)
                                    SetCareerList(careerList)
                                    break
                        else:
                            print("La Cédula ingresada no Existe.\n")
                    elif optionsEntry == "0":
                        break
                    else:
                        print("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciones.")
                else:
                    break
def DeleteStudentToCourse():
    ShowCourseList()
    courseList = GetCourseList()
    enterCoursePosition = input("\nIngrese el Curso que quiere Eliminarle un Estudiante: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(courseList)):
        if i == int(enterCoursePosition):
            ListOfStudentIdentificationCard()
            deleteCode = input("\nIngrese la Cédula del Estudiante que desea eliminar: ")
            deleteCode = deleteCode.upper()
            if deleteCode in courseList[i].studentList:
                courseList[i].studentList.remove(deleteCode)
            else:
                print("No existe el Estudinte.")
    SetCourseList(courseList)
def StudentToCourseMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Estudiante a un Curso.\n"
          "\t2...Desasignar un Estudiante a un Curso.\n"
          "\t3...Visualizar las asignaciones de la Carrera.\n"
          "\t0...Volver al Menú Operativo.")
def StudentToCourseMenuOptions():
    while True:
        StudentToCourseMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry == "1":
            AddStudenLogicToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteStudentToCourse()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCourses()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
StudentToCourseMenuOptions()