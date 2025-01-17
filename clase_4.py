#funciones y modularidad
"""una funcion es una fraccion de codigo que escribo y 
puedo invocar varias veces dentro del flujo de la plicacion"""

#funcion que no devuelve valores ni recibe parametros

def miFuncion():
    print("hola mundo")

print("estamos haciendo un ensayis")
a = 222
miFuncion()
print(a)     

 #############################################################
#funcion que recibe parametros

def funcionConParametros(nombre):
    print(nombre)

funcionConParametros("pedrito")

def funcionConParametros(a, b):
    print("el resultado de la suma es: ")

numero1 = int(input("ingrese primer valor "))
numero2 = int(input("ingrese segundo valor "))
funcionConParametros(numero1, numero2)

###############################################################
#funcion que retorna valores

def suma(a, b):
    return a+b

print(suma(8,9))