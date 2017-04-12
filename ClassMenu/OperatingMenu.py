from ClassOperatingLogic.CampusToCoursesLogic import *
from ClassOperatingLogic.ClassRoomsToCoursesLogic import *
from ClassOperatingLogic.ClassScheduleToCoursesLogic import *
from ClassOperatingLogic.CoursesToCareerLogic import *
from ClassOperatingLogic.StudentToCoursesLogic import *
from ClassOperatingLogic.TeacherToCareerLogic import *
from ClassOperatingLogic.TeacherToCoursesLogic import *
from ClassOperatingLogic.StudentToCareerLogic import *
def OperatingMenuOptions():
    while True:
        print("\nSelecciona una opción\n"
               "\t1 - Asignar Cursos a Carreras.\n"
               "\t2 - Asignar Recintos a Cursos.\n"
               "\t3 - Asignar Aulas a Cursos.\n"
               "\t4 - Asignar Horarios a Cursos .\n"
               "\t5 - Asignar Docentes a Cursos.\n"
               "\t6 - Asignar Docentes a Carreras.\n"
               "\t7 - Asignar Estudiantes a Cursos.\n"
               "\t8 - Asignar Estudiantes a Carreras.\n"
               "\t0 - Volver al Menú Principal")
        optionsEntry = input("Ingrese la Opción a Escoger")
        if optionsEntry == "1":
            CourseToCarrerMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "2":
            CampusToCourseMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "3":
            ClassRoomsToCoursesMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "4":
            ClassScheduleToCourseMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "5":
            TeacherToCoursesMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "6":
            TeacherToCareerMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "7":
            StudentToCourseMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "8":
            StudentToCarrerMenuOptions()
            input("\npulsa una tecla para continuar")
        elif optionsEntry == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú")