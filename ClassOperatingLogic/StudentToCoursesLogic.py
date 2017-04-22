from ClassLogic.CourseLogic import *
from ClassLogic.StudentLogic import *
from ClassLogic.CareerLogic import *
def AddStudenLogicToCourses():
    ShowCourseList()
    enterCoursePosition = int(input("\nIngrese el Curso que quiere Agregarle a un Estudiante: "))
    courseList = GetCourseList()
    careerList = GetCareerList()
    for i in range(len(courseList)):
        if i == enterCoursePosition:
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
                                    for q in range(len(careerList)):
                                        careerList[q].studentList.append(addCode)
                                    courseList[i].studentList.append(addCode)
                                    print(courseList[i].studentList)
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
    enterCoursePosition = int(input("\nIngrese el Estudiante que quiere Eliminarle del Curso: "))
    courseList = GetCourseList()
    for i in range(len(courseList)):
        if i == enterCoursePosition:
            deleteCode = input("Ingrese la Cédula que desea eliminar: ")
            courseList[i].studentList.remove(deleteCode)
    else:
        print("No existe ese Curso")
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