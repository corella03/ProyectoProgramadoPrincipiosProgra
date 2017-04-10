import pickle
from ClassTypes.Teacher import *
from pathlib import  Path
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
    nameEntry = str(input("Ingrese el Nombre del Docente  :"))
    lastNameEntry = str(input("Ingrese el Apellido del Docente  :"))
    identificationCardEntry = str(input("Ingrese el número de Cédula del Docente:"))
    addressEntry = str(input("Ingrese el Lugar de Residencia del Docente  :"))
    phoneEntry = str(input("Ingrese el Numero de telefono del Docente  :"))
    emailEntry = str(input("Ingrese el Correo del Docente  :"))
    newTeacher = Teacher(nameEntry,lastNameEntry,identificationCardEntry,addressEntry,phoneEntry,emailEntry)
    teacherList = GetTeacherList()
    teacherList.append(newTeacher)
    SetTeacherList(teacherList)
def DeleteTeacher():
    option = input("Desea eliminar un Docente ? si/no:")
    if option == "si":
        teacherNumber = 0
        teacherList = GetTeacherList()
        for teacher in teacherList:
            print("Número del Docente:",teacherNumber - 1,"Nombre del  Docente", teacher.teacherName, "Apellido del Docente ", teacher.teacherLastName,
                  "Número de Cédula del Docente",
                  teacher.teacherIdentificationCard, "Residencia del Docente", teacher.teacherResidency,
                  "Telefono del Docente", teacher.teacherPhone, "Correo del Docente", teacher.teacherEmail)
        deleteTeacher = int(input("Ingrese el número que desea eliminar :"))
        teacherList.remove(teacherList[deleteTeacher])
        SetTeacherList(teacherList)
    else:
        print("Vuelva a las opciones anteriores")
def ShowTeacherList():
    teacherNumber = 0
    teacherList = GetTeacherList()
    for teacher in teacherList:
        print("Número del Docente:",teacherNumber - 1,"Nombre del  Docente", teacher.teacherName, "Apellido del Docente ", teacher.teacherLastName, "Número de Cédula del Docente",
              teacher.teacherIdentificationCard, "Residencia del Docente", teacher.teacherResidency,
              "Telefono del Docente", teacher.teacherPhone,"Correo del Docente", teacher.teacherEmail)
def ModifyTeacher():
    modify = int(input("Ingrese el número del Docente que desea modificar:"))
    teacherList = GetTeacherList()
    for x in range(len(teacherList)):
        if x == modify:
            while True:
                print("\t1...Modificar Nombre del Docente", "\n",
                      "\t2...Modifciar Apellido del Docente", "\n",
                      "\t3...Modificar el número de Cédula del Docente", "\n",
                      "\t4...Modificar Residencia del Docente", "\n",
                      "\t5...Modificar Telefono del Docente", "\n",
                      "\t6...Modificar Correo del Docente", "\n",
                      "\t0...Salir")
                option = input("Por favor, Ingrese una opción :")
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
                        input("No has pulsado ninguna opción correcta...\n"
                              "Presione una tecla para volver a las Opciones.")
                else:
                    break
                print("Nombre: ",teacherList[x].teacherName," Apellido: ",teacherList[x].teacherLastName," Cédula:",
                      teacherList[x].teacherIdentificationCard," Dirección: ",teacherList[x].teacherResidency," Numero de Telefono: ",
                      teacherList[x].teacherPhone," Email: ",teacherList[x].teacherEmail)
        else:
            print("La posición del Docente no existe.")
    SetTeacherList(teacherList)
def TeacherMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Agregar Docente.\n"
          "\t2.. Eliminar Docente.\n"
          "\t3.. Ver Lista Docente.\n"
          "\t4.. Modificar Docente.\n"
          "\t0.. Volver al Menú Administrativo.")
def TeacherMenuOption():
    while True:
        TeacherMenu()
        option = input("\nIngrese la Opción a Escoger: ")
        if option == "1":
            AddTeacher()
            input("\npulsa una tecla para continuar.")
        elif option == "2":
            DeleteTeacher()
            input("\npulsa una tecla para continuar.")
        elif option == "3":
            ShowTeacherList()
            input("\npulsa una tecla para continuar.")
        elif option == "4":
            ModifyTeacher()
            input("\npulsa una tecla para continuar.")
        elif option == "0":
            break
            input("\npulsa una tecla para continuar.")
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")
TeacherMenuOption()