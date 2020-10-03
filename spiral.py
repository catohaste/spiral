import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# define spiral
#	has 4 prongs
#		each prong has
#			start_position
#			direction
#			length

animation_duration = 3000

num_points_in_ring = 50
radius = 1

spiralN = 4

prongN = 4
prongs_list = []
centre_of_mass_list = []

fig = plt.figure(figsize=(12,4))
axs = {}
for spiral in range(spiralN):
    axs[spiral] = fig.add_subplot(1,spiralN,spiral+1)

    for idx in range(prongN):
        line, = axs[spiral].plot([],[])
        prongs_list.append(line)

    mass, = axs[spiral].plot([],[],'-ok',markersize=10)
    centre_of_mass_list.append(mass)

prongs = tuple(prongs_list)
centre_of_mass = tuple(centre_of_mass_list)

def init_animation():
    for spiral in range(spiralN):
        axs[spiral].set_xlim([-1.5,1.5])
        axs[spiral].set_ylim([-1.5,1.5])
        axs[spiral].set_aspect('equal')
        axs[spiral].axis('off')
    return prongs + centre_of_mass

def update(frame):
    theta = [frame, frame + np.pi/2, frame + np.pi, frame + (3*np.pi)/2]
    direction = np.asarray([[1,1,1,1], [1,1,1,-1], [1,1,-1,-1], [1,-1,1,-1]])

    x = np.ndarray(direction.shape)
    y = np.ndarray(direction.shape)
    for spiral in range(spiralN):
        x[spiral,:] = radius * np.cos(np.multiply(direction[spiral,:],theta))
        y[spiral,:] = radius * np.sin(np.multiply(direction[spiral,:],theta))

    avg_x = np.mean(x,axis=1)
    avg_y = np.mean(y,axis=1)

    x = x.flatten()
    y = y.flatten()

    for idx, prong in enumerate(prongs):
        prong.set_data([0,x[idx]], [0,y[idx]])
    
    for spiral in range(spiralN):
        centre_of_mass[spiral].set_data([avg_x[spiral]], [avg_y[spiral]])
    
    return prongs + centre_of_mass

ani = FuncAnimation(fig, update, frames=np.linspace(0,2*np.pi,num_points_in_ring), interval = animation_duration / (num_points_in_ring - 1), init_func = init_animation, blit = True)

plt.show()

