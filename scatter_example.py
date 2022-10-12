#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 23:03:05 2022

@author: bohdan
"""

import matplotlib.pyplot as plt

with open("Goals.txt", "r") as goalData:
    homeTeamGoals = [int(i) for i in goalData.readline().strip().split()]
    awayTeamGoals = [int(i) for i in goalData.readline().strip().split()]

print(homeTeamGoals)
print(awayTeamGoals)

plt.scatter(x=homeTeamGoals, 
            y=awayTeamGoals,
            s=70,
            c=["red"],
            marker="$gg$",
            alpha=0.5
            )
