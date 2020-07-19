import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# define spiral
#	has 4 prongs
#		each prong has
#			start_position
#			direction
#			length
#			angular_v
#			forward_v

num_points_in_ring = 10
radius = 1

test_plot = plt.figure()
ax = test_plot.add_subplot(111)
test_prong, = ax.plot([],[])

def init_animation():
	ax.set_xlim([-2,2])
	ax.set_ylim([-2,2])
	ax.set_aspect('equal')
	return test_prong,

def update(frame):
	theta = frame
	x = radius * np.cos(theta)
	y = radius * np.sin(theta)
	test_prong.set_data([0,x], [0,y])
	return test_prong,
	
ani = FuncAnimation(test_plot, update, frames=np.linspace(0,2*np.pi,num_points_in_ring), interval=100,
                    init_func=init_animation, blit=True)

plt.show()

