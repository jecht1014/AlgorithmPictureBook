import sys
import os
targetDir = "軌道計算入門/"
idx = os.path.dirname(os.path.abspath(__file__)).find(targetDir)
sys.path.append(os.path.dirname(os.path.abspath(__file__))[:idx + len(targetDir)])

from library.ConicCurve import Hyperbola

hyperbola = Hyperbola(vertex=2, coVertex=5)
hyperbola.calcRange(stop=10.0, step=0.01)
hyperbola.plot(hasAsymptote=True, hasFocus=True)