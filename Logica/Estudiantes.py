import sys
listaEstudiantes = []
class Estudiante():
    def AgregarEstudiante (self):
        ingresoNombre = input("Ingrese Nombre")
        ingresoApellido = input("Ingrese Apellido")
        ingresoDireccion = input("Ingrese Dirección")
        ingreseTelefono = input("Ingrese el Número")
        ingresoCorreo = input("Ingrese Correo")
        listaEstudiantes.extend([[ingresoNombre,ingresoApellido,ingresoDireccion,ingreseTelefono,ingresoCorreo]])
        print(listaEstudiantes)
        return listaEstudiantes
    def EliminarEstudiante(self):
        ingresoPosicionEstudiante = int (input("Ingrese La poscion del Estudiante:"))
        listaEstudiantes.remove(listaEstudiantes[ingresoPosicionEstudiante])
        print(listaEstudiantes)
def menu():
    while True:
        print("\033[;34m" + "\nBienvenido ADMIN \n"
        "Selecciona una opción\n"
        "\t1 - Agregar Estudiantes\n"
        "\t2 - Eliminar Estudiantes\n"
        "\t3 - Ver Lista Estudiantes\n"
        "\t0 - Salir\n" + "\033[;23m")
        ingresoOpcion = input("Elija")
        if ingresoOpcion == "1":
            Estudiante().AgregarEstudiante()
        elif ingresoOpcion == "2":
            Estudiante().EliminarEstudiante()
        elif ingresoOpcion == "3":
            print(listaEstudiantes)
        elif ingresoOpcion == "0":
            sys.exit()
menu()