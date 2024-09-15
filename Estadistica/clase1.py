print('Hola Mundo');

# Comentario de 1 linea

"""
esto
es
un
comentario
"""

# VARIABLES
texto = 'Mi nombre es Fiorela';
edad = '25';
edad2 = 25;

"""
int: numeros enteros
float: numeros decimales
str: string
bool: bolean true/false
"""

# OPERADORES
# + - * % /         ** (potencia)

# OPERADORES DE ASIGNACION
# = , +=, -=, *=, /=

# OPERADORES DE COMPARACION
# ==, !=, < (menor), > (mayor), <=, >=

# OPERADORES DE COMPARACION
# &, || or, not

# ENTRADA DE VARIABLES
entrada = input('Ingrese su altura:');
print(entrada);

# CONDICIONES
if edad2 >= 18:
  print('Sos mayor de edad');
else:
  print('Sos menor de edad');

contador = 0;
while contador < 5:
  print(contador);
  contador += 1;
# llega hasta 5 porque entra, suma al 4 y ya la 6ta vez q evalua ya es 5 y no suma.

# ESTRUCTURAS DE CONTROL
colores = ["rojo", "azul", "amarillo"];
for color in colores:
  print(color);

# FUNCIONES
def promedio(notas1, nota2):
  suma = notas1 + nota2;
  media = suma / 2;
  print(media);

promedio(10, 5);

# MODULOS
"""
Son parte de las librerias
Son archivos que contienen definiciones y declaraciones
Se utilian para organizar el codigo y facilitar
"""

# PSEUDOCODIGO
nombre = input('Cual es tu nombre? ');
edad3 = input('Que edad tienes? ');

print(f"Hola {nombre}, tienes {edad3} años");

base = input('Ingrese el tamaño base de su triangulo: ');
altura = input('Ingrese la altura de su triangulo: ');

def triangulo(base, altura):
  area = int(base) * int(altura);
  print(f"El área del triángulo ingresado es: {area}")

triangulo(base, altura);

numero = int(input('Ingrese un número entero: '))

def par_o_inpar(num):
  resultado = num % 2;
  if resultado == 0:
    print(f'{num} es PAR');
  else:
    print(f'{num} es INPAR');

par_o_inpar(numero);

