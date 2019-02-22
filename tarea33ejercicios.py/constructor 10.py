##suarlin paz
## 10
print ("bienvenido al programa".center(50, "*"))

print("""un trabajador necesita 0.5 metros cubicos de arena por metro cuadrado.ingrese las medidas de una pared
      y el largo y ancho en metros cuadrados para determinar los metros cubicosde
      arena necesarios""")
METROS2 = 0.5
largo = float(input("ingrese el largo de la pared en metros cuadrados"))
ancho = float(input("ingrese el ancho de la pared en metros cuadrados"))
total1 = (largo * ancho)
total2 = total1 * METROS2
print("la cantidad en metros cubicos es de:{}".format(total2))

