##suarlin paz
## 7
print ("bienvenido al programa".center(50, "*"))

URGENCIA = 0.35
PEDIATRIA = 0.42
TRAUMOTOLOGIA = 0.21
print("desea calcular presupuesto")
salida = input("ingresar presupuesto 1-si \n 2-no ")
while salida != 2:
    presupuesto = int(input("ingrese cantidad"))
    print("la cantidad es:.{}".format(presupuesto * URGENCIA))
    print("la cantidad es:.{}".format(presupuesto * PEDIATRIA))
    print("la cantidad es:.{}".format(presupuesto * TRAUMOTOLOGIA))
    salida = input("ingrese presupuesto 1-si \n 2-no ")

                      
    
