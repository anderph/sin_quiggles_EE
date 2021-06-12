import matplotlib.pyplot as plt
import numpy as np
import math


#general variable settings

step_size = 1


def  plot_line(coords, degrees, length):
     # unpack the first point
     x, y = coords

     # find the end point
     endy = y + length * math.sin(math.radians(degrees))
     endx = x + length * math.cos(math.radians(degrees))

     # plot the points
     subplot1.plot([x, endx], [y, endy])
     return (endx, endy)


fig = plt.figure()
subplot1 = plt.subplot(111)
# subplot1.set_ylim([0, 10])   # set the bounds to be 10, 10
# subplot1.set_xlim([0, 10])


coordinates = (0,0)
angle = 1
counter = 1

for i in range(720):
    coordinates = plot_line(coordinates,angle, 1)
    angle += counter
    counter += 1


# Show the plot
plt.show()