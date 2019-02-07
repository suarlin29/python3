##suarlin
## realizar el promedio n notas utilizando el for

n = 0
suma = 0

print ("ingresa las notas que quieras , ingresa 1 para detener el programa")

cantidad = int(input("ingresa la cantidad de notas que podras:. "))
for i in range(cantidad):
    n = int(input("ingrese notas:. "))
    suma = suma + n
cantidad = suma / cantidad
print("el promedio es:.{}".format(promedio))
