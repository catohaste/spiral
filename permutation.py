import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

from mpl_toolkits.axes_grid1 import ImageGrid

num_points_in_ring = 100
radius = 1

spiralN = 4

prongN = 4
prongs_list = []
points_list = []
centre_of_mass_list = []

# fig = plt.figure(figsize=(6,4))
fig = plt.figure(figsize=(12,3))

axs = ImageGrid(fig, (0,0,1,1),
                 nrows_ncols=(1, 4),  # creates 2x2 grid of axes
                 axes_pad=0,  # pad between axes in inch.
                 share_all=True
                 )
                 
axs[0].get_yaxis().set_ticks([])
axs[0].get_xaxis().set_ticks([])

for spiral in range(spiralN):
    
    theta_zero = [0, np.pi/2, np.pi, (3*np.pi)/2]
    direction = np.asarray([[1,1,1,1], [1,1,1,-1], [1,1,-1,-1], [1,-1,1,-1]])
    
    circle = plt.Circle((0, 0), radius, facecolor='none', edgecolor='black', linewidth=1)
    axs[spiral].add_patch(circle)
    
    theta_zero = [0, np.pi/2, np.pi, (3*np.pi)/2]
    direction = np.asarray([[1,1,1,1], [1,1,1,-1], [1,1,-1,-1], [1,-1,1,-1]])
        
    for point_idx, theta in enumerate(theta_zero):
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        
        c = direction[spiral, point_idx]
        if c > 0:
            color = 'C0'
        else:
            color = 'C3'            
        mass, = axs[spiral].plot(x,y,'o',markersize=8, c=color)
    
    axs[spiral].set_xlim([-1.5,1.5])
    axs[spiral].set_ylim([-1.5,1.5])
    axs[spiral].set_aspect('equal')
    axs[spiral].axis('off')
    
plt.show()

fig.savefig("permutation.jpg")