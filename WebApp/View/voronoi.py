import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np

def voronoi_funkcija(new_point = [50, 50]):

	M = 10
	points = np.random.uniform(0, 100, size=(M, 2))
	dict=()
	list_of_hospitals=["Dragiše Mišovića","Bolnica Svetozar Markovic","Institut za majku i dete","Bežanijska kosa","A","B","K","D","L","R"]

	  
	vor = Voronoi(points)
	voronoi_plot_2d(vor)
 
	plt.plot(new_point[0], new_point[1], 'ro')

	point_index = np.argmin(np.sum((points - new_point)**2, axis=1))
	ridges = np.where(vor.ridge_points == point_index)[0]
	vertex_set = set(np.array(vor.ridge_vertices)[ridges, :].ravel())
	region = [x for x in vor.regions if set(x) == vertex_set][0]

	polygon = vor.vertices[region]
	print(points[point_index],list_of_hospitals[point_index])
	plt.fill(*zip(*polygon), color='yellow')
	
	'''
	fig = voronoi_plot_2d(vor)

	fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='orange',
					line_width=2, line_alpha=0.6, point_size=2)
	plt.show()
	'''
	
	return plt.gcf()
