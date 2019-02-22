##suarlin paz
## 8

print ("bienvenido al programa".center(50, "*"))
monedas1 = 0
monedas2 = 0
monedas3= 0
monedas4 = 0
monedas5 = 0
monedas6 = 0

tota1 = 0
tota2 = 0
tota3 = 0
tota4 = 0
tota5 = 0
tota6 = 0
total = 0

monedas1 = int(input("ingrese monedas de 5:."))
tota1 = monedas1 * 0.05
monedas2 = int(input("ingrese monedas de 10:."))
tota2 = monedas2 * 0.10
monedas3 = int(input("ingrese monedas de 12,5:."))
tota3 = monedas3 * 0.125
monedas4 = int(input("ingrese monedas de 25:."))
tota4 = monedas4 * 0.25
monedas5 = int(input("ingrese monedas de 50:."))
tota5 = monedas5 * 0.50
monedas6 = int(input("ingrese monedas de 1 volivar:."))
tota5 = monedas6 * 1

total = tota1 + tota2 + tota3 + tota4 + tota5 + tota6
print("la cantidad total de dinero que se tiene es de: ",total)
