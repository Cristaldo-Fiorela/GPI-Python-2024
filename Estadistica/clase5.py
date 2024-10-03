import pandas;
import matplotlib.pyplot as plt;


# Crgar database con ubicacion del archivo
df = pandas.read_csv('Estadistica/csv/tabla_estudiantes.csv');

# Ver las primeras filas
print(df.head());

