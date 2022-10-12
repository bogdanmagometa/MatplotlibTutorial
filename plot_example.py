#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 02:38:22 2022

@author: bohdan
"""

import matplotlib.pyplot as plt

with open("Goals.txt", "r") as goalData:
    homeTeamGoals = [int(i) for i in goalData.readline().strip().split()]
    awayTeamGoals = [int(i) for i in goalData.readline().strip().split()]

print(homeTeamGoals)
print(awayTeamGoals)

fig1 = plt.figure(figsize=(12, 12), facecolor = "magenta")
ax2 = fig1.add_subplot(2, 1, 1)
ax1 = fig1.add_subplot(2, 1, 2)


ax1.set_title(label="Away team goals", loc="left", 
              fontdict={"fontsize": 30, "color": "blue", "rotation":-10}, pad=20, )
ax1.set_xlabel(xlabel="Number of game", labelpad=20, fontdict={"fontsize": 20}, loc="left")
ax1.set_xlim(left=0, right=140)
ax1.set_ylim(bottom=0, top=6.1)
ax1.plot(range(len(awayTeamGoals)), awayTeamGoals, c=[0, 0, 0], 
         marker=">", markerfacecolor="magenta", markersize=10, 
         linestyle="--", linewidth=2)

plt.show()
