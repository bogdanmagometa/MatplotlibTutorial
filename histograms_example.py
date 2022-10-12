import matplotlib.pyplot as plt
import numpy as np

with open("Goals.txt", "r") as in_f:
    homeTeamGoals = [int(i) for i in in_f.readline().strip().split()]
    awayTeamGoals = [int(i) for i in in_f.readline().strip().split()]

fig1 = plt.figure(figsize=(10, 5))

ax1 = fig1.add_subplot(1, 1, 1)

N, bins, patches = ax1.hist(x=(awayTeamGoals, homeTeamGoals,), bins=4, color=["magenta", "blue"], align="mid", 
         range=(1, 5), cumulative=False, width=0.3)

plt.legend([patches[0][0], patches[1][0]], ["Home Team Goals", "Home Team Goals"])

plt.show()