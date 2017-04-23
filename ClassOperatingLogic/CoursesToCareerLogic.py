from sqlite3 import adapt

from ClassLogic.CareerLogic import *
from ClassLogic.CourseLogic import *
def AddCourseToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Agregar Cursos: ")
    if not enterCareerPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            while True:
                print("1.. Asignar un Curso a una Carrera.\n"
                      "0.. Salir.")
                optionsEntry = input(" Ingrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        courseList = GetCourseList()
                        codeList = []
                        for j in range(len(courseList)):
                            codeList.append(courseList[j].courseCode)
                            print("Nombre del Curso: ",courseList[j].courseName," Código del Curso: ",courseList[j].courseCode)
                        addCode = input("ingrese codigo")
                        addCode = addCode.upper()
                        for o in codeList:
                            if o in addCode:
                                for k in careerList[i].courseList:
                                    if k == addCode:
                                        print("El Curso ya está en esta Carrera.")
                                        break
                                else:
                                    careerList[i].courseList.append(addCode)
                                    print(careerList[i].courseList)
                                    SetCareerList(careerList)
                    elif optionsEntry == "0":
                        break
                    else:
                        print("No has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes")
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
            deleteCode = input("Ingrese el codigo que desea eliminar")
            if deleteCode in  careerList[i].courseList:
                careerList[i].courseList.remove(deleteCode)
            else:
                print("No existe ese Curso")
    SetCareerList(careerList)
def CourseToCarrerMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Asignar un Curso a una Carrera.\n"
          "\t2.. Desasignar un Cursos a una Carrera.\n"
          "\t0.. Volver al Menú Operativo.")
def CourseToCarrerMenuOptions():
    while True:
        CourseToCarrerMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1" :
            AddCourseToCareer()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "2" :
            DeleteCourseToCareer()
        elif optionsEntry == "0" :
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
CourseToCarrerMenuOptions()