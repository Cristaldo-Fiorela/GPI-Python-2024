"""
Crear un programa que permita registrar las inscripciones de los alumnos de una universidad
privada. Debe incluir un título principal, pedir los datos personales (nombre, edad, fecha de
nacimiento). Crear una variable que muestre True o False si posee título secundario (ese
dato no se pide al usuario, se escribe en el programa).
Además se deberá ingresar el monto de matrícula y calcular la cuota (valor de la matrícula +
$ 1000).
La materia "Python I" tiene un arancel especial, cuyo valor es $ 12000 por cuatrimestre.
Mostrar el costo mensual y calcular un descuento del 15% de la cuota para aquellos que
paguen en efectivo.
Finalmente se deberán imprimir todos los datos pedidos.
"""
matricula = float(input('Ingrese el valor de la matricula: '));
cuota = 1000;
python_I = 12000;
descuento = 0.15;
titularidad = 1;

nombre = input('Cual es tu nombre? ');
edad = input('Cual es tu edad? ');
nacimiento = input('Cuando naciste? ');

def valor_cuota (matricula, cuota):
  return matricula + cuota;

def costo_mensual(costo_cuatrimestral):
  return float(costo_cuatrimestral / 4);

def descuento_cuota(descuento, mensual):
  a_restar = (mensual * descuento);
  total = mensual - a_restar;
  return total;

def titulo(boolean):
  if (boolean == 1):
    return 'True'
  else:
    return 'False'

total_cuota = valor_cuota(matricula, cuota);
valor_cuota_mensual = costo_mensual(python_I);
valor_cuota_descuento = descuento_cuota(descuento, valor_cuota_mensual);
posee_titulo = titulo(titularidad);

print('================================================');
print('=====Universisas de python - Inscripciones =====');
print('================================================');
print()

print('DATOS DE INGRESO: ');
print(f'Nombre completo: {nombre}');
print(f'Fecha de nacimiento y edad: {nacimiento} ({edad})');
print(f'Posee titulo?: {posee_titulo}');
print(f'Matricula: {matricula}');
print(f'Cuota Mensual: {total_cuota}');
print(f"Aracel mensual materia 'Python I': {valor_cuota_mensual}");
print(f"Aracel mensual materia 'Python I' con descuento: {valor_cuota_descuento}");
