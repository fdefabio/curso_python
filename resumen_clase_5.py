#tipos de listas

#listas
#en pyhton las listas son objetos
#son ordenadas mutables y permiten duplicados
frutas = ["Fresa" ,"Papaya", "Mango", "Pera", 5, True]
edades = [24, 15, 18]
evaluaciones = [3.5, 2 , 4.5]
#listas de listas
#una lista puede conteenr otra lista
ensayoListasDeListas = ["Carlos", [1,2,3], 52, True]
print(frutas[2])
print(len(frutas))#abreviatura de lenght-longitud
print(type(frutas))#el tipo de elemento
#mostrar secciones de una lista
print(frutas[1:4])
print(frutas[:4])#desde el principio hasta la cuarta posicion
#buscar una frase en una lista
print("Fresa" in frutas)
#agrega un elemento en la ultima posicion
frutas.append("Guanabana")
#sacar una copia de la lista
#se hace para no modificar la lista original
frutas2 = frutas.copy()
#contar elementos que coincidan
print(frutas.count("Mango"))
#indica la posicion de un elemento en la lista
print(frutas.index("Mango"))
#insertar en una posicion especifica
frutas.insert(2, "Guayaba")
#buscar en una lista de lista
print(ensayoListasDeListas[1][1])
#remover un elemento d ela lista
frutas.remove("Mango")
#remover un elemento por posicion
#si no se da una psocion elemina el ultimo
frutas.pop()
#las muestra reversadas
frutas.reverse()
#otra forma de crear listas llamando al metodo constructor de la clase list
marcas = list(("mazda", "Renault", "Fiat"))

############################################################################

#tuplas
frutasTupla = ("Mandarina", "Fresa"," Lulo")
#mostrar cpneo de un elemento
print(frutasTupla.count("Fresa"))
#posicion de un elemento
print(frutasTupla.index("Fresa"))
#otra forma de crear tuplas invocando el constructor de la clase tuple
frutasTuplas2 = tuple (("Papaya", "Piña", "Fresa"))

############################################################################

#diccionarios
#diccionarios no permiten elementos duplicados
#sus elementos tienen una llave y un valor asociado
carro = {"marca" : "mazda", 
         "modelo":"626", 
         "anio" : 1996, 
         "colores":["rojo","azul","verde"]}
#para mostrar un elemento, buscar por la llave
print(carro["modelo"])
print(carro["colores"][1])
print(carro.values())
print(carro.keys())
#sobreescribir un elemento
carro["marca"] = "renault"
#mostrar items del diccionario
print(carro.items())
#crear diccionario invocando al constructor de la clase dict
diccionario2 = dict (nombre = "diccionario", tipo = "educativo")