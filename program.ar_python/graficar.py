from math import pi
from pyx import *
from pyx.graph import axis


def graficar(nombre=None, func=None, puntos=20, max=20, min=-20, estilo=None):
    if not nombre and not func:
        return

    gridpainter = axis.painter.regular(gridattrs=[attr.changelist([style.linestyle.dashed, None])])

    g = graph.graphxy(width=10,
                      x=axis.lin(painter=gridpainter),
                      y=axis.lin(painter=gridpainter))

    g.plot(graph.data.function(func, max=max, min=min))

    g.writePDFfile(nombre)



if __name__ == '__main__':
    g = graph.graphxy(width=8)
    # either provide lists of the individual coordinates
    g.plot(graph.data.function(func, points=puntos))
    # or provide one list containing the whole points
    g.plot(graph.data.points(list(zip(list(range(10)), list(range(10)))), x=1, y=2))
    g.writePDFfile("points")
