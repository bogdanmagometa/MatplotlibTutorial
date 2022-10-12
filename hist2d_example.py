import matplotlib.pyplot as plt
import numpy as np

with open("Goals.txt", "r") as in_f:
    homeTeamGoals = [int(i) for i in in_f.readline().strip().split()]
    awayTeamGoals = [int(i) for i in in_f.readline().strip().split()]

fig1 = plt.figure(figsize=(6, 4.5))

ax1 = fig1.add_subplot(1, 1, 1)

plt.hist2d(x=homeTeamGoals, y=awayTeamGoals,
           bins=[range(8), range(7)])

plt.colorbar()

plt.show()
