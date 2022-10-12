import matplotlib.pyplot as plt
import numpy as np

with open("Goals.txt", "r") as in_f:
    homeTeamGoals = [int(i) for i in in_f.readline().strip().split()]
    awayTeamGoals = [int(i) for i in in_f.readline().strip().split()]

fig1 = plt.figure(figsize=(10, 5))

ax1 = fig1.add_subplot(1, 1, 1)

avgGoalsScoredHome = sum(homeTeamGoals) / len(homeTeamGoals)
avgGoalsScoredAway = sum(awayTeamGoals) / len(awayTeamGoals)

ax1.bar(x=[1, 2],
        height=[avgGoalsScoredHome, avgGoalsScoredAway],
        width=0.5,
        align="center",
        color=["red", "black"],
        bottom=[0.1, 0.4],
        xerr=[0.5, .5],
        yerr=[[0.2, 0.3], [0.3, 0.2]],
        ecolor=["blue", "green"])
ax1.set_xlim(0, 3)
ax1.set_ylim(0, 3)

plt.xticks([1, 2], ["Home Team Goald", "Away Team Goald"])

plt.show()
