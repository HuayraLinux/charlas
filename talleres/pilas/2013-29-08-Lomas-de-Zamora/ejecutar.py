import pilas
import random #este comando importa las librerias o modulos necesarios, pilas y random

pilas.iniciar()

pilas.fondos.Fondo('data/nubes.png') # Aca pongo el fondo usando la imagen

class Nube (pilas.actores.Actor): # Aca creo el actor Nubes con las caracteristicas de la clase Actor de Pilas
	def __init__(self):
		pilas.actores.Actor.__init__(self)
		self.imagen = 'data/nube1.png'
		self.transparencia = 50
		self.velocidad = random.randint (5,20)

	def actualizar(self):
		self.x = self.x - self.velocidad
		if self.derecha < -320:
			self.izquierda = 320
			self.y = random.randint (-200, 200)
			self.escala = random.randint (1,3)/6.0

class Vaca (pilas.actores.Actor): # Aca creo el actor Vaca con las caracteristicas de la clase Actor de Pilas
	def __init__ (self):
		pilas.actores.Actor.__init__(self)
		self.imagen = 'data/vaca_volando.png'
		self.x = -60
		self.radio_de_colision = 40

	def actualizar(self):
		if pilas.escena_actual().control.arriba:
			self.y += 5
		elif pilas.escena_actual().control.abajo:
			self.y -= 5

class EstrellaHuayra(pilas.actores.Estrella): # Aca creo el actor EstrellaHuayra en base al actor de pila Estrella
	def __init__ (self): 
		pilas.actores.Estrella.__init__(self)
		self.x = 400
		self.x = [-400],3
		self.y = random.randint(-200,200)
		self.velocidad_rotacion = random.randint(-5,5)

	def actualizar(self):
		self.rotacion = self.rotacion + self.velocidad_rotacion
		if self.x < -360:
			self.eliminar()


lista_estrellas = []

def crear_estrella():
	nueva_estrella = EstrellaHuayra()
	lista_estrellas.append(nueva_estrella)	
	return True

pilas.mundo.agregar_tarea(2,crear_estrella)





#este incorpora un Actor de Pilas que es el marcador de puntaje
puntaje = pilas.actores.Puntaje()
puntaje.x = -300
puntaje.y = 215



def cuando_toca_estrella (protagonista,estrella):
	estrella.eliminar()
	puntaje.aumentar(10)





n1 = Nube()
n2 = Nube()
n3 = Nube()
n4 = Nube()
n5 = Nube()
n6 = Nube()


#a partir de este punto comienza el juego, cuando aparece la vaca que creamos mas arriba

protagonista = Vaca()

pilas.mundo.colisiones.agregar(protagonista,lista_estrellas,cuando_toca_estrella) #(actor1,actor2,funcion a ejecutar)


pilas.ejecutar()
