import pickle
from pathlib import Path
from ClassTypes.Student import *
def GetStudenList ():
    myStudentFile = Path("..\Files\StudentFile.pickle")
    if myStudentFile.is_file():#yaExiste es porque alguien le metio una lista "Algo"
        with open("..\Files\StudentFile.pickle", "rb") as studentFile:
            studentList = pickle._load(studentFile)
        return studentList
    return []#si no creemela lsta
def SetStudentList(studentList):
    with open("..\Files\StudentFile.pickle","wb") as studentFile:
        pickle._dump(studentList, studentFile)
def AddStudent():
    nameEntry = input("Ingrese el Nombre del Estudiante:")
    lastNameEntry = input("Ingrese el Apellido del Estudiante:")
    identificationCardEntry = input("Ingrese el número de Cédula del Estudiante:")
    addressEntry = input("Ingrese la Dirección donde vive el Estudiante:")
    phoneEntry = input("Ingrese el Número de Telefono del Estudiante:")
    emailEntry = input("Ingrese el email del Estudiante:")
    newStudent = Student(nameEntry, lastNameEntry, identificationCardEntry, addressEntry, phoneEntry, emailEntry)
    studentList = GetStudenList()
    studentList.append(newStudent)
    SetStudentList(studentList)
def DeleteStudent():
    studentNumber = 0
    studentList = GetStudenList()
    for student in studentList:
        studentNumber = studentNumber + 1
        print("Número del Estudiante:",studentNumber - 1," Nombre: ",student.name," Apellido: ",student.lastName," Cédula: ",
              student.identificationCard," Número Telefonico: ",student.phone," Dirección de Residencia: ",student.address,
              " Correo Eléctronico ",student.email)
    enterStudentPosition = int(input("Ingrese el numero del estudiante que quiera eliminar:"))
    studentList.remove(studentList[enterStudentPosition])
    SetStudentList(studentList)
def ShowStudentList():
    studentNumber = 0
    studentList = GetStudenList()
    for student in studentList:
        studentNumber = studentNumber + 1
        print("Número del Estudiante:",studentNumber - 1," Nombre: ",student.name," Apellido: ",student.lastName," Cédula: ",
              student.identificationCard," Número Telefonico: ",student.phone," Dirección de Residencia: ",student.address,
              " Correo Eléctronico ",student.email)
def ModifyStudent():
    enterStudentPosition = int(input("Ingrese el numero del estudiante que quiera Modificar:"))
    studentList = GetStudenList()
    for i in range(len(studentList)):
        if i == enterStudentPosition:
            while True:
                print("1- Para modificar el nombre:\n"
                      "2- Para modificar el apellido:\n"
                      "3- Para modificar Id:\n"
                      "4- Para modificar el direccion:\n"
                      "5- Para modificar el telefono:\n"
                      "6- Para modificar el emal:\n"
                      "0- salir:")
                optionsEntry = input("Ingrese la Opción a Escoger")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        studentList[i].name = input("Ingrese nuevo nombre")
                    elif optionsEntry == "2":
                        studentList[i].lastName = input("Ingrese nuevo Apellido")
                    elif optionsEntry == "3":
                        studentList[i].identificationCard = input("Ingrese nuevo número de Cédula")
                    elif optionsEntry == "4":
                        studentList[i].address = input("Ingrese nueva Dirección")
                    elif optionsEntry == "5":
                        studentList[i].phone = input("Ingrese nuevo numero telefonico")
                    elif optionsEntry == "6":
                        studentList[i].email = input("Ingrese nuevo Email")
                    else:
                        input("No has pulsado ninguna opción correcta...\n"
                              "Presione enter Para volver al Menú")
                else:
                    break
                print("\033[;34mNombre:", studentList[i].name + "\033[;23m", "\033[;34mApellido:", studentList[i].lastName +"\033[;23m"
                      "\033[;34mCédula:", studentList[i].identificationCard + "\033[;23m","\033[;34mDirección:",studentList[i].address + "\033[;23m",
                      "\033[;34mNumero de Telefono:", studentList[i].phone + "\033[;23m", "\033[;34mEmail:",studentList[i].email + "\033[;23m")
    SetStudentList(studentList)
def StudentMenu():
    print("\033[;34m" + "\nSelecciona una opción\n"
     "\t1 - Agregar Estudiante\n"
     "\t2 - Eliminar Estudiante\n"
     "\t3 - Ver Estudiantes\n"
     "\t4 - Modificar Estudiantes\n"
     "\t0 - Volver al Menú Administrativo" + "\033[;23m")
def StudentMenuOptions():
    while True:
        StudentMenu()
        optionsEntry = input("Ingrese la Opción a Escoger")
        if optionsEntry == "1":
            AddStudent()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "2":
            DeleteStudent()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "3":
            ShowStudentList()
        elif optionsEntry == "4":
            ModifyStudent()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")
StudentMenuOptions()