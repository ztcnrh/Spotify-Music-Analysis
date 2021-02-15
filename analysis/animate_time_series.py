# Dependecies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import rcParams
from matplotlib.animation import FuncAnimation
from itertools import count
import os

print(os.chdir('/Users/ZTC/Desktop/Penn Data Analytics Bootcamp/Projects/Project 1 - Spotify Data (Presentation 2:20)/bootcamp-project1-spotify/analysis/'))

# Definiting an "animate" function to grab the data that's being updated as we go, and plot it.
def animate(i):
    data = pd.read_csv('../output_csv/data_gen.csv')
    x_years = data['year']
    y_acousticness = data['acousticness']
    y_danceability = data['danceability']
    y_energy = data['energy']
    y_instrumentalness = data['instrumentalness']
    y_liveness = data['liveness']
    y_speechiness = data['speechiness']
    y_valence = data['valence']

    plt.cla()

    plt.plot(x_years, y_acousticness, label='Acousticness')
    plt.plot(x_years, y_danceability, label='Danceability')
    plt.plot(x_years, y_energy, label='Energy')
    plt.plot(x_years, y_instrumentalness, label='Instrumentalness')
    plt.plot(x_years, y_liveness, label='Liveness')
    plt.plot(x_years, y_speechiness, label='Speechiness')
    plt.plot(x_years, y_valence, label='Valence')

    plt.grid(True, color='k', linestyle=':', alpha=0.25)
    plt.title("Audio Features vs. Year")
    plt.xlabel("Year")
    plt.ylabel("Rating")
    plt.legend(loc='upper right', fontsize='small')

# Use function "FuncAnimation" from matplotlib.animation to continuously update
# the plot generated from our "animate" function.
ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.show()
