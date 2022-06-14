# El ejercisio consiste en predecir el coste de un incidente de seguridad en base al 
# al número de equipos que se han visto afectados.

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

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
#plt.show()

# Construcción del modelo 
#Construcción del modelo y ajuste de la función hipótesis
lin_reg = LinearRegression()
lin_reg.fit(df['n_equipos_afectados'].values.reshape(-1,1), df['coste'].values)

# Parámetro theta 0
print(lin_reg.intercept_)
# Parámetro theta 1
print(lin_reg.coef_)

# Predicción para el valor mínimo y máximo del conjunto de datos de entrenamiento
X_min_max = np.array([[df['n_equipos_afectados'].min()], [df['n_equipos_afectados'].max()]])
Y_train_pred = lin_reg.predict(X_min_max)

# Representación gráfica de la función hipótesis generada
plt.plot(X_min_max, Y_train_pred,'g-')
plt.plot(df['n_equipos_afectados'], df['coste'],'b.')
plt.xlabel('Equipos afectados')
plt.ylabel('Coste del incidente')
plt.grid(True)
plt.show()

# Predicción de nuevos ejemplos
x_new = np.array([[1200]])
coste = lin_reg.predict(x_new)
print('El coste del incidente sería:', int(coste[0]), "$")