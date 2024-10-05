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

# A - Listado de aulas

print('======Listado de aulas=======');
print(f"{'Día':<5} {'Aula':<5}")

for dia in dias:
  if(es_par(dia)):
    print(f"{dia:<5} {aula_par:<5}");
  else:
    print(f"{dia:<5} {aula_impar:<5}");
