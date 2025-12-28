import numpy as np
import matplotlib.pyplot as plt
from afv.finite_voronoi import PhysicalParams, FiniteVoronoiSimulator


pts = [[0.0, 0.0]]
simulator = FiniteVoronoiSimulator(np.array(pts), PhysicalParams)

ax = simulator.plot_2d()
plt.show()
