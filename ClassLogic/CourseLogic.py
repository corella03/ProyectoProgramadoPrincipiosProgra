import pickle
from ClassTypes.Course import *
from pathlib import Path
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
    enterCoursePosition = int(input("\nIngrese la posición del Curso que quiera Eliminar: "))
    courseList.remove(courseList[enterCoursePosition])
    SetCourseList(courseList)
def ShowCourseList():
    #Preguntar que si hay que imprimir las asignaciones
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
def CourseMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Agregar Curso.\n"
          "\t2.. Eliminar Curso.\n"
          "\t3.. Ver Cursos.\n"
          "\t4.. Modificar Cursos.\n"
          "\t0.. Volver al Menú Administrativo.")
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
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")