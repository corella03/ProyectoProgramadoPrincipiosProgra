from ClassLogic.CareerLogic import *
from ClassLogic.StudentLogic import *
def AddStudentToCareer():
    ShowCareerList()
    enterCareerPosition = int(input("\nIngrese el Estudiante que quiere Agregar a la carrera: "))
    careerList = GetCareerList()
    for i in range(len(careerList)):
        if i == enterCareerPosition:
            while True:
                print("1.. Asignar un Estudiante a una Carrera.\n"
                      "0.. Salir.")
                optionsEntry = input(" Ingrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        studentList = GetStudentList()
                        codeList = []
                        for j in range(len(studentList)):
                            codeList.append(studentList[j].identificationCard)
                            print("Nombre del Curso: ",studentList[j].name,
                                  " Cédula: ",studentList[j].identificationCard)
                        addCode = input(" Ingrese Cédula: ")
                        for o in codeList:
                            if o in addCode:
                                careerList[i].studentList.append(addCode)
                                print(careerList[i].studentList)
                        SetCareerList(careerList)
                    elif optionsEntry == "0":
                        break
                    else:
                        print("No has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes")
                else:
                    break
def DeleteStudentToCareer():
    ShowCareerList()
    enterCareerPosition = int(input("\nIngrese el Estudiante que quiere Eliminar de la Carrera: "))
    careerList = GetCareerList()
    for i in range(len(careerList)):
        if i == enterCareerPosition:
            deleteCode = input(" Ingrese la Cédula que desea eliminar: ")
            careerList[i].courseList.remove(deleteCode)
        else:
            print("No existe el Estudiante")
    SetCareerList(careerList)
def StudentToCarrerMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Asignar un Estudiante a una Carrera.\n"
          "\t2.. Desasignar un Estudiante una Carrera.\n"
          "\t0.. Volver al Menú Operativo.")
def StudentToCarrerMenuOptions():
    while True:
        StudentToCarrerMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddStudentToCareer()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeleteStudentToCareer()
        elif optionsEntry == "0" :
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")