import pickle
from pathlib import Path
from ClassTypes.Student import *
def GetStudenList():
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
    domainStudent = '@est.utn.ac.cr'
    nameEntry = input("Ingrese el Nombre del Estudiante: ")
    lastNameEntry = input("Ingrese el Apellido del Estudiante: ")
    identificationCardEntry = input("Ingrese el número de Cédula del Estudiante: ")
    addressEntry = input("Ingrese la Dirección donde vive el Estudiante: ")
    phoneEntry = input("Ingrese el Número de Telefono del Estudiante: ")
    while True:
        emailEntry = input("Ingrese el Email del Estudiante: ")
        if "@" in emailEntry:
            print("Error al ingresar el correo vuelva a intentarlo.")
        else:
            emailEntry = emailEntry+domainStudent
            break
    newStudent = Student(nameEntry, lastNameEntry, identificationCardEntry, addressEntry, phoneEntry, emailEntry)
    studentList = GetStudenList()
    studentList.append(newStudent)
    SetStudentList(studentList)
def DeleteStudent():
    studentNumber = 0
    studentList = GetStudenList()
    for student in studentList:
        studentNumber = studentNumber + 1
        print("Número del Estudiante: ",studentNumber - 1," Nombre: ",student.name," Apellido: ",student.lastName," Cédula: ",
              student.identificationCard," Número Telefonico: ",student.phone," Dirección de Residencia: ",student.address,
              " Correo Eléctronico ",student.email)
    enterStudentPosition = int(input("\nIngrese el numero del estudiante que quiera eliminar: "))
    studentList.remove(studentList[enterStudentPosition])
    SetStudentList(studentList)
def ShowStudentList():
    studentNumber = 0
    studentList = GetStudenList()
    for student in studentList:
        studentNumber = studentNumber + 1
        print("Número del Estudiante: ",studentNumber - 1," Nombre: ",student.name," Apellido: ",student.lastName," Cédula: ",
              student.identificationCard," Número Telefonico: ",student.phone," Dirección de Residencia: ",student.address,
              " Correo Eléctronico ",student.email)
def ModifyStudent():
    enterStudentPosition = int(input("\nIngrese el numero del estudiante que quiera Modificar: "))
    studentList = GetStudenList()
    for i in range(len(studentList)):
        if i == enterStudentPosition:
            while True:
                print("\t1...Modificar Nombre del Estudiante.", "\n",
                      "\t2...Modifciar Apellido del Estudiante.", "\n",
                      "\t3...Modificar el número de Cédula del Estudiante.", "\n",
                      "\t4...Modificar Residencia del Estudiante.", "\n",
                      "\t5...Modificar el número  de Telefono del Estudiante.", "\n",
                      "\t6...Modificar Correo del Estudiante.", "\n",
                      "\t0...Salir.")
                optionsEntry = input("\nIngrese la Opción a Escoger: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        studentList[i].name = input("Ingrese nuevo Nombre: ")
                    elif optionsEntry == "2":
                        studentList[i].lastName = input("Ingrese nuevo Apellido: ")
                    elif optionsEntry == "3":
                        studentList[i].identificationCard = input("Ingrese nuevo número de Cédula: ")
                    elif optionsEntry == "4":
                        studentList[i].address = input("Ingrese nueva Dirección: ")
                    elif optionsEntry == "5":
                        studentList[i].phone = input("Ingrese nuevo numero telefonico: ")
                    elif optionsEntry == "6":
                        studentList[i].email = input("Ingrese nuevo Email: ")
                    else:
                        input("No has pulsado ninguna opción correcta...\n"
                              "Presione una tecla para volver a las Opciones.")
                else:
                    break
                print("Nombre: ",studentList[i].name," Apellido: ",studentList[i].lastName,
                      " Cédula: ", studentList[i].identificationCard," Dirección: ",studentList[i].address,
                      " Numero de Telefono: ", studentList[i].phone," Email: ",studentList[i].email)
    else:
        print("La posición del Estudiante no existe.")
    SetStudentList(studentList)
def StudentMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Agregar Estudiante\n"
          "\t2.. Eliminar Estudiante\n"
          "\t3.. Ver Lista Estudianten\n"
          "\t4.. Modificar Estudiante\n"
          "\t0.. Volver al Menú Administrativo ")
def StudentMenuOptions():
    while True:
        StudentMenu()
        optionsEntry = input("\nIngrese la Opción a Escoger: ")
        if optionsEntry == "1":
            AddStudent()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteStudent()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowStudentList()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "4":
            ModifyStudent()
            input("\npulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")
StudentMenuOptions()