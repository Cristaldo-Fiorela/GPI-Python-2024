'''
La universidad está mejorando sus sistemas y ha solicitado lo siguiente:
  a. Listado de aulas: 
    desarrollar un programa que muestre en dos columnas el número de día y el aula, de acuerdo al número de día par o impar desarrollado en el ejercicio anterior.
    Imprimir el listado como el siguiente:
    Día Aula
    1 A-315
    2 A-300
    ...
    5 A-315
    6 A-300
  b. Carga de edades: 
    se desea mejorar el sistema de carga de edades, validando que correspondan a mayores de edad. Desarrollar un programa que solicite edades válidas e imprima la edad ingresada y cuántas cargas erróneas se realizaron.
  c. Promedio de notas: 
    cargar las notas de 5 alumnos y obtener el promedio (for). Nota: Al usar for probar cómo se podría plantear el ejercicio usando 1, 2 o 3 parámetros.
  d. Costo del comedor: 
    Finalmente se pide calcular el costo del comedor. La cuota vale $ 1250 por día y se desea imprimir un informe que muestre la cantidad de días (de 1 a 6) y el costo total (for). Por ejemplo: 1 día cuesta $ 1250, 2 días cuestan $ 2500
'''

# VARIABLES A UTILIZAR
dias = [1, 2, 3, 4, 5, 6]
aula_par = 'A-300';
aula_impar = 'A-315';
contador = 0;
notas = [];
cantidad = 0;

# UTILS
def es_par(num):
  """
    Verifica si un día dado es par.

    Args:
      num (int): Un número entero que representa el día de la semana.

    Returns:
      bool: 
        - True si el número es par.
        - False si el número es impar.
  """
  if (num % 2 == 0):
    return True;
  else:
    return False;

def mayor_de_edad(num):
  """
    Verifica si el numero ingresado es mayor o igual a 18.

    Args:
      num (int): Un número entero que representa la edad de la persona.

    Returns:
      bool: 
        - True si es igual o mayor a 18.
        - False si es menor a 18.
  """
  if (num >= 18):
    return True;
  else:
    return False;

def promedio(num_list):
  """
    Saca el promedio total de una lista de numeros.

    Args:
      num_list (list): Lista de numeros.

    Returns:
      promedio (float)
  """ 
  total = 0;
  cantidad = len(num_list);

  for num in num_list:
    total += num;

  promedio = total / cantidad;
  return promedio;

# A - Listado de aulas

print('======Listado de aulas=======');
print(f"{'Día':<5} {'Aula':<5}")

for dia in dias:
  if(es_par(dia)):
    print(f"{dia:<5} {aula_par:<5}");
  else:
    print(f"{dia:<5} {aula_impar:<5}");

# B - Carga de edades
print('=======Carga de edades=======');

while(True):
  edad = int(input('Ingrese una edad mayor o igual a 18: '));
  
  if not (mayor_de_edad(edad)):
    print('error! ', end='')
    contador += 1;
  
  if (mayor_de_edad(edad)):
    break

print(f'La edad ingresada es: {edad}');
print(f'Se ha ingresado la edad erroneamente {contador} veces');

# C - Promedio de Notas

while(True):
  a_cargar = int(input('Cuantas notas desea cargar? '))

  if not (a_cargar <= 0):
    break

for i in range(a_cargar):
  while (True):
    nota = float(input('Ingrese la nota: '));

    if(nota <= 0 or nota > 10):
      print("Nota inválida. Por favor, ingrese una nota en el rango de 1 a 10.")
    else:
      notas.append(nota);
      break

promedio_total = promedio(notas);
print(f'El promedio de notas es: {promedio_total}');