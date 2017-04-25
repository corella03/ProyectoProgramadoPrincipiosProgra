from ClassLogic.CareerLogic import *
from ClassTypes.Course import *
from pathlib import Path
import pickle
def GetCourseList():
    myCourseFile = Path("..\Files\CourseFile.pickle")
    if myCourseFile.is_file():
        with open("..\Files\CourseFile.pickle", "rb") as courseFile:
            courseList = pickle._load(courseFile)
        return courseList
    return []
def SetCourseList(courseList):
    with open("..\Files\CourseFile.pickle", "wb") as courseFile:
        pickle._dump(courseList,courseFile)
def AddCourse():
    courseList = GetCourseList()
    codeEntry = input("Ingrese el Código del Curso: ")
    codeEntry = codeEntry.upper ()
    allCodeToCourse = []
    sorterCourseList = sorted(courseList, key=lambda course: course.courseCode)
    for code in sorterCourseList:
        allCodeToCourse.append(code.courseCode)
    for i in range(len(allCodeToCourse)):
        if allCodeToCourse[i] == codeEntry:
            print("El Curso ya Existe.")
            break
    else:
        nameEntry = input("Ingrese el Nombre del Curso: ")
        newCourse = Course(nameEntry,codeEntry)
        courseList.append(newCourse)
        SetCourseList(courseList)
def DeleteCourse():
    ShowCourseList()
    courseList = GetCourseList()
    careerList = GetCareerList()
    enterCoursePosition = input("\nIngrese la posición del Curso que quiera Eliminar: ")
    if not enterCoursePosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for career in careerList:
        if courseList[int(enterCoursePosition)].courseCode in career.courseList:
            career.courseList.remove(courseList[int(enterCoursePosition)].courseCode)
    if courseList[int(enterCoursePosition)] in courseList:
        courseList.remove(courseList[int(enterCoursePosition)])
    SetCourseList(courseList)
    SetCareerList(careerList)
def ShowCourseList():
    courseNumber = 0
    courseList = GetCourseList()
    for course in courseList:
        courseNumber = courseNumber + 1
        print("Número de Curso: ",courseNumber - 1," **Nombre: ",course.courseName, " **Código: ",course.courseCode)
def ModifyCourse():
    ShowCourseList()
    enterCoursePosition = int(input("\nIngrese el numero del Curso que quiera Modificar: "))
    courseList = GetCourseList()
    courseExist = False
    for i in range(len(courseList)):
        if i == enterCoursePosition:
            courseExist = True
            while True:
                print("\t1...Modificar Nombre del Curso.\n",
                      "\t2...Modificar Código del Curso.\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        courseList[i].courseName = input("Ingrese nuevo Nombre: ")
                    elif optionsEntry == "2":
                        courseList[i].courseCode = input("Ingrese el nuevo Código: ")
                        courseList[i].courseCode = courseList[i].courseCode.upper()
                    else:
                        input("\nNo has pulsado ninguna opción correcta...\n"
                              "Presione una tecla para volver a las Opciones.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
    if not courseExist:
        print("El Curso NO Existe.")
    SetCourseList(courseList)
def ShowAsignationToCourses():
    courseList = GetCourseList()
    courseNumber = 0
    for course in courseList:
        courseNumber = courseNumber + 1
        print("Número de Curso: ", courseNumber - 1, " **Nombre: ", course.courseName, " **Código: ", course.courseCode,
              " **Lista de Estudiantes: ", course.studentList, " \n\t**Lista de Profesores: ", course.teacherList,
              " **Recinto donde Pertenece: ", course.campusList, " **Aulas donde se Imparten Clases: ",
              course.classRoomsList," **Horario del Curso: ", course.classScheduleList)

def CourseMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Agregar Curso.\n"
          "\t2...Eliminar Curso.\n"
          "\t3...Ver Cursos.\n"
          "\t4...Modificar Cursos.\n"
          "\t0...Volver al Menú Administrativo.")
def CourseMenuOptions():
    while True:
        CourseMenu()
        optionsEntry = input("\nIngrese la Opción a Escoger: ")
        if optionsEntry == "1":
            AddCourse()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteCourse()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowCourseList()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "4":
            ModifyCourse()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")