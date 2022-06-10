import numpy as np
#Creacion de arrays de valores 0
a = np.zeros((2, 4))
#input(a)
#input(a.shape)
#input(a.ndim)
#input(a.size)

#Creacionde arrays de valores 1
b = np.ones((3, 2, 4))
#input(b)

#Creacion de arrays cuyo valor son todos iguales al que se indica
c = np.full((2, 3, 4), 8)
#input(c)

#El resultado de np.empty no es predecible 
#Inicializa los valores del array utilizando una lista de Python
d = np.empty((2,3,9))
#input(d)

#Inicializacion del array utilizando una lista de Python
e = np.array([[1, 2, 3], [4, 5, 6]])
#print(e)

#Creación de array utilizando una funcion basada en rangos
#(minimo, maximo, número elementos de array)
#print(np.linspace(0,6,18))

#Inicializacion de un array con numeros aleatorios
#input(np.random.rand(2, 3, 4))

import matplotlib.pyplot as plt

c = np.random.randn(1000000)
plt.hist(c, bins=200)
#plt.show()

# ACCESO A LOS ELEMENTOS DE UN ARRAY

# Creación de un Array unidimensional
array_uni = np.array([1, 3, 5, 7, 9, 11])
#print(array_uni.shape)
#print(array_uni)

# Accediendo al quinto elemento del Array
#print(array_uni[4])

# Accediendo al tercer y cuarto elmento del Array 
#print(array_uni[2:4])

# Accediendo a los elmentos 0 y 3 del Array 
#print(array_uni[0:: 3])

# Creacion de un array multidimencional
array_multi = np.array([[1,2,3,4], [5,6,7,8]])

# Accediendo al curto elemento del Array
#print(array_multi[0, 3])

# Accediendo a la segunda fila del Array
#print(array_multi[1,:])

# Accediendo al tercer elemento de las dos primeras filas del Array
#print(array_multi[0:2, 2])

# MODIFICACION DE UN ARRAY

# Creacin de un array unidimensional inicializado con el rango de elementos 0-27
array1 = np.arange(28)
#print(array1)

# Cambiar las dimensiones del Array y sus longitudes
array1.shape = (7,4)
#print(array1)

# El ejemplo anterior devuelve un nuevo Array que apunta a los mismos datos. 
# Importante: Modificaciones en un Array, modificaran el otro Array
array2 = array1.reshape(4, 7)
#print("Shape:", array2.shape)
#print("Array 2:\n", array2)

# Modificación del nuevo Array devuelto
array2[0, 3] = 20
#print("Array 2:\n", array2)

#print("Array 1:\n", array1)

# Desenvuelve el Array, devolviendo un nuevo Array de una sola dimension
# Importante: El nuevo array apunta a los mismos datos
#print("Array 1:", array1.ravel())

# BROADCASTING

# Creación de dos Arrays unidimensionales
array1 = np.arange(5)
array2 = np.array([3])
#print("Shape Array 1:", array1.shape)
#print("Array 1:", array1)
#print()
#print("Shape Array 2:", array2.shape)
#print("Array 2:", array2)

# Suma de ambos Arrays
array1 + array2

# Creación de dos Arrays multidimensional y unidimensional

array1 = np.arange(6)
array1.shape = (2, 3)
array2 = np.arange(6, 18, 4)
#print("Shape Array 1:", array1.shape)
#print("Array 1:\n", array1)
#print()
#print("Shape Array 2:", array2.shape)
#print("Array 2:", array2)

# Suma de ambos Arrays
array1 + array2

#FUNCIONES ESTADISTICAS SOBRE LOS ARRAYS

# Creación de un Array unidimensional
array1 = np.arange(1, 20, 2)
#print("Array 1:", array1)

# Media de los elementos del Array
#print(array1.mean())

# Suma de los elementos del Array
#print(array1.sum())

# Cuadrado de los elementos del Array
#print(np.square(array1))

# Raiz cuadrada de los elementos del Array
#print(np.sqrt(array1))

# Exponencial de los elementos del Array
#print(np.exp(array1))

# log de los elementos del Array
#print(np.log(array1))