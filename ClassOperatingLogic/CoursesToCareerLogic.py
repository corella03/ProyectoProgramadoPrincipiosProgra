from ClassLogic.CourseLogic import *
from ClassLogic.CareerLogic import *
codeList = []
def ListOfCoursesCodes():
    courseList = GetCourseList()
    for j in range(len(courseList)):
        codeList.append(courseList[j].courseCode)
        print("Nombre del Curso: ", courseList[j].courseName, " **Código del Curso: ", courseList[j].courseCode)
def AddCourseToCareer():
    careerList = GetCareerList()
    ShowCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Agregar Cursos: ")
    if not enterCareerPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            while True:
                print("1...Asignar un Curso a una Carrera.\n"
                      "0...Salir.")
                optionsEntry = input("\nIngrese una Opción: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        ListOfCoursesCodes()
                        addCode = input("\nIngrese el código del Curso a Asignar: ")
                        addCode = addCode.upper()
                        for o in codeList:
                            if o in addCode:
                                for k in careerList[i].courseList:
                                    if k == addCode:
                                        print("El Curso ya está en esta Carrera.")
                                        break
                                else:
                                    careerList[i].courseList.append(addCode)
                                    print("Asignación Correcta.\n")
                                    SetCareerList(careerList)
                        else:
                            print("El Código del Curso no Existe.\n")
                    elif optionsEntry == "0":
                        break
                    else:
                        print("\nNo has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciones.")
                else:
                    break
def DeleteCourseToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Eliminar Cursos: ")

    if not enterCareerPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            ListOfCoursesCodes()
            deleteCode = input("Ingrese el código del Curso que desea Eliminar: ")
            deleteCode = deleteCode.upper()
            if deleteCode in  careerList[i].courseList:
                careerList[i].courseList.remove(deleteCode)
                print("Desasignación Correcta.\n")
            else:
                print("No existe ese Curso.")
    SetCareerList(careerList)
def CourseToCarrerMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Asignar un Curso a una Carrera.\n"
          "\t2...Desasignar un Cursos a una Carrera.\n"
          "\t3...Visualizar las asignaciones de la Carrera.\n"
          "\t0...Volver al Menú Operativo.")
def CourseToCarrerMenuOptions():
    while True:
        CourseToCarrerMenu()
        optionsEntry = input("\nIngrese la opción a Escoger: ")
        if optionsEntry == "1":
            AddCourseToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteCourseToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            ShowAsignationToCareer()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
CourseToCarrerMenuOptions()