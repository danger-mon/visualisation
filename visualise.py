import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def update(ind):
    return array[ind*numpass:ind*numpass+numpass, :]

def animate(frame):
    positions = update(frame)
    scatter.set_offsets(positions)

if __name__ == "__main__":
    
    parser = ArgumentParser(description="")
    parser.add_argument('data_file', help="Input CSV file for the data.")
    parser.add_argument('num_passengers', type=int, help="Number of passengers in data file.")

    arguments = parser.parse_args()

    filepath = arguments.data_file
    array = np.genfromtxt(filepath, delimiter=',')
    numpass = arguments.num_passengers

    positions = array[0:numpass, :]

    figure = plt.figure()
    axes = plt.axes(xlim=(0, 50), ylim=(0, 10))
    scatter = axes.scatter(positions[:, 0], positions[:, 1], marker='o', edgecolor='k', lw=0.5)

    anim = animation.FuncAnimation(figure, animate, frames=1000, interval=30)
    anim.save('visualisation.mp4')