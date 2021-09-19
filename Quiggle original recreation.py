import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import math


#general variable settings
step_size = 1

colorlist = list(mcolors.BASE_COLORS)
print(list(mcolors.BASE_COLORS))
color = 1

def  plot_line(coords, degrees, length):
     # unpack the first point
     x, y = coords

     # find the end point
     endy = y + length * math.sin(math.radians(degrees))
     endx = x + length * math.cos(math.radians(degrees))

     # colors
     color = int(( iterations/90+ 3) % 7)
     subplot1.plot([x, endx], [y, endy], colorlist[color], linewidth=0.8)
    # no colors:
    #  subplot1.plot([x, endx], [y, endy], linewidth=0.4)
     # subplot1.plot([x, endx], [y, endy], 'bo') #specifies the color
     return (endx, endy)

fig = plt.figure()
subplot1 = plt.subplot(111)
# subplot1.set_ylim([0, 10])   # set the bounds to be 10, 10
# subplot1.set_xlim([0, 10])

#
# subplot1.title("Mono H-Quiggle", fontdict=None, loc='center', pad=None, **kwargs


coordinates = (0,0)
angle = 0
iterations = 1
modifier = 179
counter = 1

time = 360*2

# time = 2
#
# x=0
# y=0
# for i in range(360):
#     x += x + 1 * math.sin(math.radians(angle))
#     x += + 1 * math.sin(math.radians(angle))
#     angle += counter
#     counter += modifier
#     iterations += 1
#     coordinates = (x,y)
#

for i in range(time):
    print('-'+str(counter % 360)+'-')
    coordinates = plot_line(coordinates,angle, 1)
    angle += counter
    counter += modifier
    iterations += 1
plt.title("Pseudo Mono H-Quiggle first 720", fontsize=20)
# coordinates = plot_line(coordinates,90, 1)
# plt.savefig('pseudo mono H-Quiggle first 720.png', dpi = 600)



# Show the plot
plt.show()