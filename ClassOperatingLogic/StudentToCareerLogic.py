from ClassLogic.StudentLogic import *
from ClassLogic.CourseLogic import *
from ClassLogic.CareerLogic import *
studentIdentificationCardList = []
def ListOfStudentIdentificationCards():
    studentList = GetStudenList()
    for j in range(len(studentList)):
        studentIdentificationCardList.append(studentList[j].identificationCard)
        print("Nombre del Estudiante: ", studentList[j].name," **Cédula: ", studentList[j].identificationCard)
def AddStudentToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Agregar al estudiante: ")
    if not enterCareerPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            while True:
                print("1...Asignar un Estudiante a una Carrera.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfStudentIdentificationCards()
                        addIdentificationCard = input("\nIngrese número de Cédula del Estudiante a Asignar: ")
                        addIdentificationCard = addIdentificationCard.upper()
                        for o in studentIdentificationCardList:
                            if o in addIdentificationCard:
                                for k in careerList[i].studentList:
                                    if k == addIdentificationCard:
                                        print("El Estudiante ya esta Matriculado en es Carrera.")
                                        break
                                else:
                                    careerList[i].studentList.append(addIdentificationCard)
                                    print("Asignación Correcta.\n")
                                    SetCareerList(careerList)
                                    break
                        else:
                            print("La Cédula ingresada no Existe.\n")
                    elif optionsEntry == "0":
                        break
                    else:
                        print("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciones.")
                else:
                    break
def DeleteStudentToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    courseList = GetCourseList()
    enterCareerPosition = input("\nIngrese el Estudiante que quiere Eliminar de la Carrera: ")
    if not enterCareerPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            ListOfStudentIdentificationCards()
            deleteidentificationCard = input("\nIngrese la Cédula del Estudiante que desea eliminar: ")
            deleteidentificationCard = deleteidentificationCard.upper()
            if deleteidentificationCard in careerList[i].studentList:
                careerList[i].studentList.remove(deleteidentificationCard)
                for j in range(len(courseList)):
                    if deleteidentificationCard in courseList.studenList:
                        courseList[j].studentList.remove(deleteidentificationCard)
            else:
                print("No existe el Estudiante.")
    SetCourseList(courseList)
    SetCareerList(careerList)
def StudentToCarrerMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Estudiante a una Carrera.\n"
          "\t2...Desasignar un Estudiante una Carrera.\n"
          "\t3...Visualizar las asignaciones de la Carrera.\n"
          "\t0...Volver al Menú Operativo.")
def StudentToCarrerMenuOptions():
    while True:
        StudentToCarrerMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry== "1":
            AddStudentToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteStudentToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
StudentToCarrerMenuOptions()