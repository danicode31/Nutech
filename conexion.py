import sqlite3

def conectar():
    ''' implementacion para la conexion de la bbdd '''
    try:
        conexion = sqlite3.connect("contactos.db")
        print("Se ha conectado a la base de datos")
        return conexion
    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)
        

def crear_tabla(conexion):
    ''' crea la tabla contacto para utilizar en la bbdd '''
    cursor = conexion.cursor()
    query = ''' CREATE TABLE IF NOT EXISTS contacto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            empresa TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT NOT NULL,
            direccion TEXT NOT NULL
    )'''
    cursor.execute(query)
    conexion.commit()