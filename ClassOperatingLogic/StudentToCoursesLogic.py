from ClassLogic.StudentLogic import *
from ClassLogic.CourseLogic import *
from ClassLogic.CareerLogic import *
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
                print("1.. Asignar un Estudiante a un Curso.\n"
                      "0.. Salir.")
                optionsEntry = input(" Ingrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        studentList = GetStudenList()
                        codeList = []
                        for j in range(len(studentList)):
                            codeList.append(studentList[j].identificationCard)
                            print("Nombre del Estudiante: ",studentList[j].name,
                                  " Cédula : ", studentList[j].identificationCard)
                        addCode = input(" Ingrese Cédula: ")
                        for o in codeList:
                            if o in addCode:
                                for k in courseList[i].studentList:
                                    if k == addCode:
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
                                        if not addCode in careerList[careerIndexes[0]].studentList:
                                            careerList[careerIndexes[0]].studentList.append(addCode)
                                    else:
                                        print("A cual carrera quiere asignar el estudiente")
                                        for e in careerIndexes:
                                            print(e, careerList[i].name)
                                        careerseleted = int(input("digite la posicion de la carrera"))
                                        #validate not repeat students
                                        if not addCode in careerList[careerseleted].studentList:
                                            careerList[careerseleted].studentList.append(addCode)
                                        else:
                                            print("El estudiante ya esta matriculado en esta carrera")
                                    courseList[i].studentList.append(addCode)
                                    SetCourseList(courseList)
                                    SetCareerList(careerList)
                                    break
                    elif optionsEntry == "0":
                        break
                    else:
                        print("No has pulsado ninguna opcion correcta... \n"
                              "P1resione una tecla para volver a las Opciónes")
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
            deleteCode = input("Ingrese la Cédula que desea eliminar: ")
            if deleteCode in courseList[i].studentList:
                courseList[i].studentList.remove(deleteCode)
            else:
                print("no existe el estudinte")
    SetCourseList(courseList)
def StudentToCourseMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Asignar un Estudiante a un Curso.\n"
          "\t2.. Desasignar un Estudiante a un Curso.\n"
          "\t0.. Volver al Menú Operativo.")
def StudentToCourseMenuOptions():
    while True:
        StudentToCourseMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddStudenLogicToCourses()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeleteStudentToCourse()
        elif optionsEntry == "0" :
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
StudentToCourseMenuOptions()