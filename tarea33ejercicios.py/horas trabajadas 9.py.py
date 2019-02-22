##suarlin paz
## 9

print ("bienvenido al programa".center(50, "*"))

v = 0
h = 0
h_e = 0
valor_horas = int(input("valor de las horas"))
hora = int(input("horas trabajadas"))
horas_extras = int(input("horas extras laboradas"))
v = int(valor_horas) *int(hora)
h = int(valor_horas) * int(horas_extras) * int(2)
h_e = int(valor_horas) + int(valor_horas) * int(horas_extras) * int(2)
print("su sueldo normal es:. {}".format(v))
print("su sueldo extra es:. {}".format(h))
print("el total es:. {}".format(h_e))

