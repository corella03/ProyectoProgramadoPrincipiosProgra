from ClassTypes.Teacher import *
teacherList = []
def AddTeacher():
    nameEntry = str(input("Ingrese el Nombre del Docente  :"))
    lastNameEntry = str(input("Ingrese el Apellido del Docente  :"))
    identificationCardEntry = str(input("Ingrese el número de Cédula del Docente:"))
    addressEntry = str(input("Ingrese el Lugar de Residencia del Docente  :"))
    phoneEntry = str(input("Ingrese el Numero de telefono del Docente  :"))
    emailEntry = str(input("Ingrese el Correo del Docente  :"))
    newTeacher = Teacher(nameEntry,lastNameEntry,identificationCardEntry,addressEntry,phoneEntry,emailEntry)
    teacherList.append(newTeacher)
def DeleteTeacher():
    option = input("Desea eliminar un Docente ? si/no:")
    if option == "si":
        deleteTeacher = int(input("Ingrese el número que desea eliminar :"))
        teacherList.remove(teacherList[deleteTeacher])
    else:
        print("Vuelva a las opciones anteriores")
def ShowTeacherList():
    for teacher in teacherList:
        print("Nombre del  Docente", teacher.teacherName, "Apellido del Docente ", teacher.teacherLastName, "Número de Cédula del Docente",
              teacher.teacherIdentificationCard, "Residencia del Docente", teacher.teacherResidency,
              "Telefono del Docente", teacher.teacherPhone,"Correo del Docente", teacher.teacherEmail)
def ModifyTeacher():
    modify = int(input("Ingrese el número del Docente que desea modificar:"))
    for x in range(len(teacherList)):
        if teacherList[x] == teacherList[modify]:
            while True:
                print("\t1...Modificar Nombre del Docente", "\n",
                      "\t2...Modifciar Apellido del Docente", "\n",
                      "\t3...Modificar el número de cédula del Docente", "\n",
                      "\t4...Modificar Residencia del Docente", "\n",
                      "\t5...Modificar Telefono del Docente", "\n",
                      "\t6...Modificar Correo del Docente", "\n",
                      "\t0...Salir")
                option = input("Por favor, Ingrese una opción :")
                if option != "0":
                    for i in teacherList:
                        if option == "1":
                            i.teacherName = input("Ingrese un Nombre Nuevo")
                        elif option == "2":
                            i.teacherLastName = input("Ingrese un Apellido Nuevo")
                        elif option == "3":
                            i.teacherIdentificationCard = input("Ingrese una cédula Nueva")
                        elif option == "4":
                            i.teacherResidency = input("Ingrese una Residencia Nueva")
                        elif option == "5":
                            i.teacherPhone = input("Ingrese un número Nuevo")
                        elif option == "6":
                            i.teacherEmail = input("Ingrese un Correo Nuevo")
                        else:
                            print("Ingrese un numero válido", "\n",
                                  "Regresar al menú")
                    else:
                        break

                    print("\033[;34mNombre:",i.teacherName + "\033[;23m", "\033[;34mApellido:",i.teacherLastName + "\033[;23m",
                          "\033[;34mCédula:", i.teacherIdentificationCard + "\033[;23m","\033[;34mDirección:", i.teacherResidency + "\033[;23m",
                          "\033[;34mNumero de Telefono:", i.teacherPhone + "\033[;23m", "\033[;34mEmail:",i.teacherEmail + "\033[;23m")
def TeacherMenu():
    print("\t========= SELECCIONE ======\n"
          "\t========= UNA OPCION  ======\n"
          "\t1.. Agregar Docente\n"
          "\t2.. Eliminar Docente\n"
          "\t3.. Ver Lista Docente\n"
          "\t4.. Modificar Docente\n"
          "\t0.. Volver al menú ")
def TeacherMenuOption():
    while True:
        TeacherMenu()
        option = input("Ingrese una opcion")
        if option == "1":
            AddTeacher()
            input("\npulsa una tecla para continuar")
        elif option == "2":
            DeleteTeacher()
            input("\npulsa una tecla para continuar")
        elif option == "3":
            ShowTeacherList()
            input("\npulsa una tecla para continuar")
        elif option == "4":
            ModifyTeacher()
            input("\npulsa una tecla para continuar")
        elif option == "0":
            break
            input("\npulsa una tecla para continuar")
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")