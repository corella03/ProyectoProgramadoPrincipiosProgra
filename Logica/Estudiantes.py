StudentList = []
def AddStudent():
    nameEntry = input("Ingrese el Nombre del Estudiante:")
    lastNameEntry = input("Ingrese el Apellido del Estudiante:")
    identificationCardEntry = input("Ingrese el número de Cédula del Estudiante:")
    addressEntry = input("Ingrese la Dirección donde vive el Estudiante:")
    phoneEntry = input("Ingrese el Número de Telefono del Estudiante:")
    emailEntry = input("Ingrese el email del Estudiante:")
    import Logica.Carrera
    StudentList.append(Logica.Carrera.Student().DataStudent(nameEntry,lastNameEntry,identificationCardEntry,addressEntry,
    phoneEntry,emailEntry))
    print(StudentList)
def DeleteStudent():
    enterStudentPosition = int(input("Ingrese el numero del estudiante que quiera eliminar:"))
    StudentList.remove(StudentList[enterStudentPosition])
def Menu():
    print("\033[;34m" + "\nSelecciona una opción\n"
     "\t1 - Agregar Estudiante\n"
     "\t2 - Eliminar Estudiante\n"
     "\t3 - Ver Estudiantes\n"
     "\t0 - Salir" + "\033[;23m")
def MenuOptions():
    while True:
        Menu()
        optionsEntry = input("Ingrese la Opción a Escoger")
        if optionsEntry == "1":
            AddStudent()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "2":
            DeleteStudent()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "3":
            print(StudentList)
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")
MenuOptions()





'''
def CreateFile():
    StudentFile = open("Student.txt", "w")
    StudentFile.close()
CreateFile()
def WriteFile():
    StudentFile = open("Student.txt", "a")
    StudentFile.write()
    StudentFile.close()
WriteFile()
def ReadAsList():
    StudentFile = open("Student.txt", "r")
    lineas = StudentFile.readlines()
    print(lineas)
    StudentFile.close()
'''