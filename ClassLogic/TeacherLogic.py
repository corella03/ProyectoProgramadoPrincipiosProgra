from ClassTypes.Teacher import *
from ClassLogic.CourseLogic import *
import pickle
from pathlib import Path
def GetTeacherList():
    myTeacherFile = Path("..\Files\TeacherFile.pickle")
    if myTeacherFile.is_file():
        with open("..\Files\TeacherFile.pickle", "rb") as teacherFile:
            teacherList = pickle._load(teacherFile)
        return teacherList
    return []
def SetTeacherList(teacherList):
    with open("..\Files\TeacherFile.pickle", "wb") as teacherFile:
        pickle._dump(teacherList, teacherFile)
def AddTeacher():
    teacherList = GetTeacherList()
    identificationCardEntry = str(input("Ingrese el número de Cédula del Docente: "))
    domainTeacher = "@utn.ac.cr"
    allIdToTeacher = []
    sorterTeachertList = sorted(teacherList, key=lambda teacher: teacher.teacherIdentificationCard)
    for idTeacher in sorterTeachertList:
        allIdToTeacher.append(idTeacher.teacherIdentificationCard)
    for j in range(len(allIdToTeacher)):
        if allIdToTeacher[j] == identificationCardEntry:
            print("El Docente ya existe.")
            break
    else:
        nameEntry = str(input("Ingrese el Nombre del Docente: "))
        lastNameEntry = str(input("Ingrese el Apellido del Docente: "))
        addressEntry = str(input("Ingrese el Lugar de Residencia del Docente: "))
        phoneEntry = str(input("Ingrese el Numero de telefono del Docente: "))
        while True:
            emailEntry = str(input("Ingrese solo el nombre del Correo del Docente: "))
            if "@" in emailEntry:
                print("Error al ingresar el correo, ingrese solo el nombre sin el @...")
            else:
                emailEntry = emailEntry+domainTeacher
                break
        newTeacher = Teacher(nameEntry,lastNameEntry,identificationCardEntry,addressEntry,phoneEntry,emailEntry)
        teacherList.append(newTeacher)
        SetTeacherList(teacherList)
def DeleteTeacher():
    ShowTeacherList()
    courseList = GetCourseList()
    teacherList = GetTeacherList()
    deleteTeacher = input("\nIngrese la posición del Docente que quiera eliminar: ")
    if not deleteTeacher.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for course in courseList:
        if teacherList[int(deleteTeacher)].teacherIdentificationCard in course.teacherList:
            course.studentList.remove(deleteTeacher[int(deleteTeacher)].teacherIdentificationCard)
    if teacherList[int(deleteTeacher)] in teacherList:
        teacherList.remove(teacherList[int(deleteTeacher)])
    SetTeacherList(teacherList)
    SetCourseList(courseList)
def ShowTeacherList():
    teacherNumber = 0
    teacherList = GetTeacherList()
    for teacher in teacherList:
        teacherNumber = teacherNumber + 1
        print("Número del Docente: ",teacherNumber - 1," **Nombre del  Docente: ",teacher.teacherName," **Apellido del Docente: ",
              teacher.teacherLastName," **Número de Cédula del Docente: ",teacher.teacherIdentificationCard," **Residencia del Docente: ",
              teacher.teacherResidency," **Telefono del Docente: ", teacher.teacherPhone," **Correo del Docente: ",teacher.teacherEmail)
def ModifyTeacher():
    ShowTeacherList()
    modify = int(input("\nIngrese el número del Docente que desea modificar:"))
    teacherList = GetTeacherList()
    teacherExiste = False
    for x in range(len(teacherList)):
        if x == modify:
            teacherExiste = True
            while True:
                print("\t1...Modificar Nombre del Docente.\n",
                      "\t2...Modifciar Apellido del Docente.\n",
                      "\t3...Modificar el número de Cédula del Docente.\n",
                      "\t4...Modificar Residencia del Docente.\n",
                      "\t5...Modificar Telefono del Docente.\n",
                      "\t6...Modificar Correo del Docente.\n",
                      "\t0...Salir.")
                option = input("\nIngrese la Opción a Escoger: ")
                if option != "0":
                    if option == "1":
                        teacherList[x].teacherName = input("Ingrese un Nombre Nuevo")
                    elif option == "2":
                        teacherList[x].teacherLastName = input("Ingrese un Apellido Nuevo")
                    elif option == "3":
                        teacherList[x].teacherIdentificationCard = input("Ingrese una cédula Nueva")
                    elif option == "4":
                        teacherList[x].teacherResidency = input("Ingrese una Residencia Nueva")
                    elif option == "5":
                        teacherList[x].teacherPhone = input("Ingrese un número Nuevo")
                    elif option == "6":
                        teacherList[x].teacherEmail = input("Ingrese un Correo Nuevo")
                    else:
                        input("\nNo has pulsado ninguna opción correcta...\n"
                              "Presione una tecla para volver a las Opciones.")
                elif option == "0":
                    print("Saliendo...")
                    break
    if not teacherExiste:
        print("El Docente NO Existe.")
    SetTeacherList(teacherList)
def TeacherMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Agregar Docente.\n"
          "\t2...Eliminar Docente.\n"
          "\t3...Ver Lista Docente.\n"
          "\t4...Modificar Docente.\n"
          "\t0...Volver al Menú Administrativo.")
def TeacherMenuOption():
    while True:
        TeacherMenu()
        option = input("\nIngrese la Opción a Escoger: ")
        if option == "1":
            AddTeacher()
            input("\nPulsa una tecla para continuar.")
        elif option == "2":
            DeleteTeacher()
            input("\nPulsa una tecla para continuar.")
        elif option == "3":
            ShowTeacherList()
            input("\nPulsa una tecla para continuar.")
        elif option == "4":
            ModifyTeacher()
            input("\nPulsa una tecla para continuar.")
        elif option == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")