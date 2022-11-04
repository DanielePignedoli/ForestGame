#import numpy as np
#import igraph as ig
from forest_game import Forest
import matplotlib.pyplot as plt
from test_forest import to_graph, hole_distribution
import seaborn as sns
from time import time

#parameters
lattice_lenght = 80
interaction = 0.01
p_death = 0.1
p_birth = 0.9
max_size = 20
max_epoch = 10000

t_0 = time()

my_forest = Forest(lattice_lenght=lattice_lenght,
                   interaction=interaction,
                   p_death=p_death,
                   p_birth=p_birth,
                   max_size=max_size,
                   empty = False)


for epoch in range(max_epoch):
    my_forest.step()
    
#plt.imshow(my_forest.forest, cmap='jet')
#plt.colorbar()

t_1 = time()

#save only trees smaller than 5 meters (hole distribution), and remove boundaries
binary_forest = my_forest.forest[1:lattice_lenght+1,1:lattice_lenght+1] < 2

plt.imshow(binary_forest, cmap='jet')
plt.colorbar()

t_2 = time()

hole_graph = to_graph(binary_forest)
distribution = hole_distribution(hole_graph)



sns.displot(distribution, bins=30, log_scale=(True,True), kde = True)

t_3 = time()

print('first step',t_1-t_0)
print('second step',t_2-t_1)
print('tird step',t_3-t_2)


