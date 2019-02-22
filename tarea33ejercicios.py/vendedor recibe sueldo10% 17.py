##suarlin paz
## 17

print("su sueldo al mes es de :.2500".center(50,"*"))

sueldo  = 2500
comicion = 0.10
ventas = 3
precio_de_ventas = int(input("ingrese precio de su venta:. "))
total_de_comicion = (ventas * precio_de_ventas) * comicion
total = sueldo + total_de_comicion
print("el total de comicion es de :.{}".format(total_de_comicion))
print("el total del mes es de :.{}".format(total))
