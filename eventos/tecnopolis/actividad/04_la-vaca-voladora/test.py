#!/usr/bin/env python
# Instrucciones:
#
#     para iniciar este juego, escribir:
#
#           python test.py

import random
import math
import pilas


class Estado:

    def __init__(self, vaca):
        self.vaca = vaca
        self.iniciar()

    def iniciar(self):
        pass

class FondoContador(pilas.actores.Actor):

    def __init__(self):
        self.carga_imagenes()
        pilas.actores.Actor.__init__(self, self.fondo_contador)
        self.contador_reposo = 0
        self.izquierda =  -315
        self.arriba = 235
        t = pilas.actores.Texto("Jugador 1") #Nombre del jugador
        t.izquierda = -180
        t.arriba = 218
        t.escala = 0.60
        t.color = pilas.colores.negro

    def carga_imagenes(self):
        self.fondo_contador = pilas.imagenes.cargar("fondo_contador.png")

class Ganador(pilas.actores.Actor):
	
    def __init__(self):
        self.carga_imagenes()
        pilas.actores.Actor.__init__(self, self.cara_ganador)
        self.contador_reposo = 0
        

    def carga_imagenes(self):
        self.cara_ganador = pilas.imagenes.cargar("cara_final.png")


class Jugador(pilas.actores.Actor):

    def __init__(self):
        self.carga_imagenes()
        pilas.actores.Actor.__init__(self, self.normal)
        self.escala = 0.23
        self.contador_reposo = 0
        self.izquierda =  -313
        self.arriba = 225
        pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla)

    def carga_imagenes(self):
        self.normal = pilas.imagenes.cargar("cara_normal.png")
        self.gana = pilas.imagenes.cargar("cara_gana.png")
        self.pierde = pilas.imagenes.cargar("cara_pierde.png")

    def actualizar(self):
        if self.contador_reposo > 0:
            self.contador_reposo -= 1

            if self.contador_reposo == 0:
                self.imagen = self.normal

    def mostrar_cara_gana(self):
        self.imagen = self.gana
        self.contador_reposo = 40

    def mostrar_cara_pierde(self):
        self.imagen = self.pierde
        self.contador_reposo = 40

    def cuando_pulsa_tecla(self, evento):
        if evento.codigo == 'r':
            self.carga_imagenes()
            self.imagen = self.normal
            print "recargando imagenes..."


class Ingresando(Estado):

    def iniciar(self):
        self.vaca.definir_animacion([3, 4, 5, 6, 7, 8, 9, 10])
        self.contador = 0
        self.vaca.x = -380
        self.vaca.x = [-170], 0.5

    def actualizar(self):
        self.contador += 2

        if self.contador > 50:
            self.vaca.estado = Volando(self.vaca)

class Volando(Estado):

    def iniciar(self):
        self.vaca.definir_animacion([3, 4, 5, 6, 7, 8, 9, 10])
        self.contador = 0
        self.esta_riendo = False

    def actualizar(self):
        control = pilas.mundo.control
        velocidad = 5

        if control.arriba:
            self.vaca.y += velocidad
        elif control.abajo:
            self.vaca.y -= velocidad

        if control.izquierda:
            self.vaca.x -= velocidad
        elif control.derecha:
            self.vaca.x += velocidad

        if self.vaca.y > 210:
            self.vaca.y = 210
        elif self.vaca.y < -210:
            self.vaca.y = -210

        if self.vaca.izquierda < -400:
            self.vaca.izquierda = -400

        if not self.esta_riendo:
            if self.vaca.contador_sonreir == 40:
                self.esta_riendo = True
                self.vaca.definir_animacion([0])
        else:
            if self.vaca.contador_sonreir == 0:
                self.esta_riendo = False
                self.vaca.definir_animacion([3, 4, 5, 6, 7, 8, 9, 10])

        self.actualizar_movimiento_vuelo()

    def actualizar_movimiento_vuelo(self):
        "Mueve la vaca de arriba hacia abajo muy suavemente."
        self.contador += 0.1
        self.vaca.y += math.cos(self.contador) * 0.4


class Perdiendo(Estado):

    def iniciar(self):
        self.vaca.definir_animacion([1])
        self.vaca.centro = ('centro', 'centro')
        self.contador = 0

    def actualizar(self):
        self.contador += 1
        self.vaca.x -= 3

        if self.contador > 30:
            self.vaca.regresar_al_vuelo()


