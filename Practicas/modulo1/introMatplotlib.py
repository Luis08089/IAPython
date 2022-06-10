import matplotlib
import matplotlib.pyplot as plt

#Mostrar los graficos integrados dentro de jupyter notebook
#%matplotlib inline 

#REPRESENTACION GRAFICA DE DATOS 
#Si a la funcion de trazado se le da una matriz de datos, la usara como coordenadas en ele eje vertical, 
# y utilizara el indice de cada punto de datos en el array como la coordenada horizontal
lista = [1,2,5,7,8,3,1]
#plt.plot(lista)
#plt.show()

#Tambien se puede proporcionar dos matrices: una para el eje horizontal y otra para el eje vertical
lista2 = [1,4,6,7,8,9,10]
#plt.plot(lista2, lista) 
#plt.show()
#Pueden modificarse las longitudes de los ejes para que la figura no se vea tan ajustada
#plt.plot([-3,-1,0,4,7], [1,4,6,7,8])
#plt.show()

#plt.axis([-4,8,0,10])
#plt.show()

#Se sigue el mismo procedimiento para pintar una funcion matematica
import numpy as np

x = np.linspace(-2,2,500)
y = x**2 
#plt.plot(x,y)
#plt.show()

#Tambien puede modificarse el estilo de la grafica para que contenga mas informacion
#plt.plot(x,y)
#plt.title('Square function')
#plt.xlabel('x')
#plt.ylabel('y = x^2')
#plt.grid(True)
#plt.show()

#Pueden superponerse graficas y cambiar el estilo de las lineas
y2 = x+1
#plt.plot(x,y,'b--',x,y2,'g')
#plt.show()

#Para poder diferenciar entre ambas funciones siempre es recomendable añadir una leyenda
#plt.plot(x,y,'b--', label='x^2')
#plt.plot(x,y2,'g', label='x+1')
#plt.legend(loc='best')
#plt.show()

#Tambien puede crearse dos graficas que no se superpongan. Estas graficas se organizan en un
#grid y se denominan subplots
#plt.subplot(1,2,1)
#plt.plot(x,y,'b--')

#plt.subplot(1,2,2)
#plt.plot(x,y2,'g')
#plt.show()

#Para que las gráficas no queden tan ajustadas, podemos hacer la figura más grande
#plt.figure(figsize=(14,6))
#plt.subplot(1,2,1)
#plt.plot(x,y,'b--')
#plt.xlabel("x1", fontsize=14)
#plt.ylabel("Y1", fontsize=14)

#plt.subplot(1,2,2)
#plt.plot(x,y2,'g')
#plt.xlabel("x2", fontsize=14)
#plt.ylabel("Y2", fontsize=14)
#plt.show()

# SCATTER PLOTS
from numpy.random import rand

x,y = rand(2,100)
x2,y2 = rand(2,100)

#plt.scatter(x,y, c='red')
#plt.scatter(x2,y2, c='blue')
#plt.show()

#HISTOGRAMAS
data = [1,1.1,1.8,2,2.1,3.2,2,2,3,3,3]
#plt.subplot(211)
#plt.hist(data, bins=15, rwidth=0.8)
#plt.xlabel("Value")
#plt.ylabel('Frecuency')
#plt.show()

#GUARDAR LAS FIGURAS
x = np.linspace(-2,2,500)
y = x**2
y2 = x+1

#plt.plot(x,y,'b--',label="x^2")
#plt.plot(x,y2,'g', label='x+1')
#plt.legend(loc='best')

#plt.savefig("mi_grafica.png", transparent=True)