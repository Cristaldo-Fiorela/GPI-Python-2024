"""
Explique la razón por la cual se recomienda agrupar un conjunto de datos para el análisis estadístico.
- Esto permite trabajar de manera mas eficiente, abstrayendo aquello que nos interesa y organizando la informacion para su anaisis.
"""

import pandas

data = ['Alta', 'Sin afeccion', 'Sin afeccion', 'Moderada' , 'Moderada', 'Moderada', 'Leve', 'Leve', 'Alta', 'Moderada']

df = pandas.DataFrame(data, columns=['Niveles de Afectación']);

# Frecuencia Absoluta
absoluta = df['Niveles de Afectación'].value_counts();

# Frecuencia Relativa
relativa = df['Niveles de Afectación'].value_counts(normalize=True);

print('===Frecuencia absoluta===');
print(absoluta);

print();

print('===Frecuencia relativa===');
print(relativa);


