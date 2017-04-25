from ClassLogic.TeacherLogic import *
from ClassLogic.CareerLogic import *
teacherIdentificationCardList = []
def ListOfTeacherIdentificationCards():
    teacherList = GetTeacherList()
    for j in range(len(teacherList)):
        teacherIdentificationCardList.append(teacherList[j].teacherIdentificationCard)
        print("Nombre del Docente: ", teacherList[j].teacherName, " **Cédula del Docente: ",teacherList[j].teacherIdentificationCard)
def AddTeacherToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Agregar Docentes: ")
    if not enterCareerPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            while True:
                print("1...Asignar un Docente a una Carrera.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfTeacherIdentificationCards()
                        addIdentificationCard = input("\nIngrese número de Cédula del Docente a Asignar: ")
                        addIdentificationCard = addIdentificationCard.upper()
                        for o in teacherIdentificationCardList:
                            if o in addIdentificationCard:
                                for k in careerList[i].teacherList:
                                    if k == addIdentificationCard:
                                        print("Este Docente ya está Registrado en esta Carrera.")
                                        break
                                else:
                                    careerList[i].teacherList.append(addIdentificationCard)
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
def DeleteTeacherToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    courseList = GetCourseList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Eliminar Docentes: ")
    if not enterCareerPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            ListOfTeacherIdentificationCards()
            deleteCode = input("Ingrese la Cédula del Docente que desea eliminar: ")
            if deleteCode in careerList[i].teacherList:
                careerList[i].teacherList.remove(deleteCode)
                for j in range(len(courseList)):
                    if deleteCode in courseList[j].teacherList:
                        courseList[j].teacherList.remove(deleteCode)
        else:
            print("No existe ese Cedula.")
    SetCourseList(courseList)
    SetCareerList(careerList)
def TeacherToCareerMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Docente a una Carrera.\n"
          "\t2...Desasignar un Docente a una Carrera.\n"
          "\t3...Visualizar las asignaciones de la Carrera.\n"
          "\t0...Volver al Menú Operativo.")
def TeacherToCareerMenuOptions():
    while True:
        TeacherToCareerMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1":
            AddTeacherToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteTeacherToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
TeacherToCareerMenuOptions()