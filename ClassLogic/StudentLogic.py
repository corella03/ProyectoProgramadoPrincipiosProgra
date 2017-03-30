import ClassTypes.Student
StudentList = []
def AddStudent():
    nameEntry = input("Ingrese el Nombre del Estudiante:")
    lastNameEntry = input("Ingrese el Apellido del Estudiante:")
    identificationCardEntry = input("Ingrese el número de Cédula del Estudiante:")
    addressEntry = input("Ingrese la Dirección donde vive el Estudiante:")
    phoneEntry = input("Ingrese el Número de Telefono del Estudiante:")
    emailEntry = input("Ingrese el email del Estudiante:")
    NewStudent = ClassTypes.Student.Student(nameEntry, lastNameEntry, identificationCardEntry, addressEntry, phoneEntry, emailEntry)
    StudentList.append(NewStudent)
def DeleteStudent():
    enterStudentPosition = int(input("Ingrese el numero del estudiante que quiera eliminar:"))
    StudentList.remove(StudentList[enterStudentPosition])
def ShowStudentList():
    for student in StudentList:
        print("Nombre", student.name ,"Apellido",student.lastName,"Cédula",student.identificationCard,
              "Dirreción",student.address,"Telefono",student.phone,"email",student.email)
def StudentMenu():
    print("\033[;34m" + "\nSelecciona una opción\n"
     "\t1 - Agregar Estudiante\n"
     "\t2 - Eliminar Estudiante\n"
     "\t3 - Ver Estudiantes\n"
     "\t0 - Salir" + "\033[;23m")
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
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")