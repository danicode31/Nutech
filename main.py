from conexion import *
from contacto import *
from tabulate import tabulate
import os
con = conectar()
crear_tabla(con)


def iniciar():
    os.system('cls')
    while True:  
        print('Seleccione una opción: ')
        print('\t1. Añadir un contacto')
        print('\t2. Mostrar todos los contactos')
        print('\t3. Buscar un contacto')
        print('\t4. Modificar un contacto')
        print('\t5. Eliminar un contacto')
        print('\t6. Salir del programa')
        opcion = input('Ingrese la opción: ')        
        if opcion == '1':
            os.system('cls')
            nuevo_contacto()
        elif opcion == '2':
            os.system('cls')
            ver_contactos()
        elif opcion == '3':
            os.system('cls')
            buscar_contacto()
        elif opcion == '4':
            os.system('cls')
            modificar_contacto()
        elif opcion == '5':
            os.system('cls')
            eliminar_contacto()
        elif opcion == '6':
            break
        

def nuevo_contacto():
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    empresa = input('Ingrese la empresa: ')
    telefono = input('Ingrese el teléfono: ')
    email = input('Ingrese el email: ')
    direccion = input('Ingrese la dirección: ')
    respuesta = registrar(nombre, apellido, empresa, telefono, email, direccion)
    print(respuesta)
    
def ver_contactos():
    datos = mostrar()
    headers = ['ID','NOMBRES', 'APELLIDOS', 'EMPRESA','TELEFONO','EMAIL','DIRECCION']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)


def buscar_contacto():
    id = input('Ingrese el id del contacto: ')
    datos = buscar(id)
    headers = ['ID','NOMBRES', 'APELLIDOS', 'EMPRESA','TELEFONO','EMAIL','DIRECCION']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)


def modificar_contacto():
    id = input('Ingrese del id del contacto a modificar: ')
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    empresa = input('Ingrese la empresa: ')
    telefono = input('Ingrese el teléfono: ')
    email = input('Ingrese el email: ')
    direccion = input('Ingrese la dirección: ')
    respuesta = modificar(id,nombre, apellido, empresa, telefono, email, direccion)
    print(respuesta)
    
    
def eliminar_contacto():
    id = input('Ingrese del id del contacto a eliminar: ')
    respuesta = eliminar(id)
    print(respuesta)
    
if __name__ == iniciar():
    iniciar()
