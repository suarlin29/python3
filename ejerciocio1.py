##suarlin
##crear un programa que permita una de dos opciones de combertir dolares
## a quetzalez o de quetzalez a dolares el usuario escoge una opcion
## y si no es ninguna de las dos no es valida


print("Bienvenido al programa".center (50,"*"))

dolar = 7.5
print("selecciona el tipo de cambio que desehe hacer 1 para dolar y 2 para quetzalez")
cambio = int(input("ingrse 1 o 2 para el cambio que va hacer.: "))
if cambio == 1:
  dolar = float(input("ingrese la cantida de dolar que desea cambiar.:"))
  resultado = dolar * dolar
  print("el cambio de quetz {}".format(resultado))
elif cambio == 2:
    quetz = float(input("ingrese la cantida de quetz que desea cambiar.: "))
    resultado2 = quetz / dolar
    print ("el cambio de dolar {}".format(resultado2))
else:
       print(" si no es ninguno de los dos datos no valido")
