import ClassLogic.StudentLogic
def MenuOptions():
    while True:
        print("\033[;34m" + "\nSelecciona una opción\n"
        "\t1 - Opciones Estudiante.\n"
        "\t2 - Opciones Docentes.\n"
        "\t3 - Opciones Carreras.\n"
        "\t4 - Opciones Carreras.\n"
        "\t5 - Opciones Cursos.\n"
        "\t6 - Opciones Recintos.\n"
        "\t7 - Opciones Aulas.\n"
        "\t8 - Opciones Horarios.\n"
        "\t0 - Salir" + "\033[;23m")
        optionsEntry = input("Ingrese la Opción a Escoger")
        if optionsEntry == "1":
            ClassLogic.StudentLogic.StudentMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "2":
            print("Estamos Trabando en esto :D")
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "3":
            print("Estamos Trabando en esto :D")
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "4":
            print("Estamos Trabando en esto :D")
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "5":
            print("Estamos Trabando en esto :D")
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "6":
            print("Estamos Trabando en esto :D")
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "7":
            print("Estamos Trabando en esto :D")
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "8":
            print("Estamos Trabando en esto :D")
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")