class Vaca(pilas.actores.Actor):

    def __init__(self):
        pilas.actores.Actor.__init__(self)
        grilla = pilas.imagenes.cargar_grilla('data/sprites.png', 11, 1)
        self.imagen = grilla
        self.definir_animacion([0])
        self.centro = (140, 59)
        self.radio_de_colision = 40
        self.x = -170
        self.estado = Ingresando(self)
        self.contador = 0
        self.contador_sonreir = 0

    def definir_animacion(self, cuadros):
        self.paso = 0
        self.contador = 0
        self.cuadros = cuadros

    def actualizar(self):
        self.estado.actualizar()
        self.actualizar_animacion()

        if self.contador_sonreir > 0:
            self.contador_sonreir -= 1

    def actualizar_animacion(self):
        self.contador += 0.2

        if (self.contador > 1):
            self.contador = 0
            self.paso += 1

            if self.paso >= len(self.cuadros):
                self.paso = 0

        self.imagen.definir_cuadro(self.cuadros[self.paso])

    def perder(self):
        self.estado = Perdiendo(self)
        t = pilas.actores.Texto("uuyyy !!!")
        t.color = pilas.colores.naranja
        t.escala = 0
        t.escala = [2], 0.2
        t.rotacion = 60
        t.rotacion = [0], 0.2

        def eliminar_texto():
            t.eliminar()

        pilas.mundo.agregar_tarea(1.5, eliminar_texto)

    def regresar_al_vuelo(self):
        self.estado = Volando(self)

    def sonreir(self):
        self.contador_sonreir = 40

class Enemigo(pilas.actores.Actor):

    def __init__(self):
        pilas.actores.Actor.__init__(self)
        self.imagen = "data/enemigo2.png"	# Imagen del enemigo, 1, 2 o 3.
        self.escala = 0.5
        self.izquierda = 320
        self.y = random.randint(-210, 210)

    def actualizar(self):
        self.x -= 7
        pilas.actores.Actor.actualizar(self)

class Netbook(pilas.actores.Actor):

    def __init__(self):
        pilas.actores.Actor.__init__(self, 'bueno3.png') # Elemento que suma puntos 1, 2 o 3
        self.izquierda = 320
        self.y = random.randint(-210, 210)

    def actualizar(self):
        self.izquierda -= 5

        if self.derecha < -320:
            self.eliminar()

    def capturar(self):
        self.eliminar()
        EfectoNetbookLiberada(self.x, self.y)


class EfectoNetbookLiberada(pilas.actores.Actor):

    def __init__(self, x, y):
        pilas.actores.Actor.__init__(self, 'bueno3_fx.png', x=x, y=y)

    def actualizar(self):
        self.izquierda -= 8
        self.escala += 0.1
        self.transparencia += 3

        if self.transparencia > 90:
            self.eliminar()

class AlumnoItem(pilas.actores.Actor):
	
	def __init__(self):
	    pilas.actores.Actor.__init__(self, 'bueno4.png') # Elemento Jugador, que suma puntos extras
	    self.izquierda = 320
	    self.y = random.randint(-210,210)
	    self.escala = 0.18
		
	def actualizar(self):
	    self.izquierda -= 8
		
	    if self.derecha < -320:
		self.eliminar()
			
	def capturar(self):
		self.eliminar()
		EfectoAlumnoItem(self.x, self.y)
		
	
class EfectoAlumnoItem(pilas.actores.Actor):
	
	def __init__(self, x, y):
		pilas.actores.Actor.__init__(self, 'bueno4_fx.png', x=x, y=y)
		
	def actualizar(self):
		self.izquierda -= 12
		self.escala += 0.1
		self.transparencia += 3
		
		if self.transparencia > 90:
			self.eliminar()
			


