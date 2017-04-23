from ClassLogic.CareerLogic import *
from ClassLogic.TeacherLogic import *
def AddTeacherToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Agregar Cursos: ")
    if not enterCareerPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            while True:
                print("1.. Asignar un Docente a una Carrera.\n"
                      "0.. Salir.")
                optionsEntry = input(" Ingrese una Opcion: ")
                if optionsEntry != "0":
                    if optionsEntry == "1":
                        teacherList = GetTeacherList()
                        codeList = []
                        for j in range(len(teacherList)):
                            codeList.append(teacherList[j].teacherIdentificationCard)
                            print("Nombre del Docente: ", teacherList[j].teacherName, " Cédula del Docente: ",
                                  teacherList[j].teacherIdentificationCard)
                        addCode = input("ingrese Cédula: ")
                        for o in codeList:
                            if o in addCode:
                                for k in careerList[i].teacherList:
                                    if k == addCode:
                                        print("Este Docente ya está Registrado en esta Carrera.")
                                        break
                                else:
                                    careerList[i].teacherList.append(addCode)
                                    print(careerList[i].teacherList)
                                    SetCareerList(careerList)
                                    break
                    elif optionsEntry == "0":
                        break
                    else:
                        print("No has pulsado ninguna opcion correcta... \n"
                              "Presione una tecla para volver a las Opciónes")
                else:
                    break
def DeleteTeacherToCareer():
    ShowCareerList()
    careerList = GetCareerList()
    enterCareerPosition = input("\nIngrese la Carrera que quiere Eliminar Docentes: ")
    if not enterCareerPosition.isdigit():
        print("Haz ingresado un dato que no es un número.")
        return
    for i in range(len(careerList)):
        if i == int(enterCareerPosition):
            deleteCode = input("Ingrese la Cédula que desea eliminar: ")
            if deleteCode in careerList[i].teacherList:
                careerList[i].teacherList.remove(deleteCode)
            else:
                print("No existe ese Cedula")
    SetCareerList(careerList)
def TeacherToCareerMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1.. Asignar un Docente a una Carrera.\n"
          "\t2.. Desasignar un Docente a una Carrera.\n"
          "\t0.. Volver al Menú Operativo.")
def TeacherToCareerMenuOptions():
    while True:
        TeacherToCareerMenu()
        optionsEntry = input("Ingrese la opción a Escoger: ")
        if optionsEntry== "1":
            AddTeacherToCareer()
            input("Pulsa una tecla para continuar.")
        elif optionsEntry == "2":
            DeleteTeacherToCareer()
        elif optionsEntry == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter para volver al Menú.")
TeacherToCareerMenuOptions()