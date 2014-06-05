from math import pi
from pyx import *
from pyx.graph import axis


def graficar(nombre=None, func=None, puntos=20, max=None, min=None, estilo=None):
    if not nombre and not func:
        return

    if not max:
        max = 4

    if not min:
        min = -4


    xgridpainter = axis.painter.regular(gridattrs=[])
    ygridpainter = axis.painter.regular(gridattrs=[attr.changelist([style.linestyle.dashed, None])])

    g = graph.graphxy(width=10,
                      x=axis.lin(painter=xgridpainter,
                                 #divisor=pi,
                                 #texter=axis.texter.rational(suffix=r"\pi"),
                                 min=min*10,
                                 max=max*10),
                      y=axis.lin(painter=ygridpainter))

    g.plot(graph.data.function(func, points=puntos))

    g.writePDFfile(nombre)



def test():
    g = graph.graphxy(width=8)
    # either provide lists of the individual coordinates
    g.plot(graph.data.values(x=list(range(10)), y=list(range(10))))
    # or provide one list containing the whole points
    g.plot(graph.data.points(list(zip(list(range(10)), list(range(10)))), x=1, y=2))
    g.writeEPSfile("points")
    g.writePDFfile("points")
