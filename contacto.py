from conexion import *


def registrar(nombre, apellido, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        query = ''' INSERT INTO contacto (
                nombre, apellido, empresa, telefono, email, direccion) values
                ( ?, ?, ?, ?, ?, ?)'''
        datos = (nombre, apellido, empresa, telefono, email, direccion)
        cursor.execute(query,datos)
        con.commit()
        con.close()
    except sqlite3.Error as err:
        print("Ha ocurrido un error",err)
        

def mostrar():
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        query = '''SELECT * FROM contacto '''
        cursor.execute(query)
        datos = cursor.fetchall()
        con.close()
    except sqlite3.Error as err:
        print("Ha ocurrido un error",err)
    return datos

def buscar(id):
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        query = ''' SELECT * FROM contacto WHERE id=?'''
        cursor.execute(query,(id,))
        datos = cursor.fetchall()
        con.close()
    except sqlite3.Error as err:
        print("Ha ocurrido un error",err)
    return datos


def modificar(id,nombre, apellido, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        query = ''' UPDATE contacto SET nombre=?, apellido=?,
        empresa=?, telefono=?, email=?, direccion=? WHERE id=?'''
        datos = (nombre, apellido, empresa, telefono, email, direccion,id)
        cursor.execute(query)
        con.close()
        return "Se ha modificado correctamente"
    except sqlite3.Error as err:
        print("Ha ocurrido un error",err)
        
def eliminar(id):
    try:
        con = conectar()
        cursor = con.cursor()
        query = ''' DELETE FROM contacto WHERE id=? '''
        cursor.execute(query,(id,))
        con.commit()
        con.close()
        return "Se ha eliminado correctamente"
    except sqlite3.Error as err:
        print("Ha ocurrido un error",err)