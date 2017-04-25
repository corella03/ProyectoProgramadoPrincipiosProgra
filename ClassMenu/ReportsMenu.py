from ClassLogic.StudentLogic import *
from ClassLogic.TeacherLogic import *
from ClassLogic.CourseLogic import *
from ClassLogic.CareerLogic import *
import time
def Report1():
    careerList = GetCareerList()
    studentList = GetStudenList()
    for student in studentList:
        print(" Nombre: ", student.name, " Apellido: ", student.lastName,
              " Cédula: ",student.identificationCard)
    studentIdentificationCard = input("Ingrese Cédula del Estudiante: ")
    studentExist = False
    for i in range(len(careerList)):
        for j in range(len(careerList[i].studentList)):
            if studentIdentificationCard == careerList[i].studentList[j]:
                studentExist = True
                print("El Estudiante:", studentIdentificationCard," Pertenece a la Carrera: ",careerList[i].name)
                break
    print(time.strftime('%d %b %y'))
    print(time.strftime('%H:%M:%S'))
    if not studentExist:
        print("No existe el Estudiante.")
def Report2():
    careerList = GetCareerList()
    studentList = GetStudenList()
    allCourse = GetCourseList()
    studentExist = False
    for student in studentList:
        print(" Nombre: ", student.name, " Apellido: ", student.lastName,
              " Cédula: ", student.identificationCard)
    studentIdentificationCard = input("Ingrese Cédula del Estudiante: ")
    for i in range(len(careerList)):
        for j in range(len(careerList[i].studentList)):
            if studentIdentificationCard == careerList[i].studentList[j]:
                studentExist = True
                print("El Estudiante:", studentIdentificationCard, " Pertenece a la Carrera: ", careerList[i].name,
                      " con los Cursos: ")
                #Recorremos a los id de los cursos de  cada carrera
                for courseId in careerList[i].courseList:
                    for course in allCourse:
                        if courseId == course.courseCode:
                            for studentId in course.studentList:
                                if studentId == studentIdentificationCard:
                                    print(course.courseName)
                break
    print(time.strftime('%d %b %y'))
    print(time.strftime('%H:%M:%S'))
    if not studentExist:
        print("No existe el Estudiante.")
def Report3():
    careerList = GetCareerList()
    teachertList = GetTeacherList()
    allCourse = GetCourseList()
    teacherExist =  False
    for teacher in teachertList:
        print(" Nombre: ", teacher.teacherName, " Apellido: ", teacher.teacherLastName,
              " Cédula: ", teacher.teacherIdentificationCard)
    teacherIdentificationCard = input("Ingrese Cédula del Docente: ")
    for i in range(len(careerList)):
        for j in range(len(careerList[i].teacherList)):
            if teacherIdentificationCard == careerList[i].teacherList[j]:
                teacherExist = True
                print("El Docente:", teacherIdentificationCard, " Pertenece a la Carrera: ", careerList[i].name,
                      " con los Cursos: ")
                # Recorremos a los id de los cursos de  cada carrera
                for courseId in careerList[i].courseList:
                    for course in allCourse:
                        if courseId == course.courseCode:
                            for teacherId in course.teacherList:
                                if teacherId == teacherIdentificationCard:
                                    print(course.courseName)
                break
    print(time.strftime('%d %b %y'))
    print(time.strftime('%H:%M:%S'))
    if not teacherExist:
        print("No existe el Estudiante.")
def Report4():
    careerList = GetCareerList()
    allCourse = GetCourseList()
    sorterCareerList = sorted(careerList, key = lambda career: len(career.studentList),reverse = True)
    for career in sorterCareerList:
        print("Carrera: ", career.name, " número de estudiantes Matriculados: ",len(career.studentList))
        for courseId in career.courseList:
            for course in allCourse:
                if courseId == course.courseCode:
                    print(" Curso", course.courseName)
    print(time.strftime('%d %b %y'))
    print(time.strftime('%H:%M:%S'))
