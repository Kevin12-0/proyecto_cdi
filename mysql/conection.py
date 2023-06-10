import mysql.connector

conection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "holamundo",
    db = "cdi"
)
cur = conection.cursor()
cur.execute(
    "SELECT * FROM alumnos;"
    )
for datos in cur.fetchall():
    print(datos)
conection.close
