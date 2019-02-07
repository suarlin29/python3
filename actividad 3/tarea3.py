##suarlin
##realiza un promedio de 5 notas untilizando el ciclo for



suma = 0
print("bienvenido al programa".center(50,"*"))
print("ingrese 5 notas para saber su promedio")

for i in range(5):
    n = int(input("ingresa notas :. "))
    suma = suma + n
promedio = suma / 5
print("el promedio es:. {}".format(promedio))
