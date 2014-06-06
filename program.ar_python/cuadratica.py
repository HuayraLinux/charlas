# -*- coding: utf-8 -*-

from decimal import Decimal
from fractions import Fraction
from lineal import numero
from graficar import graficar

try:
    entrada = raw_input
except:
    entrada = input

def calcular_raices(a, b, discriminante):
    x1 = (-b + (discriminante ** 1/2)) / (2*a)

    if discriminante == 0:
        x2 = x1

    else:
        x2 = (-b - (discriminante ** 1/2)) / (2*a)


    return {
        'x1': x1,
        'x2': x2
    }

def calcular_cuadratica(a, b, c):
    x_vertice = Fraction(-b / (2*a)) # Eje de simetría
    y_vertice = a * (x_vertice ** 2) + (b * x_vertice) + c

    discriminante= (b ** 2) - (4 * a * c)

    datos = {
            'ordenada': b,
            'vertice': (x_vertice, y_vertice),
    }

    if discriminante < 0:
        datos['raices'] = None

    else:
        datos['raices'] = calcular_raices(a, b, discriminante)

    return datos

if __name__ == '__main__':
    print('La ecuación de la parábola es Y = aX² + bX + c\n')
    a = numero(entrada('Ingrese el término al cuadrado (a): '))
    b = numero(entrada('Ingrese el término lineal (b): '))
    c = numero(entrada('Ingrese el término independiente (c): '))
    print('')

    print('Calculando Y = %sX² + %sX + %s\n' % (a, b, c))

    resultado = calcular_cuadratica(a, b, c)

    print('Ordenada al origen: %s' % resultado['ordenada'])
    print('El vértice está en las coordenadas: (%s, %s)' % (
        resultado['vertice'][0],
        resultado['vertice'][1]
    ))
    if resultado['raices'] == None:
        print('No hay raices.')

    else:
        print('Las raices son: x1 = %s, x2 = %s' % (
            resultado['raices']['x1'],
            resultado['raices']['x2']
        ))

    graficar('cuadratica_', 'y(x) = (%s*x**2) + (%s*x) + %s' % (a, b, c))



