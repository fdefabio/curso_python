#tipos de variable

"""python es un lenguaje de tipado dinamico, esto significa 
que las variables no necesitan ser definidas por tipo y su tipo puede 
cambiar"""

edad = 15
nombre = "nombre"
feliz = True
cantidad = 48.5



#operadores aritmeticos

a = 5
b = 2
resultado = a + b
print(resultado)
resultado = a - b
print(resultado)
resultado = a * b
print(resultado)
resultado = a / b
print(resultado)
resultado = a % b
print(resultado)
#division entera, elimina la parte que sobra y hace la division con enteros
resultado = a // b
print(resultado)

#operadores de comparacion

#igual que ==
print(a == b)
#diferente que !=
print(a != b)
#mayor que >
print(a > b)
#menor que <
print(a < b)
#mayor que >=
print(a >= b)
#menor que <=
print(a <= b)

#operadores logicos

"""es un tipo de operador que retorna un valor booleano"""

resultado = ( a < b ) or (  a >= b )  or ( b == a)
print(resultado)

resultado = (a < b) and ( a == 5 ) 
print(resultado)