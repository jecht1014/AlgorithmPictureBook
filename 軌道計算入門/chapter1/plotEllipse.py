import sys
sys.path.append('../')

from library.ConicCurve import Ellipse

ellipse = Ellipse(majorAxis=10, minorAxis=4)
ellipse.calcRange(0.01)
ellipse.plot()