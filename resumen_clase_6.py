#programacion funcional
#funcion lamda
#debemos llamar a la funcion lambda

x = lambda a : a  + 10 

y = lambda a, b : a  * b 

print(x(12))
print(y(8, 6))

#metodo filter

edades = [2, 8, 52, 15, 16, 41]

def mayorDeEdad(x):
    if x < 18:
        return False
    else:
        return True

adultos = filter(mayorDeEdad, edades)

for element in adultos:
    print(element)


#metodo map

#retornar la longitud
def miFuncion(n):
    return len(n)

x = map(miFuncion,("manzana", "piña", "cereza"))
for i in x:
    print(i)