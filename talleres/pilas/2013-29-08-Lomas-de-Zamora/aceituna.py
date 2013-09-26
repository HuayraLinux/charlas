class AceitunaHuayra(pilas.actores.Aceituna):
	def __init__ (self):
		pilas.actores.Aceituna.__init__(self)
		self.x = 400									#arranca en 400, fuera de la pantalla
		self.x = [-400],3								#termina en -400, fuera de la pantalla del otro lado, y tarda 3 segundos en llegar
		self.y = random.randint(-200,200)				#la posicion en Y va tomando un numero al azar entre 200 y -200. asi no van todas al mismo lugar 

	def actualizar(self):								#elimina las aceitunas a medida que van desapareciendo de la pantalla para que no ocupe memoria
		if self.x < -360:
			self.eliminar()



def crear_aceituna():
	nueva_aceituna = AceitunaHuayra()
	lista_aceitunas.append(nueva_aceituna)	
	return True

pilas.mundo.agregar_tarea(2,crear_aceituna)               #para que las aceitunas y las estrellas no salgan al mismo tiempo cambiarlo por random


-----------
#agregar debajo en puntaje

def cuando_toca_aceituna (protagonista,aceituna):
	aceituna.eliminar()
	puntaje.aumentar(-10)   							#usamos numero negativos para "restar" puntaje
	protagonista.decir("GUACALA")						



pilas.mundo.colisiones.agregar(protagonista,lista_aceitunas,cuando_toca_aceituna)
