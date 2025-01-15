i = 2
while i < 12:
    print(i)
    i += 2
#ejercicio tabblas de multiplicar
tabla = int(input("cual tabla quiere que le muestre: "))
i = 1
#ciclo while
while i < 11:
    if i == 6:
        #rompe el ciclo
        break
    print(tabla,"X",i,"= ",i*tabla)
    i += 1
print("aqui ya salio del ciclo")    
##########################################################
tabla = int(input("cual tabla quiere que le muestre: "))
i = 1
while i < 11:
    i += 1
    if i == 6:
        #salta instruccion
        continue
    print(tabla,"X",i,"= ",i*tabla)
print("aqui ya salio del ciclo")   
##########################################################
#ciclo for
cadena = "cosita"
for x in cadena:
    print(x)
#----------------------------
posicion = 0
longitud = len(cadena)
while posicion <= longitud:
    print(cadena[posicion])
    posicion += 1
#-----------------------------
for x in range(5):
    print(x+1)
print("ya acabe")    