from conexion import Conexion

class Usuario():
  def __init__(self,id_usuario,nombreUsuario,clave): 
    self.__id_usuario=id_usuario
    self.__nombreUsuario=nombreUsuario
    self.__clave=clave
    self.__tipo=1

  def __str__(self):
    cadena=self.__id_usuario+ " " + "\n" +self.__nombreUsuario+" "+"\n"+str(self.__clave)
    return cadena

  @property
  def id_usuario(self):
    return self.__id_usuario
  @property
  def nombreUsuario(self):
    return self.__nombreUsuario
  @property
  def clave(self):
    return self.__clave
  @property
  def tipo(self):
    return self.__tipo

  @id_usuario.setter
  def id_usuario(self, nuevoValor):
    self.__nombreUsuario=nuevoValor
  @nombreUsuario.setter
  def nombreUsuario(self, nuevoValor):
    self.__nombreUsuario=nuevoValor
  @clave.setter
  def clave(self, nuevoValor):
    self.__clave=nuevoValor

  def consulta_US(self):
    conexion=Conexion("BaseDatos\supermark.db")
    datos=conexion.read(f"SELECT * FROM usuario WHERE nombre_US='{self.__nombreUsuario}' and clave='{self.__clave}'")
    #no me da el error cuando ingreso cualquier cosa  
    print("datos",datos)
    if (datos == []):
      return False
    else:
      return True

  def consulta_tipo(self):
      conexion=Conexion("BaseDatos\supermark.db")
      tipo=conexion.read(f"SELECT tipo FROM usuario WHERE nombre_US='{self.__nombreUsuario}' and clave='{self.__clave}'")
      return tipo[0][0]

  def insertar_US(self):
    datosU=(self.nombreUsuario, self.clave)
    conexion=Conexion("BaseDatos\supermark.db")
    conexion.insert("INSERT INTO usuario (nombre_US,clave) VALUES (?,?)", datosU)
    
  def eliminar_US(self):
    conexion=Conexion("BaseDatos\supermark.db")
    conexion.delete(f"DELETE FROM usuario WHERE id_usuario={self.__id_usuario}")

#admin= Usuario(1,"admin@gmail.com",123456)
#usuario= Usuario(2,"sergio@gmail.com",123456)
#admin.insertar_US()
#usuario.insertar_US()
#print(usuario.consulta_US())
#usuario.eliminar_US()
#usuario.consulta_tipo()