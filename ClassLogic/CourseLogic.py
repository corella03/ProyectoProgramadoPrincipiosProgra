from ClassTypes.Course import *
courseList = []
def AddCourse():
    nameEntry = input("Ingrese el nombre del Curso:")
    codeEntry = input("Ingrese el código del Curso")
    newCourse = Course(nameEntry,codeEntry)
    courseList.append(newCourse)
def DeleteCourse():
    enterCoursePosition = int(input("Ingrese la posición del curso que quiera eliminar:"))
    courseList.remove(courseList[enterCoursePosition])
def ShowCourseList():
    for course in courseList:
        print("Nombre", course.courseName, "Código",course.courseCode)
def ModifyCourse():
    enterCoursePosition = int(input("Ingrese el numero del Curso que quiera Modificar:"))
    for i in range(len(courseList)):
        if courseList[i] == courseList[enterCoursePosition]:
            while True:
                print("1- Para modificar el Nombre:\n"
                      "2- Para modificar el Código:\n"
                      "0- salir:")
                optionsEntry = input("Ingrese la Opción a Escoger")
                if optionsEntry != "0":
                    for course in courseList:
                        if optionsEntry == "1":
                            course.courseName = input("Ingrese nuevo nombre")
                        elif optionsEntry == "2":
                            course.courseCode = input("Ingrese nuevo Código")
                        else:
                            input("No has pulsado ninguna opción correcta...\n"
                                  "Presione enter Para volver al Menú")
                else:
                    break
                print("\033[;34mNombre:", course.courseName + "\033[;23m", "\033[;34mCódigo:", course.courseCode)
def CreateFile():
    courseFile = open("..\Files\Course.txt", "w")
    courseFile.close()
CreateFile()
def WriteFile():
    courseFile = open("..\Files\Course.txt", "a")
    courseFile.write("")
    courseFile.close()
WriteFile()
def ReadAsList():
    courseFile = open("..\Files\Course.txt", "r")
    lineas = courseFile.readlines()
    print(lineas)
    courseFile.close()
def CourseMenu():
    print("\033[;34m" + "\nSelecciona una opción\n"
     "\t1 - Agregar Curso\n"
     "\t2 - Eliminar Curso\n"
     "\t3 - Ver Cursos\n"
     "\t4 - Modificar Curso\n"
     "\t0 - Volver al Menú Administrativo" + "\033[;23m")
def CourseMenuOptions():
    while True:
        CourseMenu()
        optionsEntry = input("Ingrese la Opción a Escoger")
        if optionsEntry == "1":
            AddCourse()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "2":
            DeleteCourse()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "3":
            ShowCourseList()
        elif optionsEntry == "4":
            ModifyCourse()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")