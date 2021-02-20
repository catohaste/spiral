import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from matplotlib import rc

# define spiral
#	has 4 prongs
#		each prong has
#			start_position
#			direction
#			length

rc('animation', html='html5')

animation_duration = 3000

num_points_in_ring = 100
radius = 1

spiralN = 4

prongN = 4
prongs_list = []
points_list = []
centre_of_mass_list = []

fig = plt.figure(figsize=(12,4))
# fig = plt.figure(figsize=(6,4))
axs = {}
colors = ['C0', 'C1', 'C2', 'C3']
for spiral in range(spiralN):
    # axs[spiral] = fig.add_subplot(2,2,spiral+1)
    axs[spiral] = fig.add_subplot(1,spiralN,spiral+1)

    for idx in range(prongN):
        line, = axs[spiral].plot([],[], color = colors[idx])
        point, = axs[spiral].plot([],[], '-o', markersize=5, color = colors[idx])
        prongs_list.append(line)
        points_list.append(point)

    mass, = axs[spiral].plot([],[],'ok',markersize=10)
    centre_of_mass_list.append(mass)

prongs = tuple(prongs_list)
points = tuple(points_list)
centre_of_mass = tuple(centre_of_mass_list)

def init_animation():
    for spiral in range(spiralN):
        axs[spiral].set_xlim([-1.5,1.5])
        axs[spiral].set_ylim([-1.5,1.5])
        axs[spiral].set_aspect('equal')
        axs[spiral].axis('off')
    return prongs + points + centre_of_mass

def update(frame):
    theta_zero = [0, np.pi/2, np.pi, (3*np.pi)/2]
    direction = np.asarray([[1,1,1,1], [1,1,1,-1], [1,1,-1,-1], [1,-1,1,-1]])

    x = np.ndarray(direction.shape)
    y = np.ndarray(direction.shape)
    for spiral in range(spiralN):
        x[spiral,:] = radius * np.cos(theta_zero + frame * direction[spiral,:])
        y[spiral,:] = radius * np.sin(theta_zero + frame * direction[spiral,:])

    avg_x = np.mean(x,axis=1)
    avg_y = np.mean(y,axis=1)

    x = x.flatten()
    y = y.flatten()

    for idx, prong in enumerate(prongs):
        prong.set_data([0,x[idx]], [0,y[idx]])
        points[idx].set_data([x[idx]], [y[idx]])
    
    for spiral in range(spiralN):
        centre_of_mass[spiral].set_data([avg_x[spiral]], [avg_y[spiral]])
        
    return prongs + points + centre_of_mass
    
fig.tight_layout()

ani = FuncAnimation(fig, update, frames=np.linspace(0,2*np.pi,num_points_in_ring), interval = animation_duration / (num_points_in_ring - 1), init_func = init_animation, blit = True)

plt.show()

# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=24)
# ani.save('animation.mp4', writer=writer)

ani.save('animation.gif', writer='imagemagick', fps=24)

