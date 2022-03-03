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
color = 0

fig = plt.figure()
subplot1 = plt.subplot(111)
# subplot1.set_ylim([-.5, 3.5])   # set the bounds to be 10, 10
# subplot1.set_xlim([-1, 3])

subplot1.set_aspect('equal', adjustable='box')

# subplot1.title("Mono H-Quiggle", fontdict=None, loc='center', pad=None, **kwargs


coordinates = (0,0)
angle = 0
iterations = 0
modifier = 10
counter = 15

time = 7


def plot_line(coords, degrees, length):
    # unpack the first point
    global color
    global counter
    x, y = coords

    # find the end point
    endy = y + length * math.sin(math.radians(degrees))
    endx = x + length * math.cos(math.radians(degrees))

    # colors
    # color = int(( iterations/90+ 3) % 7)
    # if counter >= 360*3:
    #     color = 4
    # if counter == 1:
    #     color = color + 1

    # subplot1.plot([x, endx], [y, endy], colorlist[color], linewidth=1)
    # no colors:
    # subplot1.plot([x, endx], [y, endy], linewidth=0.4)
    subplot1.plot([x, endx], [y, endy], 'black', linewidth=1) #specifies the color
    return (endx, endy)

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

# for i in range(time):
#     # print('-'+str(counter % 360)+'-')
#     # if counter % 360 == 1 :
#         # print(iterations)
#         # print("---" + str(i) + "---x:" + str(coordinates[0])+ '---y:' + str(coordinates[1]))
#     angle += counter
#     coordinates = plot_line(coordinates, angle, 1)
#     counter += modifier
#     iterations += 1
#     print("------" + str(counter % 360))




x,y = (0,0)
endx,endy=(1,0)
for i in range(time):
    angle += counter
    counter += modifier
    iterations += 1

    subplot1.plot([endx, endx+.75], [endy, endy], 'green', linewidth=.5)
    # subplot1.plot([x, endx + 1.5*(endx-x)], [y, endy + 1.5*(endy-y)], 'purple', linewidth=1)

    subplot1.plot([x, endx], [y, endy], 'black', linewidth=2)
    endy = y + 1 * math.sin(math.radians(angle))
    endx = x + 1 * math.cos(math.radians(angle))

    # subplot1.plot([x, endx], [y, endy], 'black', linewidth=2)
    # subplot1.plot([endx, endx + .5], [endy, endy], 'green', linewidth=1)
    if (i != time-1): subplot1.plot([endx, endx + .75 * (endx - x)], [endy, endy + .75 * (endy - y)], 'purple', linewidth=.5)
    x, y = (endx, endy)



title = "H-Quiggle Step-size: 10 (t₁=15)"
plt.title(title, fontsize=20)
# coordinates = plot_line(coordinates,90, 1)
# plt.savefig(title+'.png',dpi=200)



# Show the plot
plt.show()