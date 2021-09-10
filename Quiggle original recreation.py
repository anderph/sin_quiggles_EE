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
     # subplot1.plot([x, endx], [y, endy], 'bo') #specifies the color
     return (endx, endy)


fig = plt.figure()
subplot1 = plt.subplot(111)
# subplot1.set_ylim([0, 10])   # set the bounds to be 10, 10
# subplot1.set_xlim([0, 10])


coordinates = (0,0)
angle = 0
modifier = 1
counter = 1

time = 360*2+2

# time = 2

for i in range(time):
    print('-'+str(counter % 360)+'-')
    coordinates = plot_line(coordinates,angle, 1)
    angle += counter
    counter += modifier
# coordinates = plot_line(coordinates,90, 1)

# Show the plot
plt.show()