class Nube(pilas.actores.Actor):

    def __init__(self):
        pilas.actores.Actor.__init__(self)
        velocidad = random.randint(2, 10)
        self.velocidad = velocidad
        self.escala = velocidad / 10.0
        self.transparencia = velocidad * 6
        self.z = - (velocidad -5)
        self.x = random.randint(-320, 320)
        self.y = random.randint(-210, 210)

        rutas_imagenes_nubes = [
                'data/nube1.png',
                'data/nube2.png',
        ]
        self.imagen = random.choice(rutas_imagenes_nubes)

    def actualizar(self):
        self.x -= self.velocidad

        if self.derecha < -320:
            self.reiniciar_posicion()

    def reiniciar_posicion(self):
        self.izquierda = 320
        self.y = random.randint(-210, 210)

class Panadero(pilas.actores.Actor):
	
	def __init__(self):
		pilas.actores.Actor.__init__(self)
		velocidad = random.randint(2, 10)
		self.velocidad = velocidad
		self.escala = velocidad / 8.0
		self.transparencia = velocidad * 6
		self.z = - (velocidad -5)
		self.x = random.randint(-350, 350)
		self.y = random.randint(-210, 210)
		self.rotacion = random.randint(-360, 360)
		self.imagen = pilas.imagenes.cargar("data/panadero.png")

	def actualizar(self):
		self.x += self.velocidad
		self.rotacion -= self.velocidad / 4.0

		if self.derecha > 350:
			self.reiniciar_posicion()

	def reiniciar_posicion(self):
		self.izquierda = -350
		self.y = random.randint(-210, 210)	

pilas.iniciar(usar_motor="qt")

class EscenaJuego(pilas.escena.Normal):

	def iniciar(self):
		fondo = pilas.fondos.Fondo('data/nieve.png') # Imagen de fondo
		jugador = Jugador()
		fondo_contador = FondoContador()
		puntos = pilas.actores.Puntaje(y=162)
		puntos.izquierda = jugador.derecha + 150
		puntos.color = pilas.colores.naranja

		vaca = Vaca()
		items = []
		items2 = []
		enemigos = []

		def crear_netbook():
			un_item = Netbook()
			items.append(un_item)
			return True

		def crear_alumnoItem():
			un_alumno = AlumnoItem()
			items2.append(un_alumno)
			return True

		pilas.mundo.agregar_tarea(2, crear_netbook)
		pilas.mundo.agregar_tarea(7, crear_alumnoItem)

		def cuanto_toca_item(vaca, netbook):
			netbook.capturar()
			vaca.sonreir()
			puntos.aumentar(10)
			puntos.escala = 2
			puntos.escala = [1], 0.2
			puntos.rotacion = random.randint(30, 60)
			puntos.rotacion = [0], 0.2
			jugador.mostrar_cara_gana()
		
			if puntos.obtener() >= 100:
				pilas.cambiar_escena(EscenaGanar())

		def cuando_toca_alumnoItem(vaca, alumnoItem):
			alumnoItem.capturar()
			vaca.sonreir()
			puntos.aumentar(25)
			puntos.escala = 3
			puntos.escala = [1], 0.3
			puntos.rotacion = random.randint(30, 60)
			puntos.rotacion = [0], 0.2
			jugador.mostrar_cara_gana()
			
			if puntos.obtener() >= 100:
				pilas.cambiar_escena(EscenaGanar())
				
		pilas.mundo.colisiones.agregar(vaca, items, cuanto_toca_item)				
		pilas.mundo.colisiones.agregar(vaca, items2, cuando_toca_alumnoItem)

		def crear_enemigo():
			un_enemigo = Enemigo()
			enemigos.append(un_enemigo)
			return True

		pilas.mundo.agregar_tarea(2.5, crear_enemigo)


		def cuanto_toca_enemigo(vaca, enemigo):
			puntos.aumentar(-5)
			vaca.perder()
			enemigo.eliminar()
			jugador.mostrar_cara_pierde()


		pilas.mundo.colisiones.agregar(vaca, enemigos, cuanto_toca_enemigo)


		for x in range(7):
			Nube()

class EscenaGanar(pilas.escena.Normal):

    def iniciar(self):
		fondo = pilas.fondos.Fondo('data/fondo_final.png')
		
		
		for x in range(7):
			Panadero()
			
		ganador = Ganador()
		ganador.y = 10
		ganador.escala = 0.8
		ganaste = pilas.actores.Mono()
		ganaste.imagen = pilas.imagenes.cargar("ganaste.png")
		ganaste.y = -170
		

pilas.cambiar_escena(EscenaJuego())
pilas.ejecutar()