def Report5():
    careerList = GetCareerList()
    allCourse = GetCourseList()
    sorterCareerList = sorted(careerList, key=lambda career: len(career.studentList))
    for career in sorterCareerList:
        print("Carrera: ", career.name, " número de estudiantes Matriculados: ", len(career.studentList))
        for courseId in career.courseList:
            for course in allCourse:
                if courseId == course.courseCode:
                    print(" Curso", course.courseName)
    print(time.strftime('%d %b %y'))
    print(time.strftime('%H:%M:%S'))
def Report6():
    allCourse = GetCourseList()
    #devuelve lista ordenada por algo
    #pirmerparametro = la lista a ordenar 2do:key=lambda la funcion de ordenamiento
    #lambda funcion anonima, y lo que hace es decir que ahi va una funcion
    #course ante de : es un parametro que es el que recibio lambda  y esa funcion retorda len(course.studentList)
    sorterCourseList = sorted(allCourse, key = lambda course: len(course.studentList), reverse=True)
    print(sorterCourseList[0].courseName,sorterCourseList[0].classScheduleList," cantidad de estudiantes matriculados :",
          len(sorterCourseList[0].studentList))
    print(time.strftime('%d %b %y'))
    print(time.strftime('%H:%M:%S'))
def Report7():
    careerList = GetCareerList()
    studentList = GetStudenList()
    allCourse = GetCourseList()
    studentExist = False
    for student in studentList:
        print(" Nombre: ", student.name, " Apellido: ", student.lastName,
              " Cédula: ", student.identificationCard)
    studentIdentificationCard = input("Ingrese Cédula del Estudiante: ")
    for i in range(len(careerList)):
        for j in range(len(careerList[i].studentList)):
            if studentIdentificationCard == careerList[i].studentList[j]:
                studentExist = True
                print("El Estudiante:", studentIdentificationCard, " Pertenece a la Carrera: ", careerList[i].name,
                      " con los Cursos: ")
                # Recorremos a los id de los cursos de  cada carrera
                for courseId in careerList[i].courseList:
                    for course in allCourse:
                        if courseId == course.courseCode:
                            for studentId in course.studentList:
                                if studentId == studentIdentificationCard:
                                    print(course.courseName," Recinto: ",course.campusList," Horario: ",course.classScheduleList)
                break
    print(time.strftime('%d %b %y'))
    print(time.strftime('%H:%M:%S'))
    if not studentExist:
        print("No existe el Estudiante.")
def ReportsMenu():
    print("\n========= SELECCIONE =========\n"
          "========= UNA OPCION =========\n"
          "\t1...Imprimir lista de Carreras a la que un Estudiante pertenece.\n"
          "\t2...Imprimir lista de Cursos por Carrera que un Estudiante pertenece.\n"
          "\t3...Imprimir lista de Cursos por Carrera que un Docente pertenece.\n"
          "\t4...Imprimir Curso por cada Carrera con más Estudiantes Matriculados.\n"
          "\t5...Imprimir Curso por cada Carrera con menos Estudiantes Matriculados.\n"
          "\t6...Imprimir el Horario de un Curso de una Carrera, donde más Estudiantes están Matriculados.\n"
          "\t7...Imprimir la Carrera, con los cursos, con el Recinto de cada Curso, con el Aula de cada Recinto,"
          " con el Horario de cada Curso de un Estudiante en específico.\n"
          "\t0...Volver al Menú Administrativo.")
def ReportsMenuOptions():
    while True:
        ReportsMenu()
        optionsEntry = input("\nIngrese la Opción a Escoger: ")
        if optionsEntry == "1":
            Report1()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "2":
            Report2()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "3":
            Report3()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "4":
            Report4()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "5":
            Report5()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "6":
            Report6()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "7":
            Report7()
            input("\nPulsa una tecla para continuar.")
        elif optionsEntry == "0":
            break
        else:
            input("\nNo has pulsado ninguna opción correcta...\n"
                  "Presione enter Para volver al Menú.")