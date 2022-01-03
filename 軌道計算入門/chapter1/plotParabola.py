import sys
sys.path.append('../')

from library.ConicCurve import Parabola

parabola = Parabola(forcus=1)
parabola.calcRange(0, 10, 0.1)
parabola.plot()