from ClassLogic.CourseLogic import *
from ClassLogic.CampusLogic import *
def AddCampusToCourses():
    ShowCourseList()
    enterCoursePosition = int(input("\nIngrese el Curso que quiere Agregarle Recintos: "))
    courseList = GetCourseList()
    for i in range(len(courseList)):
        if i == enterCoursePosition:
            while True:
                print("1.. Asignar un Recinto a un Curso.\n"
                      "0.. Salir.")
                optionsEntry = input(" Ingrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        campusList = GetCampusList()
                        codeList = []
                        for j in range(len(campusList)):
                            codeList.append(campusList[j].campusCode)
                            print("Nombre del Recinto: ",campusList[j].campusName," Código del Recinto: ",campusList[j].campusCode)
                        addCode = input("ingrese codigo")
                        for o in codeList:
                            if o in addCode:
                                for k in courseList[i].campusList:
                                    if k == addCode:
                                        print("El Recinto ya se asignó a este curso.")
                                        break
                                else:
                                    courseList[i].campusList.append(addCode)
                                    print(courseList[i].campusList)
                                    SetCourseList(courseList)
                                    break
                    elif optionsEntry == "0":
                        break
                    else:
                        print("No has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes")
                else:
                    break
def DeleteCampusToCourse():
    ShowCourseList()
    enterCoursePosition = int(input("\nIngrese el Curso que quiere Eliminarle Recintos: "))
    courseList = GetCourseList()
    for i in range(len(courseList)):
        if i == enterCoursePosition:
            deleteCode = input("Ingrese el codigo que desea eliminar")
            courseList[i].campusList.remove(deleteCode)
        else:
            print("No existe ese Curso")
    SetCourseList(courseList)
def CampusToCourseMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Asignar un Recinto a un Curso.\n"
          "\t2.. Desasignar un Recinto a un Curso.\n"
          "\t0.. Volver al Menú Operativo.")
def CampusToCourseMenuOptions():
    while True:
        CampusToCourseMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddCampusToCourses()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeleteCampusToCourse()
        elif optionsEntry == "0" :
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
CampusToCourseMenuOptions()