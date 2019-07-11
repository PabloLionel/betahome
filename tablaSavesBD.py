import sqlite3


class ConexionSaves():
	def crearTablaSaves(self):

		#CONECTAMOS
		conexion=sqlite3.connect("betahome.db")
		#CURSOR
		consulta=conexion.cursor()

		#CREA TABLA
		sql="""
		CREATE TABLE IF NOT EXISTS saves(
		id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		extra float,
		total float 
		)
		"""
		#EJECUTAMOS LA CONSULTA
		if (consulta.execute(sql)):
			print("tabla creada")
		else:
			print("error al crear tabla")

		#CERRAMOS la consulta y la conexion y guardamos los datos
		consulta.close()
		conexion.commit()
		conexion.close()

		#CONECTAMOS
		conexion=sqlite3.connect("betahome.db")
		#CURSOR
		consulta=conexion.cursor()
		#INSERCION (ponemos a cero para poder operar)
		extra=0
		total=0
		datos=(extra,total)
		sql="""
		INSERT INTO saves(extra,total) VALUES (?,?)
		"""
		if (consulta.execute(sql,datos)):
			print("datos guardados")
		else:
			print("error")
		#CERRAMOS la consulta, guardamos los datos y cerramos la conexion
		consulta.close()
		conexion.commit()
		conexion.close()

	def traerTotal(self):
		conexion=sqlite3.connect("betahome.db")
		consulta=conexion.cursor()
		
		consulta.execute("SELECT SUM(saves.extra) FROM saves")
		
		var=consulta.fetchone()
		
		consulta.close()
		conexion.commit()
		conexion.close()
		return var[0]

	def actualizarTablaSave(self,extra):
		conexion=sqlite3.connect("betahome.db")
		consulta=conexion.cursor()
		#INSERCION
		extra=extra
		#sumamos todos los valores de la columna extra
		consulta.execute("SELECT SUM(saves.extra) FROM saves")
		#guardo la tupa obtenida
		var=consulta.fetchone()
		#sumo la celda de la tupla + el extra que ingreso actualmente
		total= var[0] + extra

		consulta.close()
		conexion.commit()
		conexion.close()

		conexion=sqlite3.connect("betahome.db")
		consulta=conexion.cursor()
		datos=(extra,total)
		sql="""
		INSERT INTO saves(extra,total) VALUES (?,?)
		"""
		if (consulta.execute(sql,datos)):
			print("datos guardados")
		else:
			print("error")
		#CERRAMOS la consulta, guardamos los datos y cerramos la conexion
		consulta.close()
		conexion.commit()
		conexion.close()

