# El ejercisio consiste en predecir el coste de un incidente de seguridad en base al 
# al número de equipos que se han visto afectados.

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#Generación del conjunto de datos 
x = 2 * np.random.rand(100,1)
y = 4 + 3 * x + np.random.randn(100,1)

print('La longitud del conjunto de datos es: ', len(x))

# Visualización del conjunto de datos 
plt.plot(x, y, "b.")
plt.xlabel('Equipos afectados (u/1000)')
plt.ylabel('Coste del incidente (u/10000)')
#plt.show()

# Modificación del conjunto de datos 
data = {'n_equipos_afectados': x.flatten(), 'coste': y.flatten()}
df = pd.DataFrame(data)
#print(df.head(10))

# Escalado del número de equipos afectados
df['n_equipos_afectados'] = df['n_equipos_afectados'] * 1000
df['n_equipos_afectados'] = df['n_equipos_afectados'].astype('int')
# Escalado del coste
df['coste'] = df['coste'] * 10000
df['coste'] = df['coste'].astype('int')
#print(df.head(10))

# Representación gráfica del conjunto de datos
plt.plot(df['n_equipos_afectados'], df['coste'], 'b.')
plt.xlabel('Equipos afectados')
plt.ylabel('Coste del incidente')
plt.show()