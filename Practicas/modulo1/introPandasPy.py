import pandas as pd


# importCreación del objeto Series 

#Creacion de un objeto Series
s = pd.Series([2, 4, 6, 8, 10])
print(s)

# Creacion de un objeto Series inicializandolo con un diccionario de Python
altura = {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}
s2 = pd.Series(altura)
print(s2)

#Creacion de un objeto Series inicializandolo con algunos de los elementos de un diccionario de Python
s3 = pd.Series(altura, index = ["Pedro","Julia"])
print(s3)

# Creacion de un objeto Series inicializandolo con un escalar
s4 = pd.Series(30, ["Test1","Test2","Test3"])
print(s4)
