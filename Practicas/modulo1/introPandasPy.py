import pandas as pd


# importCreación del objeto Series 

#Creacion de un objeto Series
s = pd.Series([2, 4, 6, 8, 10])
#print(s)

# Creacion de un objeto Series inicializandolo con un diccionario de Python
altura = {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}
s2 = pd.Series(altura)
#print(s2)

#Creacion de un objeto Series inicializandolo con algunos de los elementos de un diccionario de Python
s3 = pd.Series(altura, index = ["Pedro","Julia"])
#print(s3)

# Creacion de un objeto Series inicializandolo con un escalar
s4 = pd.Series(30, ["Test1","Test2","Test3"])
#print(s4)

# ACCESO A LOS ELEMENTOS DE UN OBJETO SERIES

#Accediendo al tercer elemento del objeto
s5 = pd.Series([1,4,6,8], index=["num1","num2","num3","num5"])
#print(s5["num3"])

#Accediendo al elemento por posicion
#print(s5[2])

#loc es la forma estandar de acceder a un elemento de un objeto series por atributo
#print(s5.loc["num3"])

#iloc es la forma estandar de acceder a un elemento de un objeto series por posicion
#print(s5.iloc[2])

#Accediendo al segundo y tercer elemento por posicion
#print(s5.iloc[2:4])

# REPRESENTACION GRAFICA DE UN OBJETO SERIES

#Creación de un objeto Series denominado Temperaturas
temperaturas = [4.4,5.1,6.1,6.2,6.1,6.1,5.7,5.2,4.7,4.1,3.9]
s = pd.Series(temperaturas, name="Temperaturas")
#print(s)

# Representación gráfica del objeto Series
import matplotlib.pyplot as plt
#s.plot()
#plt.show()

# CREACION DE UN OBJETO DATAFRAME

#Creación de un DataFrame inicializándolo con un diccionario de objetos Series
personas = {
    "peso": pd.Series([84,90,56,64], ["Santiago","Pedro","Ana","Julia"]),
    "altura": pd.Series({"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}),
    "hijos": pd.Series([2,3], ["Pedro","Julia"])
}
#df = pd.DataFrame(personas)
#print(df)

#Creación de un DataFrame inicializándolo con algunos elementos de un diccionario de objetos series
#df = pd.DataFrame(personas, columns = ["altura","peso"], index = ["Ana","Julia","Santiago"])
#print(df)