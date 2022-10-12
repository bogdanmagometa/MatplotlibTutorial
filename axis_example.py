#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 02:12:40 2022

@author: bohdan
"""

import matplotlib.pyplot as plt

with open("Goals.txt", "r") as goalData:
    homeTeamGoals = [int(i) for i in goalData.readline().strip().split()]
    awayTeamGoals = [int(i) for i in goalData.readline().strip().split()]

print(homeTeamGoals)
print(awayTeamGoals)

fig1 = plt.figure("First", figsize=(7, 5), facecolor="orange")
fig2 = plt.figure("Second", figsize=(12, 5), facecolor="blue")

plt.figure("Second")

ax1 = fig1.add_subplot(3, 3, 1)
ax2 = fig1.add_subplot(3, 3, 3)
plt.sca(ax1)
plt.scatter(x=homeTeamGoals, 
            y=awayTeamGoals,
            s=500,
            c="red",
            marker="$gg$",
            alpha=0.5
            )

plt.sca(ax2)
plt.scatter(x=awayTeamGoals,
            y=homeTeamGoals,
            s=100,
            c="brown")

fig1.show()