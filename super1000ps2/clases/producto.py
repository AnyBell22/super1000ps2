from conexion import Conexion

class Producto():
  def __init__(self, id_producto:int,nombre:str,descripcion:str,precio:float,stock:int, categoria:str):
    self.__id_producto=id_producto
    self.__nombre=nombre
    self.__descripcion=descripcion
    self.__precio=precio
    self.__stock=stock
    self.__categoria=categoria
  
  def __str__(self):
    cadena=self.__nombre+" "+str(round(self.__precio, 2))+" "+str(self.__stock)+"\n"+self.__descripcion+"\n"+self.__categoria
    return cadena
 
  @property
  def id_producto(self):
    return self.__id_producto
  @property
  def nombre(self):
    return self.__nombre
  @property
  def descripcion(self):
    return self.__descripcion
  @property
  def precio(self):
    return self.__precio
  @property
  def stock(self):
    return self.__stock
  @property
  def categoria(self):
    return self.__categoria
  
  @nombre.setter
  def nombre(self, nuevovalor):
    self.__nombre=nuevovalor
  @descripcion.setter
  def descripcion(self, nuevovalor):
    self.__descripcion=nuevovalor
  @precio.setter
  def precio(self, nuevovalor):
    self.__precio=nuevovalor
  @stock.setter
  def stock(self, nuevovalor):
    self.__stock=nuevovalor
  @categoria.setter
  def categoria(self, nuevovalor):
    self.__categoria=nuevovalor

  def insertar(self):
    datos=(self.__nombre,self.__descripcion,self.__precio,self.__stock, self.__categoria)
    conexion=Conexion("BaseDatos\supermark.db")
    conexion.insert("INSERT INTO producto (nombre,descripcion,precio_venta,stock,categoria) VALUES (?,?,?,?,?)", datos)

  def eliminar(self):
    conexion=Conexion("BaseDatos\supermark.db")
    conexion.delete(f"DELETE FROM producto WHERE id_producto={self.__id_producto}")

  def modificar(self):
    datos=(self.nombre, self.descripcion, self.precio, self.stock,self.categoria, self.__id_producto)
    conexion=Conexion("BaseDatos\supermark.db")
    conexion.update("UPDATE producto SET nombre=?, descripcion=?,precio_venta=?, stock=?, categoria=?  WHERE id_producto=?", datos)
  
  def mostrar(self):
    conexion=Conexion("BaseDatos\supermark.db")
    productos=conexion.read(f"SELECT * FROM producto")
    return productos
    


#producto=Producto(35,"Dentifrico","Dentrifico Kolgate 100 gr",350,730,"Perfumeria") 
#producto.insert()
#producto.eliminar()
#producto.modificar()
#print(producto.mostrar())
