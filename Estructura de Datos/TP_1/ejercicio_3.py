"""
La universidad requiere un programa para organizar las aulas para los alumnos de primer año, de acuerdo al número de día, sabiendo que 1 es lunes y 6 es sábado.
a. Aulas: Desarrollar un programa que permita ingresar el número de día entre 1 y 6. Los días cuyo número de orden son pares los alumnos cursan en el aula A-300, mientras que aquellos días impares cursan en el aula A-315.
b. Descuento: Además se requiere un programa que otorgue un descuento especial del 25% en el valor de la cuota a aquellos alumnos que deseen cursar en el turno Tarde y se inscriban a más de 3 materias, para el resto de los casos el descuento será de un 5%. El programa debe imprimir el valor de la cuota con descuento de acuerdo al caso.
c. Estacionamiento: También se requiere que el programa asigne un costo diario de estacionamiento de $ 300 a aquellos alumnos que vengan en auto o en moto y de $ 50 si vienen en bicicleta.
"""

# Variables default
dia = 1;
par = False;
aula_par = 'A-300';
aula_impar = 'A-315';

# VALIDACIONES
def valido(dia):
  if(dia > 6 or dia < 1):
    print('Ingrese un valor valido del 1 al 6');
    return True
  else:
    return False;

while (True):
  dia = int(input('Ingrese su dia en un rango de 1 a 6: '));

  if not valido(dia):
    break;

# A
def es_par(dia):
  if (dia % 2 == 0):
    return True;
  else:
    return False;


def aula_disponible(dia):
  resultado = es_par(dia);

  if(resultado):
    print(f'Los alumnos cursan en el aula {aula_par}');
  else:
    print(f'Los alumnos cursan en el aula {aula_impar}');

aula = aula_disponible(dia);
