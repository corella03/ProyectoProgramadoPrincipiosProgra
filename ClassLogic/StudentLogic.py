import pickle
from pathlib import Path
from ClassTypes.Student import *
varNumbers = "0123456789"
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
    studentList = GetStudenList()
    identificationCardEntry = input("Ingrese el número de Cédula del Estudiante: ")
    domainStudent = '@est.utn.ac.cr'
    allIdToStudent = []
    sorterStudentList = sorted(studentList, key=lambda student: student.identificationCard)
    for idStudent in sorterStudentList:
        allIdToStudent.append(idStudent.identificationCard)
    for j in range(len(allIdToStudent)):
        if allIdToStudent[j] == identificationCardEntry:
            print("El Estudiante ya existe.")
            break
    else:
        nameEntry = input("Ingrese el Nombre del Estudiante: ")
        lastNameEntry = input("Ingrese el Apellido del Estudiante: ")
        addressEntry = input("Ingrese la Dirección donde vive el Estudiante: ")
        phoneEntry = input("Ingrese el Número de Telefono del Estudiante: ")
        while True:
            emailEntry = input("Ingrese solo el nombre del Correo del Estudiante: ")
            if "@" in emailEntry:
                print("Error al ingresar el correo, ingrese solo el nombre sin el @...")
            else:
                emailEntry = emailEntry+domainStudent
                break
        newStudent = Student(nameEntry, lastNameEntry, identificationCardEntry, addressEntry, phoneEntry, emailEntry)
        studentList.append(newStudent)
        SetStudentList(studentList)
def DeleteStudent():
    studentList = GetStudenList()
    ShowStudentList()
    #Validar si solo le da enter y los numeros igaules no funcionan ejem 11
    while True:
        enterStudentPosition = input("\nIngrese el numero del estudiante que quiera eliminar: ")
        if enterStudentPosition in varNumbers:
            studentList.remove(studentList[int(enterStudentPosition)])
            break
        else:
            print("Datos inválidos intente de nuevo.")
    SetStudentList(studentList)
def ShowStudentList():
    #Preguntar si se imprimen las asignaciones
    studentNumber = 0
    studentList = GetStudenList()
    for student in studentList:
        studentNumber = studentNumber + 1
        print("Número del Estudiante: ",studentNumber - 1," **Nombre: ",student.name," **Apellido: ",student.lastName," **Cédula: ",
              student.identificationCard," **Número Telefonico: ",student.phone," **Dirección de Residencia: ",student.address,
              " **Correo Eléctronico ",student.email)
def ModifyStudent():
    ShowStudentList()
    studentList = GetStudenList()
    studentExist = False
    enterStudentPosition = input("\nIngrese el numero del estudiante que quiera Modificar: ")
    for i in range(len(studentList)):
        if i == int(enterStudentPosition):
            studentExist = True
            while True:
                print("\t1...Modificar Nombre del Estudiante.\n",
                      "\t2...Modifciar Apellido del Estudiante.\n",
                      "\t3...Modificar el número de Cédula del Estudiante.\n",
                      "\t4...Modificar Residencia del Estudiante.\n",
                      "\t5...Modificar el número  de Telefono del Estudiante.\n",
                      "\t6...Modificar Correo del Estudiante.\n",
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
                        input("\nNo has pulsado ninguna opción correcta...\n"
                              "Presione una tecla para volver a las Opciones.")
                elif optionsEntry == "0":
                    print("Saliendo...")
                    break
    if not studentExist:
        print("El Estudiante NO Existe.")
    SetStudentList(studentList)
def StudentMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Agregar Estudiante.\n"
          "\t2...Eliminar Estudiante.\n"
          "\t3...Ver Lista Estudianten.\n"
          "\t4...Modificar Estudiante.\n"
          "\t0...Volver al Menú Administrativo.")
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