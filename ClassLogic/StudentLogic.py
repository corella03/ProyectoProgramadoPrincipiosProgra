from ClassTypes.Student import *
studentList = []
def AddStudent():
    nameEntry = input("Ingrese el Nombre del Estudiante:")
    lastNameEntry = input("Ingrese el Apellido del Estudiante:")
    identificationCardEntry = input("Ingrese el número de Cédula del Estudiante:")
    addressEntry = input("Ingrese la Dirección donde vive el Estudiante:")
    phoneEntry = input("Ingrese el Número de Telefono del Estudiante:")
    emailEntry = input("Ingrese el email del Estudiante:")
    newStudent = Student(nameEntry, lastNameEntry, identificationCardEntry, addressEntry, phoneEntry, emailEntry)
    studentList.append(newStudent)
def DeleteStudent():
    enterStudentPosition = int(input("Ingrese el numero del estudiante que quiera eliminar:"))
    studentList.remove(studentList[enterStudentPosition])
def ShowStudentList():
    for student in studentList:
        print("Nombre", student.name ,"Apellido",student.lastName,"Cédula",student.identificationCard,
              "Dirreción",student.address,"Telefono",student.phone,"email",student.email)
def ModifyStudent():
    enterStudentPosition = int(input("Ingrese el numero del estudiante que quiera Modificar:"))
    for i in range(len(studentList)):
        if studentList[i] == studentList[enterStudentPosition]:
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
                    for student in studentList:
                        if optionsEntry == "1":
                            student.name = input("Ingrese nuevo nombre")
                        elif optionsEntry == "2":
                            student.lastName = input("Ingrese nuevo Apellido")
                        elif optionsEntry == "3":
                            student.identificationCard = input("Ingrese nuevo número de Cédula")
                        elif optionsEntry == "4":
                            student.address = input("Ingrese nueva Dirección")
                        elif optionsEntry == "5":
                            student.phone = input("Ingrese nuevo numero telefonico")
                        elif optionsEntry == "6":
                            student.email = input("Ingrese nuevo Email")
                        else:
                            input("No has pulsado ninguna opción correcta...\n"
                                  "Presione enter Para volver al Menú")
                else:
                    break
                print("\033[;34mNombre:", student.name + "\033[;23m", "\033[;34mApellido:", student.lastName +"\033[;23m"
                      "\033[;34mCédula:", student.identificationCard + "\033[;23m","\033[;34mDirección:", student.address + "\033[;23m",
                      "\033[;34mNumero de Telefono:", student.phone + "\033[;23m", "\033[;34mEmail:", student.email + "\033[;23m")
def CreateFile():
    studentFile = open("..\Files\Student.txt", "w")
    studentFile.close()
CreateFile()
def WriteFile():
    studentFile = open("..\Files\Student.txt", "a")
    studentFile.write(str((studentList)))
    studentFile.close()
WriteFile()
def ReadAsList():
    studentFile = open("..\Files\Student.txt", "r")
    lineas = studentFile.readlines()
    print(lineas)
    studentFile.close()
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