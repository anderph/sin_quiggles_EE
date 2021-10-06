import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl
import numpy as np
import math


mpl.rcParams['figure.dpi'] = 200


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
     color = int(((iterations-1)/360 ) % 7)
     # if counter >= 360*3:
     #     color = 4
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
modifier = 70
counter = 0

time = 360*8*2*2

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


# title = "Two Features of H-Quiggle, a = 1"
title = str(modifier)
plt.title(title, fontsize=20)
# coordinates = plot_line(coordinates,90, 1)
# plt.savefig(title+'.png', dpi=300)



# Show the plot
plt.show()