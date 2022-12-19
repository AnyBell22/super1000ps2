import sqlite3 
from sqlite3 import Error
import tkinter as tk
from tkinter import messagebox

def creacionBD(db_file):
    conexion=None
    try:
        conexion=sqlite3.connect(db_file) 
    except Error as e:
        print(e)
    '''
    finally:
        if conexion:
            conexion.close()
    '''
    return conexion

def crear_tabla(conexion, tabla_sql):
    """ create a table from the create_table_sql statement
    :param conexion: Connection object
    :param table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c=conexion.cursor()
        c.execute(tabla_sql)
        #messagebox.showinfo("BBDD", "Base de datos creada con exito")
    except Error as e:
        #messagebox.showwarning("Atencion !", "La base de datos ya existe")
        print(e)
    #conexion.close()


def main():
    database='BaseDatos\supermark.db'

    crear_tabla_producto = """ CREATE TABLE IF NOT EXISTS Producto (
                                    id_producto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                    nombre TEXT, 
                                    descripcion TEXT, 
                                    precio_venta REAL, 
                                    stock INTEGER,
                                    categoria TEXT
                                ); """

    crear_tabla_usuario = """CREATE TABLE IF NOT EXISTS Usuario(
                                    id_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    nombre_US TEXT NOT NULL, 
                                    clave INTEGER NOT NULL, 
                                    tipo INTEGER NOT NULL DEFAULT 1, 
                                    FOREIGN KEY (nombre_US) REFERENCES cliente(correo)
                                );"""

    crear_tabla_cliente = """CREATE TABLE IF NOT EXISTS Cliente(
                                    id_cliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                    nombre TEXT NOT NULL,
                                    apellido TEXT NOT NULL, 
                                    dni INTEGER(8) NOT NULL,
                                    id_direccion INTEGER NOT NULL,
                                    correo TEXT NOT NULL,
                                    FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion)
                                );"""

    crear_tabla_venta = """ CREATE TABLE IF NOT EXISTS Venta(
                                    id_venta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                    fecha DATE, 
                                    id_cliente INTEGER, 
                                    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)
                                );"""

    crear_tabla_detalle_venta = """CREATE TABLE IF NOT EXISTS Detalle_Venta(
                                    id_venta INTEGER, 
                                    cantidad INTEGER, 
                                    id_producto INTEGER,
                                    FOREIGN KEY(id_venta) REFERENCES venta(id_venta), 
                                    FOREIGN KEY(id_producto) REFERENCES producto(id_producto)
                                );"""  

    crear_tabla_direccion = """CREATE TABLE IF NOT EXISTS Direccion(
                                    id_direccion INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                    calle TEXT,
                                    altura INTEGER,
                                    localidad TEXT,
                                    provincia TEXT,
                                    codigo_postal TEXT
                                );"""


    # crear  coneccion a base de datos
    conexion=creacionBD(database)

    # create tables
    if conexion is not None:
        # create table
        crear_tabla(conexion, crear_tabla_producto)

        crear_tabla(conexion, crear_tabla_usuario)

        crear_tabla(conexion, crear_tabla_cliente)

        crear_tabla(conexion, crear_tabla_venta)

        crear_tabla(conexion, crear_tabla_detalle_venta)

        crear_tabla(conexion, crear_tabla_direccion)

        print("Base de Datos Creada")
        
    else:
        print("Error! No se puede crear la coneccion a la Base de Datos.")
    

if __name__ == '__main__':
    main() 

'''    
    def conexionBD(db_file):

        conexion=sqlite3.connect(db_file)
        cursor= conexion.cursor()
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS producto (id_producto INTEGER primary key autoincrement, nombre TEXT, descripcion TEXT, categoria TEXT,precio_venta REAL, stock INTEGER)");
            cursor.execute("CREATE TABLE IF NOT EXISTS usuario(id_usuario INTEGER primary key autoincrement, nombre_US TEXt, clave INTEGER, tipo INTEGER NOY NULL DEFAULT 1, FOREIGN KEY (nombre_US) REFERENCES cliente(correo),tipo INTEGER)");
            cursor.execute("CREATE TABLE IF NOT EXISTS cliente(id_cliente INTEGER primary key autoincrement, nombre TEXT,apellido TEXT, dni INTEGER(8),correo TEXT,FOREIGN KEY (direccion) REFERENCES direccion(id_direccion))");
            cursor.execute("CREATE TABLE IF NOT EXISTS venta(id_venta INTEGER primary key autoincrement, fecha DATE, id_cliente INTEGER, FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente))");
            cursor.execute("CREATE TABLE IF NOT EXISTS detalle_venta(id_venta INTEGER, cantidad INTEGER, id_producto INTEGER, FOREIGN KEY(id_venta) REFERENCES venta(id_venta), FOREIGN KEY(id_producto) REFERENCES producto(id_producto))");
            cursor.execute("CREATE TABLE IF NOT EXISTS direccion(id_direccion INTEGER primary key autoincrement, calle TEXT,altura INTEGER,localidad TEXT,provincia TEXT,codidoPostal TEXT)");

            messagebox.showinfo("BBDD", "Base de datos creada con exito")
        except:
            messagebox.showwarning("Atencion !", "La base de datos ya existe")
            
        conexion.close()

conexionBD('BaseDatos\supermark.db')
'''