# IMPRIMIR EN CONSOLA
print('==========CONSOLA============')
saludo = 'hola';
print(saludo); # posee salto de linea
print("sin salto de linea", end='') #end='' hace que sea continuo y no pegue el salto de línea
print("en la comisión A") 
print()

cadena= "Pepe Argento"
print("Hola",cadena) #, agrega espacio intermedio
print("Hola"+cadena) #+ no agrega espacio intermedio
edad= 25
print("Hola",cadena, "mi edad es", edad) # Concatenamos
print("Hola",cadena, "mi edad es"+ str(edad)) #Parseamos entero a string
print(f"hola  mi noimbre es {cadena} y mi edad es {edad}") #inserta el valor de las variables en la impresion 

# SEPARADOR DE DATOS
print('==========SEPARADOR DE DATOS============')
print(11,22,33, sep=' * ') #es un asterisco la sepación
print(11,22,33, sep='\t') #es una tabulacion
print(11,22,33, sep='\n') #es un salto de línea
print(11,22,33, sep='\n\n') #es un doble salto de línea
print()

# TERMINADOR
print('==========TERMINADOR============')
print(11,22,33, end=' / ') #termina con una línea en vez de con 1 salto
print('otra línea')
print('nueva línea')
print()

# ENTRADA DE DATOS POR TECLADO
print('==========ENTRADA DE DATOS POR TECLADO============')
print('Cual es tu nombre?');
nombre = input();
print(saludo, nombre);

# EXPRESIONES
print('==========EXPRESIONES============')
d = 4
print(d is None) # Da False
d = ''
print(d is None) # Da False

d=None
print(d is None) # Da True

# SENTENCIAS
print('==========SENTENCIAS============')

# sentencia dividida en lìneas, mejora la ligibilidad de sentencias largas.
a= 2 + 3 + 4 + 5 \
+ 6 + 7 + 8 + \
9 
print(a);

c= [2, 3, 4,
5, 6, 7, 8,
9, 10] # continuación de línea implícita
print(c);

# CADENA DE CARACTERES
print('==========CADENA DE CARACTERES============')

dia="Viernes"
mes='Octubre'
print(dia+mes)
print(dia,mes)

apellido="Cristaldo"
print(apellido[0]) #Toma la cadena como un vector
print(len(apellido)) #Devuelve el largo de la cadena
print(apellido[7]) #Devuelve el 7mo valor

# Devuelve el ultimo valor.
print(apellido[len(apellido)-1]) #Es -1 porque arranca de 0.
print(apellido[-1]) #Pq el negativo siempre va al último caracter

#Programa para obtener el primer caracter, el último y el largo de la cadena
print('==========PROGRAMA CARACTERES============')
nombre = input("Ingrese su nombre: ")
primer_caracter = nombre[0]
largo_cadena = len(nombre)
ultimo_caracter= nombre[largo_cadena-1]
ultimo_caracter_2 = nombre[-1]

# ultimo_caracter= nombre[-1]
print("--------- INFORME ---------")
print("Primer caracter:", primer_caracter)
print("Último caracter v1:", ultimo_caracter)
print("Último caracter v2:", ultimo_caracter_2)
print("Largo de la cadena:", largo_cadena)


#Las cadenas son objetos, por lo tanto, tienen métodos
nombre_completo="carlos Martínez estrada"
print(nombre_completo.lower()) #minúsculas
print(nombre_completo.upper()) #mayúsculas
print(nombre_completo.capitalize()) #primer letra de la cadena
print(nombre_completo.title()) #primer letra de cada palabra