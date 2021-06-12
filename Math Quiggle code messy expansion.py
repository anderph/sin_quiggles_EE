import matplotlib.pyplot as plt
import numpy as np
import math


#general variable settings

step_size = 1

fig = plt.figure(1)
subplot1 = plt.subplot(111)
subplot1.axis('off')
subplot1.set_aspect('equal', adjustable='box')
# subplot1.set_ylim([0, 10])   # set the bounds to be 10, 10
# subplot1.set_xlim([0, 10])

def  plot_line(_coordinates, degrees, _length, subplotName=None):
    if subplotName == None:
        subplotName = subplot1
     # unpack the first point
    x, y = _coordinates
     # find the end point
    endy = y + _length * math.sin(math.radians(degrees))
    endx = x + _length * math.cos(math.radians(degrees))

     # plot the points
    subplotName.plot([x, endx], [y, endy])
    return (endx, endy)




coordinates = (0,0)
angle = 0
counter = 0

def reset_variables():
    global coordinates
    global angle
    global counter
    coordinates = (0,0)
    angle = 1
    counter = 1


def standard_quiggle_draw(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(360*4):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += counter
        counter += stepper
        # print(str(angle % 360), str(counter))
    reset_variables()

def length_exploration_of_quiggles(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(360*4):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += counter
        step_size += counter
        counter += stepper
    reset_variables()

def flip_flopper_quiggle(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    flipper = 1
    for i in range(360*4):
        coordinates = plot_line(coordinates,angle, step_size)
        flipper = -1 * flipper
        angle += counter
        counter += stepper * flipper
    reset_variables()

def exponential_quiggle_draw(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(360*8):
        coordinates = plot_line(coordinates,angle, step_size)
        angle = (counter ** 1.25)
        print(str(angle%360))
        counter += stepper
    reset_variables()

def fibonacci_mod_draw(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    new_fibo = 1
    old_fibo = 0
    temp_fibo = 0
    for i in range(70):
        coordinates = plot_line(coordinates,angle, step_size)
        angle = new_fibo
        temp_fibo = new_fibo % 360
        new_fibo = (new_fibo + old_fibo) % 360
        old_fibo = temp_fibo % 360

    reset_variables()

def geometric_series_quiggle(r_value):
    global coordinates
    global angle
    global counter
    global step_size
    term = r_value
    for i in range(360):
        coordinates = plot_line(coordinates,angle, step_size)
        angle = term
        term = term * r_value
        # print(str(angle % 360), str(counter))
    reset_variables()

def weird_square_root_archimedian_spiral(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(360*8):
        coordinates = plot_line(coordinates,angle, step_size)
        angle = counter ** (1/2)
        counter += stepper
        # print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(360*12):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += math.sin(counter/360)
        counter += stepper
        # print(str(angle % 360), str(counter))
    reset_variables()

def random(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(360*12):
        coordinates = plot_line(coordinates,angle, step_size)
        # angle += math.fabs(counter-180)
        counter += stepper
        # print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration_but_with_different_sequence(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(180):
        coordinates = plot_line(coordinates,angle, step_size)
        angle = math.sin(math.radians(counter))*180
        counter += stepper
        print(str(angle % 360), str(counter))
    reset_variables()

def mushroom(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(180):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += math.sin(math.radians(counter))*360
        counter += stepper
        print(str(angle % 360), str(counter))
    reset_variables()

def mushroom_not_really(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(180*4):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += math.sin(math.radians(counter))*180
        counter += stepper
        print(str(angle % 360), str(counter))
    reset_variables()

def special_case_of_sin_wave_exploration_but_with_different_sequence(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(180):
        coordinates = plot_line(coordinates,angle, step_size)
        angle = math.sin(math.radians(counter))*360
        counter += stepper
        print(str(angle % 360), str(counter))
    for i in range(180):
        coordinates = plot_line(coordinates,angle, step_size)
        angle = -math.sin(math.radians(counter))*360
        counter += stepper
        print(str(angle % 360), str(counter))
    reset_variables()

def circle_creator_but_non_trivial_maybe(stepper, iterations):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(iterations):
        coordinates = plot_line(coordinates,angle, step_size)
        counter += stepper
        angle = counter
        print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration_extended(stepper, division):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(360*24):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += 10*math.sin(counter*math.pi/division) ** 2
        counter += stepper
        # print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration_extended_critical_point(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(360*24):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += math.sin(counter/math.pi/50.5) ** 2
        counter += stepper
        # print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration_well_behaved_attempt_360(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(364*6):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += 360*math.sin(counter*math.pi) ** 2
        counter += stepper
        # print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration_well_behaved_attempt_180(stepper):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(364*6):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += 180*math.sin(counter*math.pi) ** 2
        counter += stepper
        # print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration_well_behaved_attempt_180_multiple_plots(height, width, start_value, length_multiplier):
    global coordinates
    global angle
    global counter
    global step_size
    figure, axis = plt.subplots(height, width)
    for k in range(width):
        for j in range(height):
            axis[j, k].axes.get_xaxis().set_ticks([])
            axis[j, k].axes.get_yaxis().set_ticks([])
            axis[j, k].set_aspect('equal', adjustable='box')
            axis[j, k].set_title("Graph 1/" + str(k+start_value+j*width))
            for i in range((k+start_value+j*width)*length_multiplier):
                coordinates = plot_line(coordinates,angle, step_size, axis[j,k])
                angle += 180*math.sin(counter*math.pi) ** 2
                counter += 1/(k+start_value+j*width)
                # print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration_well_behaved_attempt_90_multiple_plots(height, width, start_value, length_multiplier):
    global coordinates
    global angle
    global counter
    global step_size
    figure, axis = plt.subplots(height, width)
    for k in range(width):
        for j in range(height):
            axis[j, k].axes.get_xaxis().set_ticks([])
            axis[j, k].axes.get_yaxis().set_ticks([])
            axis[j, k].set_aspect('equal', adjustable='box')
            axis[j, k].set_title("Graph 1/" + str(k+start_value+j*width))
            for i in range((k+start_value+j*width)*length_multiplier):
                coordinates = plot_line(coordinates,angle, step_size, axis[j,k])
                angle += 90*math.sin(counter*math.pi) ** 2
                counter += 1/(k+start_value+j*width)
                # print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration_well_behaved_attempt_90(stepper, length):
    global coordinates
    global angle
    global counter
    global step_size
    for i in range(length):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += 90*math.sin(counter*math.pi) ** 2
        counter += stepper
        # print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration_well_behaved_attempt_variable_angular_multiplier(stepper, length, angular_multiplier):
    global coordinates
    global angle
    global counter
    global step_size
    subplot1.set_title("Graph 1/" + str(1/stepper))
    for i in range(length):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += angular_multiplier*math.sin(counter*math.pi) ** 2
        counter += stepper
        # print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration_well_behaved_attempt_variable_angular_multiplier_not_squared(stepper, length, angular_multiplier):
    global coordinates
    global angle
    global counter
    global step_size
    subplot1.set_title("Graph 1/" + str(1/stepper))
    for i in range(length):
        coordinates = plot_line(coordinates,angle, step_size)
        angle += angular_multiplier*math.fabs((math.sin(counter*math.pi)))
        counter += stepper
        # print(str(angle % 360), str(counter))
    reset_variables()


def sin_wave_exploration_well_behaved_attempt_90_multiple_plots(height, width, start_value, length_multiplier):
    global coordinates
    global angle
    global counter
    global step_size
    figure, axis = plt.subplots(height, width)
    plt.tight_layout()
    for k in range(width):
        for j in range(height):
            axis[j, k].axes.get_xaxis().set_ticks([])
            axis[j, k].axes.get_yaxis().set_ticks([])
            axis[j, k].set_aspect('equal', adjustable='box')
            axis[j, k].set_title("Graph 1/" + str(k+start_value+j*width))
            for i in range((k+start_value+j*width)*length_multiplier):
                coordinates = plot_line(coordinates,angle, step_size, axis[j,k])
                angle += 90*math.sin(counter*math.pi) ** 2
                counter += 1/(k+start_value+j*width)
                # print(str(angle % 360), str(counter))
    reset_variables()

def sin_wave_exploration_well_behaved_attempt_90_multiple_plots_different_files(iterations, start_value, length_multiplier):
    global coordinates
    global angle
    global counter
    global step_size
    for k in range(iterations):
        plt.figure(k)
        subplotter = plt.subplot(111)
        subplotter.axis('off')
        subplotter.set_aspect('equal', adjustable='box')
        subplotter.axes.get_xaxis().set_ticks([])
        subplotter.axes.get_yaxis().set_ticks([])
        subplotter.set_aspect('equal', adjustable='box')
        subplotter.set_title("Graph 1/" + str(k + start_value))
        for i in range((k + start_value) * length_multiplier):
            coordinates = plot_line(coordinates, angle, step_size, subplotter)
            angle += 90 * math.sin(counter * math.pi) ** 2
            counter += 1 / (k + start_value)
            # print(str(angle % 360), str(counter))
        plt.savefig("Sin Wave Quiggle, 90 deg, 1 over "+str(k+start_value), dpi=1200)
        reset_variables()

def sin_wave_exploration_well_behaved_attempt_multiple_files_and_variable_angular_multiplier(iterations,
                                                        start_value, length_multiplier, angular_multiplier):
    global coordinates
    global angle
    global counter
    global step_size
    for k in range(iterations):
        plt.figure(k)
        subplotter = plt.subplot(111)
        subplotter.axis('off')
        subplotter.set_aspect('equal', adjustable='box')
        subplotter.axes.get_xaxis().set_ticks([])
        subplotter.axes.get_yaxis().set_ticks([])
        subplotter.set_aspect('equal', adjustable='box')
        subplotter.set_title("Graph 1/" + str(k + start_value))
        for i in range((k + start_value) * length_multiplier):
            coordinates = plot_line(coordinates, angle, step_size, subplotter)
            angle += angular_multiplier * math.sin(counter * math.pi) ** 2
            counter += 1 / (k + start_value)
            # print(str(angle % 360), str(counter))
        plt.savefig("Sin Wave Quiggle, " + str(angular_multiplier) + " deg, 1 over "+str(k+start_value), dpi=1200)
        print(str(k+start_value) + " is looped, " + str(angular_multiplier) +" is multiplier" )
        plt.clf()
        reset_variables()

sin_wave_exploration_well_behaved_attempt_90(1/258, 600)

# sin_wave_exploration_well_behaved_attempt_variable_angular_multiplier(1/4/8, 300, 45)

# sin_wave_exploration_well_behaved_attempt_variable_angular_multiplier_not_squared(1/9, 2000, 180)

# for j in range(24):
    # sin_wave_exploration_well_behaved_attempt_multiple_files_and_variable_angular_multiplier(50,2,4*(int(360/((j+1)*15))),(j+1)*15)



# Initialise the subplot function using number of rows and columns
# sin_wave_exploration_well_behaved_attempt_90_multiple_plots_different_files(10, 2, 8)


        #this is a good way of showing many plots on the same graph. though it does not work for all thing
        #as the length required for the infinite ones should be less than finite (or it will just look like a line)

# sin_wave_exploration_well_behaved_attempt_180_multiple_plots(3, 4, 3, 2)
# plt.savefig('big list of quiggles.svg')


# Combine all the operations and display
# plt.show()

# plt.show()

# sin_wave_exploration_well_behaved_attempt_90(1/(1+1), (1+1)*5)
# plt.show()

# sin_wave_exploration_well_behaved_attempt_180(1/366)




# print(math.radians(360))
# sin_wave_exploration_extended(1/9,50)
# sin_wave_exploration_extended(1,360)
# sin_wave_exploration_extended(1,360)
# sin_wave_exploration_extended(1,360)

# mushroom_not_really(2)
# mushroom(2)

# circle_creator_but_non_trivial_maybe(230, 500)

# random(1)
# special_case_of_sin_wave_exploration_but_with_different_sequence(1)






# sin_wave_exploration_but_with_different_sequence(1)

# sin_wave_exploration(0.5)

# weird_square_root_archimedian_spiral(100)

# geometric_series_quiggle(1.02)

# standard_quiggle_draw(1)

# fibonacci_mod_draw(1)

# exponential_quiggle_draw(1)
        # for this one you can explore why the circle in the middle is untouched and whether the circle will ever cross
# flip_flopper_quiggle(1)
# length_exploration_of_quiggles(3)
# standard_quiggle_draw(1)

# Show the plot
plt.show()