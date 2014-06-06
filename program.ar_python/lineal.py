# -*- coding: utf-8 -*-

from decimal import Decimal
from fractions import Fraction
from graficar import graficar

try:
    entrada = raw_input
except:
    entrada = input

def numero(valor):
    valor = valor.split('/')

    if len(valor) == 2:
        return Fraction(int(valor[0]), int(valor[1]))
    else:
        return Fraction(valor[0])

def calcular_lineal(m, b):
    if m == 0:
        return {
            'ordenada': b,
            'abscisa': None
        }

    else:
        return {
            'ordenada': b,
            'abscisa': Fraction(-b / m)
        }

if __name__ == '__main__':
    print('La ecuación de la recta es Y = mX + b\n')
    m = numero(entrada('Ingrese la pendiente de la recta (m): '))
    b = numero(entrada('Ingrese el término independiente (b): '))
    print('')

    print('Calculando Y = %sX + %s\n' % (m, b))

    resultado = calcular_lineal(m, b)

    if resultado['abscisa'] == None:
        print('Ordenada al origen: %s' % resultado['ordenada'])
        print('Abscisa al origen : {}')

    else:
        print('Ordenada al origen: %s' % resultado['ordenada'])
        print('Abscisa al origen : %s' % resultado['abscisa'])

    graficar('lineal_', 'y(x) = (%s*x) + %s' % (m, b))



