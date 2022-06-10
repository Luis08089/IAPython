from xml.sax.handler import DTDHandler
from numpy import dtype
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
df = pd.DataFrame(personas)
#print(df)

#Creación de un DataFrame inicializándolo con algunos elementos de un diccionario de objetos series
df = pd.DataFrame(personas, columns = ["altura","peso"], index = ["Ana","Julia","Santiago"])
#print(df)

#Creación de un DataFrame inicializándolo con una lista de listas de Python (Se debe especificar las columnas e indices por separado)
valores = [
    [185,4,76],
    [170,0,65],
    [190,1,89]
]
df = pd.DataFrame(valores, columns=['altura','hijos','peso'], index=['Pedro','Ana','Juan'])
#print(df)

#Cración de un DataFrame inicializándolo con un diccionario de Python
personas = {
    "peso": {"Santiago": 87,"Pedro": 78,"Ana": 65,"Julia": 70},
    "altura": {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}
}
df = pd.DataFrame(personas)
#print(df)

# ACCESO A LOS ELEMENTOS DE UN DATAFRAME
#Creación de un DataFrame inicializándolo con un diccionario de objetos Series
personas2 = {
    "peso": pd.Series([84,90,56,64], ["Santiago","Pedro","Ana","Julia"]),
    "altura": pd.Series({"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}),
    "hijos": pd.Series([2,3], ["Pedro","Julia"])
}
df = pd.DataFrame(personas2)
#Acceso a los elementosde las columnas del DataFrame
# print (df['peso'])
#print(df[['peso', 'hijos']])

#Pueden combinarse los metodos anteriores con expresiones booleanas
#print(df[df["peso"] > 80])

#Pueden combinarse los metodos anteriores con expresiones booleanas
#print(df[(df['peso'] >80) & (df['altura'] >180)])

# CONSULTA AVANZADA DE LOS ELEMENTOS DE UN DATAFRAME
#print(df.query('altura >= 170 and peso > 70'))

#Copia del DataFrame df en df_copy (Al modificar un elemento de df_copy no se modifica df)
df_copy = df.copy()
#print(df_copy)

#Añadir una nueva columna al DataFrame
df['cumpleaños'] = [1990,1987,1980,1994]
#print(df)
#Añadir una nueva columna calculada al DataFrame
df['Años'] = 2022 - df['cumpleaños']
#print(df)
#Añadir una nueva columna creada al DataFrame
df_mod = df.assign(mascotas = [1,3,0,0])
#print(df_mod)
#print(df) 
#Eliminar una columna existente del DataFrame
#del df['peso']
##print(df)
#Eliminar una columna existente devolviendo una copia del DataFrame resultante
df_mod = df.drop(['hijos'], axis = 1)
#print(df_mod)

#EVALUACION DE ESPRESIONES SOBRE UN DATAFRAME
#Evaluar una funcion sobre una columna del DataFrame
df_mod = df.eval('altura / 2')
#print(df_mod)
#asignar el valor resultante como una nueva columna
df.eval('media_altura = altura / 2', inplace = True)
#print(df)
#Evaluar una funcion utilizando una variable local
max_altura = 180
#print(df.eval('altura > @max_altura'))
#Aplicar una funcion externa a una columna del DataFrame
def func(x): return x+2
#print(df['peso'].apply(func))

# GUARDAR Y CARGAR EL DATAFRAME
#Guardar el DataFrame como CSV, HTML y JSON
#df.to_csv('df_personas.csv')
#df.to_html('df_personas.html')
#df.to_json('df_personas.json')

#Cargar el DataFrame en Jupyter
df2 = pd.read_csv('df_personas.csv')
#print(df2)
#Cargar el DataFrame con la primera columna correctamente asignada
df2 = pd.read_csv('df_personas.csv', index_col=0)
#print(df2)