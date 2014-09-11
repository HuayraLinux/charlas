#!/bin/env python
# -*- encoding: utf-8 -*-

import sys
sys.path.insert(0, "..")
import pilas
import random

pilas.iniciar()

class Enemigo(pilas.actores.Actor):
    def __init__(self, objetivo):
        pilas.actores.Actor.__init__(self)
        self.set_imagen("data/enemigo.png")
        self.aprender(pilas.habilidades.PerseguirAOtroActor, objetivo=objetivo, velocidad=random.uniform(0.5,1.5))
        self.aprender(pilas.habilidades.PuedeExplotar)
        self.pre_x = 0
        self.radio_de_colision = 25

    def actualizar(self):
        if self.pre_x > self.x:
            self.espejado = False
        else:
            self.espejado = True
        self.pre_x = self.x
        pilas.actores.Actor.actualizar(self)

class Juego(pilas.actores.Actor):
    def __init__(self):
        pilas.actores.Actor.__init__(self, 'invisible.png')
        pilas.fondos.Espacio()
        self.mapa = self.crear_mapa()
        self.enemigos = []
        self.marciano = pilas.actores.Martian(self.mapa)
        self.marciano.habilidades.Disparar.definir_colision(self.enemigos, self.hacer_explotar_enemigo)
        self.marciano.radio_de_colision = 30
        self.max_enemigos=3
        self.estrella = pilas.actores.Estrella(x=-80,y=180)
        self.estrella.radio_de_colision = 35
        pilas.escena_actual().colisiones.agregar(self.marciano, self.enemigos, self.enemigo_colisiona_marciano)
        pilas.escena_actual().colisiones.agregar(self.marciano, self.estrella, self.colisiona_premio)

    def enemigo_colisiona_marciano(self, marciano, enemigo):
        marciano.x = -200
        marciano.y = 0
        enemigo.x = random.uniform(-300,300)
        enemigo.y = 200

    def colisiona_premio(self, marciano, estrella):
         pilas.avisar("Ganaste genio !") 
         
    def agregar_enemigo(self):
        enemigo = Enemigo(self.marciano)
        enemigo.x = random.uniform(-300,300)
        enemigo.y = 200
        self.enemigos.append(enemigo)

    def crear_mapa(self):
        mapa = pilas.actores.Mapa(filas=15, columnas=20)

        # Plataforma superior
        mapa.pintar_bloque(5, 6, 0)
        mapa.pintar_bloque(5, 7, 1)
        mapa.pintar_bloque(5, 8, 2)

        # Segunda plataforma superior
        mapa.pintar_bloque(7, 13, 0)
        mapa.pintar_bloque(7, 14, 1)
        mapa.pintar_bloque(7, 15, 2)
        
        # Plataforma del medio
        mapa.pintar_bloque(9, 6, 0)
        mapa.pintar_bloque(9, 7, 1)
        mapa.pintar_bloque(9, 8, 1)
        mapa.pintar_bloque(9, 9, 1)
        mapa.pintar_bloque(9, 10, 1)
        mapa.pintar_bloque(9, 11, 1)
        mapa.pintar_bloque(9, 12, 2)


        mapa.pintar_bloque(12, 14, 0)
        mapa.pintar_bloque(12, 15, 2)

        #mapa.pintar_bloque(13, 12, 8, False)
        #mapa.pintar_bloque(13, 13, 9, False)
        #mapa.pintar_bloque(13, 14, 9, False)
        #mapa.pintar_bloque(13, 15, 10, False)

        # Limite izquierdo de la pantalla
        mapa.pintar_bloque(13, 0, 7, True)
        mapa.pintar_bloque(12, 0, 7, True)
        mapa.pintar_bloque(11, 0, 7, True)
        mapa.pintar_bloque(10, 0, 7, True)

        # Limite derecho de la pantalla
        mapa.pintar_bloque(13, 19, 7, True)
        mapa.pintar_bloque(12, 19, 7, True)
        mapa.pintar_bloque(11, 19, 7, True)
        mapa.pintar_bloque(10, 19, 7, True)

        # Pinta todo el suelo
        for columna in range(0, 20):
            mapa.pintar_bloque(14, columna, 1)

        return mapa

    def hacer_explotar_enemigo(self, mi_disparo, el_enemigo):
        mi_disparo.eliminar()
        self.enemigos.remove(el_enemigo)
        el_enemigo.eliminar()

    def actualizar(self):
        if len(self.enemigos) < self.max_enemigos and random.random() > 0.99:
            self.agregar_enemigo()   

juego = Juego()
pilas.ejecutar()
