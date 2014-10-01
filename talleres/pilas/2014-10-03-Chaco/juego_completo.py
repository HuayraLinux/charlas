#!/bin/env python
# -*- encoding: utf-8 -*-

import sys
import pilas
import random

pilas.iniciar()
def crear_mapa():
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

def colisiona_premio(marciano, estrella):
     pilas.avisar("Ganaste genio !") 

mapa = crear_mapa()
marciano = pilas.actores.Martian(mapa)
marciano.radio_de_colision = 30

estrella = pilas.actores.Estrella(x=-80,y=180)
estrella.radio_de_colision = 35
pilas.escena_actual().colisiones.agregar(marciano, estrella, colisiona_premio)

enemigos = []

def agregar_enemigo():
    enemigo = pilas.actores.Aceituna()
    enemigo.x = random.uniform(-300,300)
    enemigo.y = 200
    enemigo.aprender(pilas.habilidades.PerseguirAOtroActor, objetivo=marciano, velocidad=0.7)
    enemigo.aprender(pilas.habilidades.PuedeExplotar)
    enemigos.append(enemigo)

agregar_enemigo()

def enemigo_colisiona_marciano(marciano, enemigo):
    marciano.x = -200
    marciano.y = 0
    enemigo.x = random.uniform(-300,300)
    enemigo.y = 200


def hacer_explotar_enemigo(mi_disparo, el_enemigo):
    mi_disparo.eliminar()
    enemigos.remove(el_enemigo)
    el_enemigo.eliminar()

pilas.escena_actual().colisiones.agregar(marciano, enemigos, enemigo_colisiona_marciano)

marciano.habilidades.Disparar.definir_colision(enemigos, hacer_explotar_enemigo)

pilas.ejecutar()
