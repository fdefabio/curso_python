#Estructuras de control de flujo: se refiere al flujo que va teniendo el programa

edad = 20

if edad >= 18: 
    print("La persona es mayor de edad")
else:
    print("La persona es menor de edad")

######################################################################
sexo = 'M'

if sexo == 'M':
    print("masculino")
elif sexo == 'F':
    print("femenino")
else:
    print("otro")        

#######################################################################

#si no se especifica el tipo de entrada la tomara como una cadena de caracteres
edad = int(input("Ingrese su edad:"))

if edad >= 0 and edad < 6:
    print("primera infancia")
    print("es un pequeño bebe")
elif edad >= 6 and edad < 14:
    print("infancia")
elif edad >= 14 and edad < 18:
    print("adolescencia")
elif edad >= 18 and edad < 116:
    print("adulto")     
else:
    print("edad incorrecta")

print("esta se ejecuta siempre")    
#python agrupa funciones segun la identacion