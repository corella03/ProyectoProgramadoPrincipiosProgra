from ClassLogic.StudentLogic import *
from ClassLogic.CourseLogic import *
from ClassLogic.CampusLogic import*
from ClassLogic.TeacherLogic import *
from ClassLogic.CareerLogic import *
from ClassLogic.ClassroomsLogic import *
from ClassLogic.ClassScheduleLogic import *
def MenuOptions():
    while True:
        print("\033[;34m" + "\nSelecciona una opción\n"
        "\t1 - Opciones Estudiante.\n"
        "\t2 - Opciones Docentes.\n"
        "\t3 - Opciones Carreras.\n"
        "\t4 - Opciones Cursos.\n"
        "\t5 - Opciones Recintos.\n"
        "\t6 - Opciones Aulas.\n"
        "\t7 - Opciones Horarios.\n"
        "\t0 - Volver al Menú Principal" + "\033[;23m")
        optionsEntry = input("Ingrese la Opción a Escoger")
        if optionsEntry == "1":
            StudentMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "2":
            TeacherMenuOption()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "3":
            CareerMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "4":
            CourseMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "5":
            CampusMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "6":
            ClassRoomsMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "7":
            ClassScheduleMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")