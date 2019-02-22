##SUARLIN PAZ
## 25
print ("bienvenido al programa".center(50, "*"))
print("ingrese 2 numero enteros positivosy se mostrara la + y * de estos")
num1 = int(input("ingrese el numero 1:. "))
num2 = int(input("ingrese el numero 2:. "))

if num1 >=0 and num2 >=0:
    suma = num1 + num2
    multi = num1 * num2
    print("la suma de los dos numeros es de :. {}".format(suma))
    print("la multiplicacion de los dos numeros es de :. {}".format(multi))
else:
    print("solo numeros positivos")
