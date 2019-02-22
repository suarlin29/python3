##suarlin paz
## 18
print ("bienvenido al programa".center(50, "*"))

print("""el cliente desea saber cuanto pagara de su totalde la compra si se ofrece
      un descuentodel 15% de la misma""")
DESCUENTO = 0.15
compra = float(input("ingrese el total de su compra:. "))
total = compra * DESCUENTO
print("el descuento es de. {}".format(total))
total2 = compra - total
print("el total a pagar es de . {}".format(total2))
