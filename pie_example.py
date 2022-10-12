import matplotlib.pyplot as plt
import numpy as np

with open("Goals.txt", "r") as in_f:
    homeTeamGoals = [int(i) for i in in_f.readline().strip().split()]
    awayTeamGoals = [int(i) for i in in_f.readline().strip().split()]

fig1 = plt.figure(figsize=(10, 5))

ax1 = fig1.add_subplot(1, 1, 1)

totalHomeTeamGoals = sum(homeTeamGoals)
totalAwayTeamGoals = sum(awayTeamGoals)

ax1.pie(x=[totalHomeTeamGoals, totalAwayTeamGoals],
        # sum(x) > 1 - normalized internally
        # sum(x) <= 1 - no normalization is performed
        labels=["Home Team Goals", "Away Team Goals"],
        labeldistance=1.05,
        colors=["red", "black"],
        explode=[0, 0.1],
        radius=1.4,
        center=[0,0],
        shadow=True
        )

plt.show()
