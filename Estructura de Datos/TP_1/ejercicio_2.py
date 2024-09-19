"""
La universidad ahora pide un programa que permita cargar las notas de dos exámenes y obtener el promedio. Además deberá determinar si el alumno aprobó el último examen (nota mayor o igual a 7), en caso contrario informar que desaprobó.
Además se desea saber si el alumno mejoró, empeoró o mantuvo su desempeño entre ambos parciales. Para ello se deberá informar "Mejoró su desempeño" si la nota del segundo parcial es mayor que la del primero, "Mantuvo la nota" si ambas notas son iguales o "Empeoró su desempeño" si la nota del primer parcial es mayor que la del segundo.
Finalmente, la universidad desea saber si el alumno promocionó la materia (promedio mayor o igual a 7), debe rendir final (promedio mayor o igual a 4) o debe recursar.
"""

notas = [];

def valido(nota):
  if isinstance(nota, (int, float)):
    if (nota < 0 or nota > 10):
      print('Ingrese un valor valido.');
      return False;
    return True;
  elif isinstance(nota, str):
    nota_lower = nota.lower();
    if (nota_lower == 'ok'):
      return 'ok'
  else:
    print('Ingrese un valor valido.');
    return False

while (True):
  input_user = input("Ingrese las notas a cargar, cuando desea finalizar el proceso por favor escriba: 'ok' ");

  if (input_user.lower() == 'ok'):
    break;

  valor = float(input_user);
  if valido(valor):
    notas.append(valor);

def promedio(notas): 
  total = 0;
  cantidad = len(notas);

  for nota in notas:
    total += nota;

  promedio = total / cantidad;
  return promedio;

promedio_total = promedio(notas);

print(f"El promedio es: {promedio_total}");

def rendimiento(notas):
  ultimo_idx = len(notas) - 1;
  primera_nota = notas[0];
  ultima_nota = notas[ultimo_idx];

  if(primera_nota > ultima_nota):
    print('Empeoró su desempeño');
  elif(primera_nota == ultima_nota):
    print('Mantuvo la nota');
  else:
    print('Mejoró su desempeño');

rendimiento_total = rendimiento(notas);

if(promedio_total >= 7):
  print('Promocionó');
elif(promedio_total >= 4):
  print('Debe rendir final');
else:
  print('Debe recursar');