import numpy as np
import math
import matplotlib.pyplot as plt
import vtk
from matplotlib import pyplot
from matplotlib import collections as mc
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
from vtk.util.numpy_support import vtk_to_numpy

def create_horizontal_points(vertical_index):
	points = [(i*segment, vertical_index*L0) for i in range(0, resolution*n_cells + 1)]
	return np.asarray(points)

def create_vertical_points(horizontal_index):
	points = [(horizontal_index*L0, i*segment) for i in range(0, resolution*n_cells + 1)]
	return np.asarray(points)

if __name__ == '__main__':

	# plot from vtk
	reader = vtk.vtkXMLUnstructuredGridReader()
	reader.SetFileName("data/mesh_assemble.vtu")
	reader.Update()

	data = reader.GetOutput()
	points = data.GetPoints()
	npts = points.GetNumberOfPoints()
	x = vtk_to_numpy(points.GetData())
	triangles =  vtk_to_numpy(data.GetCells().GetData())
	ntri = triangles.size//4  # number of cells
	tri = np.take(triangles, [n for n in range(triangles.size) if n%4 != 0]).reshape(ntri,3)

	plt.figure(figsize=(8, 8))
	plt.triplot(x[:,0], x[:,1], tri, marker='o', markersize=1, linewidth=0.5, color='b')
	plt.gca().set_aspect('equal')
	plt.axis('off')

	# homemade plot
	plt.figure(figsize=(8, 8))
	L0 = 0.5
	n_cells = 5
	resolution = 10
	segment = L0/resolution

	for i in range(0, n_cells + 1):
		points = create_horizontal_points(i)
		plt.plot(points[:,0], points[:, 1], marker ='o', markersize=1, linewidth=0.5, color='b')

	for i in range(0, n_cells + 1):
		points = create_vertical_points(i)
		plt.plot(points[:,0], points[:, 1], marker ='o', markersize=1, linewidth=0.5, color='b')

	plt.axis('off')
	plt.axis('equal')
	plt.show()





