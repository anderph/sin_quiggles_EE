import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl
import numpy as np
import math


mpl.rcParams['figure.dpi'] = 300
fig = plt.figure()
subplot1 = fig.add_subplot(1,1,1)
# subplot1.set_ylim([-4, 4])

#general variable settings

def get_angle_plot(color = None, origin = [0,0],theta1=0, theta2=0, len_x_axis = 1, len_y_axis = 1):
    _angle = math.fabs(theta1-theta2)

    if color is None:
        color = 'b'# Uses the color of line 1 if color parameter is not passed.

    return  mpl.patches.Arc(origin, len_x_axis, len_y_axis, 0, theta1, theta2, color=color, label = str(angle)+u"\u00b0")

def get_angle_text(angle_plot, _angle):
    # Get the vertices of the angle arc
    vertices = angle_plot.get_verts()
    print(vertices)
    # Get the midpoint of the arc extremes
    x_width = (vertices[0][0] + vertices[-1][0]) / 2.0
    y_width = (vertices[0][5] + vertices[-1][6]) / 2.0

    #print x_width, y_width
    the_angle = _angle
    separation_radius = max(x_width/2.0, y_width/2.0)

    return [ x_width + separation_radius, y_width + separation_radius, the_angle]


def plot_line(coords, degrees, length):
    # unpack the first point
    x, y = coords

    # find the end point
    endy = y + length * math.sin(math.radians(degrees))
    endx = x + length * math.cos(math.radians(degrees))

    subplot1.plot([x, endx], [y, endy], 'black', linewidth=1)

    subplot1.plot([endx, 2*endx-x], [endy, 2*endy-y], 'black', linewidth=1, linestyle='dashed')
    return (endx, endy)



# subplot1.set_ylim([0, 10])   # set the bounds to be 10, 10
# subplot1.set_xlim([0, 10])
# subplot1.title("Mono H-Quiggle", fontdict=None, loc='center', pad=None, **kwargs


coordinates = (0,0)
angle = 0
oldangle = 0
iterations = 1
modifier = 4
counter = 1

time = 5

listoflines = []

for i in range(time):
    print('-'+str(counter % 360)+'-')
    oldcoords = coordinates
    coordinates = plot_line(coordinates,angle, 1)
    # print(coordinates)
    listoflines.append([oldcoords,coordinates, (angle %360), (oldangle % 360)])
    oldangle = angle
    angle += counter
    counter += modifier
    iterations += 1

# print(listoflines)

title = "H-Quiggle with Step-Size of 1"
plt.title(title, fontsize=20)


# subplot1.set_ylim([0, 0.4])
# subplot1.set_xlim([0,.7])

for i in range(1, len(listoflines)):
    oldcoords, coordinates, angle, oldangle = listoflines[i]
    # patch = get_angle_plot(origin=oldcoords, theta1=0, theta2=angle, color='green',len_x_axis=1, len_y_axis=coordinates[1])
    # subplot1.add_patch(patch)
    patch = get_angle_plot(origin=oldcoords, theta1=oldangle, theta2=angle,len_x_axis=1, len_y_axis=1)
    subplot1.add_patch(patch)

# Show the plot
# plt.legend()
plt.savefig(title+'.png', dpi=300)
plt.show()
