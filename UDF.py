# Conexion a la base de datos 
import sqlite3
import pandas as pd

# Antes de conectar la base de datos, creamos una funcion que dado un numero n, lo eleva al cuadrado

square = lambda n: n*n

conn = sqlite3.connect("northwind.db")

# Ahora, hay que registrar la funcion en SQLite. Para ello, se llama al siguiente metodo:

conn.create_function("square",1,square)

# Primer parametro: nombre que le voy a dar en SQLite
# Segundo parametro: cuantos parametros va a tener la funcion (en este caso, solo 1 (para potencia solo necesitamos un parametro))
# Tercer parametro: Cual es la funcion de python que voy a utilizar para crear esta funcion.

# Ahora, queremos crear algo que nos permita hacer una consulta a una base de datos y obtener una respuesta. Pero, si hago una consulta a
# la base de datos, para recibir una respuesta, la db debe recibir los datos, procesarlos, etc. Por lo tanto, vamos a necesitar un cursor,
# es decir, objetos que nos permiten, cuando se realiza una consulta, que la db la reciba, procese, etc y el resultado lo devuelva formateado

cursor = conn.cursor()
cursor.execute('''
    SELECT * FROM Products
    ''')

results = cursor.fetchall() # con fetchall() se obtiene la informacion obtenida en cursor (en este caso, la tabla Products) 
results_df = pd.DataFrame(results)
print(results_df)

conn.commit() # como estamos iniciando una transaccion, si realizamos alguna modificacion en la db, debemos impactar los cambios realizando un commit 

cursor.close() # luego de obtener la informacion, cierra el cursor
conn.close() # cerramos la conexion tambien

# Luego de ejecutar esto, obtenemos la tabla Products pero sin formato. Esto se debe a que el metodo fetchall() nos devuelve una lista de tuplas
# con cada uno de los valores. Para solucionar esto, podemos importar la libreria pandas



################## Ahora, aplicamos lo mismo usando contexto con with ##################

# import sqlite3
# import pandas as pd

# square = lambda n: n*n

# with sqlite3.connect("northwind.db") as conn: 
#     conn.create_function("square",1,square)
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM Products')
#     results = cursor.fetchall()  
#     results_df = pd.DataFrame(results)

# print(results_df)

# Nos ahorramos los cierres porque con el with la conexion se cierra automaticamente

# Tambien podemos llamar a la funcion de la siguiente manera:

import sqlite3
import pandas as pd

square = lambda n: n*n

with sqlite3.connect("northwind.db") as conn: 
    conn.create_function("square",1,square)
    cursor = conn.cursor()
    cursor.execute('SELECT *, square(Price) FROM Products WHERE Products > 0')
    results = cursor.fetchall()  
    results_df = pd.DataFrame(results)

print(results_df)

