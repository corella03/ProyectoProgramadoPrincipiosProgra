
dominio = "@est.utn.ac.cr"
while True:
    x = input("ingrese correo")
    if "@" in x:
        print("vuelve a ingresarlo")
    else:
        x=x+dominio
        break
print(x)