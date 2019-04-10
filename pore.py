import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection

def build_base_pore(coords_fn, n_points):
    thetas = [float(i) * 2 * math.pi / n_points for i in range(n_points)]
    radii = [coords_fn(float(i) * 2 * math.pi / n_points) for i in range(n_points)]
    points = [(rtheta * np.cos(theta), rtheta * np.sin(theta))
              for rtheta, theta in zip(radii, thetas)]
    return np.array(points), np.array(radii), np.array(thetas)

def coords_fn(theta):
    return r0 * (1 + c1 * np.cos(4 * theta) + c2 * np.cos(8 * theta))

def build_pore_polygon(base_pore_points, offset):
    points = [(p[0] + offset[0], p[1] + offset[1]) for p in base_pore_points]
    points = np.asarray(points)
    pore = Polygon(points)
    return pore

if __name__ == '__main__':

    porosity = 0.5
    L0 = 0.5
    c1 = -0.2
    c2 = 0.2
    pore_radial_resolution = 120
    n_cells = 3
    patches = []
    colors = []

    points = [(0, 0), (n_cells*L0, 0), (n_cells*L0, n_cells*L0), (0, n_cells*L0)]
    frame = Polygon(np.asarray(points))
    patches.append(frame)
    colors.append((254./255.,127./255.,156./255.))

    r0 = L0 * math.sqrt(2 * porosity) / math.sqrt(math.pi * (2 + c1**2 + c2**2))
    r0 = 0.2


    for i in range(n_cells):
        for j in range(n_cells):
            # c1 = np.random.normal(0, 0.1)
            # c2 = np.random.normal(0, 0.1)
            base_pore_points, radii, thetas = build_base_pore(
                coords_fn, pore_radial_resolution)            
            pore = build_pore_polygon(
                base_pore_points, offset=(L0 * (i + 0.5), L0 * (j + 0.5)))

            patches.append(pore)
            colors.append((1,1,1))

    fig, ax = plt.subplots()
    p = PatchCollection(patches, alpha=1, edgecolor=None, facecolor=colors)
    ax.add_collection(p)
    plt.axis('equal')
    plt.axis('off')
    plt.show()