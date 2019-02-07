##suarli
##solicitar al usuario que seleccione una opcio
## 1 solicitar do numeros y elevar el primero elevado al segundo
## 2 solicitar tres numeros y elevar el primero al segundo y el resultado elevarlo al tercero

opcion = input("""seleciona entre 2 opciones )1 para elevar 2 numeros )
2 para elevar 3 numeros:.""")

if opcion == "1":
    print("escoger ingresa 2 numeros y elevar el primero x segundo")
    num1 = float(input("ingrese el numero 1:. "))
    num2 = float(input("ingrese el numero 2:. "))
    elevacion = num1**num2
    print("el resultado es. {}".format(elevacion))

elif opcion == "2":
        print("escogio ingresar 3 numeros y elevarlos entre si")
        num1 = float(input("ingresa el numero 1:. "))
        num2 = float(input("ingresa el numero 2:. "))
        num3 = float(input("ingresa el numero 3:. "))
        elevacion = num1**num2
        elevacion2 = elevacion**num3
        print("el resultado es. {}".format(elevacion2))
else:
    print("opcion incorrecta")
        
             
