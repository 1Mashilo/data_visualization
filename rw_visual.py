import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Create a random walk object and generate the walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Set the style for the plot
    plt.style.use('classic')

    # Create a figure and axis for the scatter plot
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)


    # Use point_numbers for color mapping
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Set the aspect ratio to equal for a square plot
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    # Display the plot
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
