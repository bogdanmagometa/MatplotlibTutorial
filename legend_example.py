#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 00:21:22 2022

@author: bohdan
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, NullLocator
import numpy as np


def dnorm(x, mean=0, sd=1):
    return 1 / np.sqrt(2*np.pi*sd**2) * np.e**(-(x-mean)**2 / 2 / sd**2)
def dexp(x, lambd):
    return lambd * np.e**(-lambd * x)

fig = plt.figure(figsize=(13,7))
ax1 = fig.add_subplot(1, 1, 1)
print()
x = np.arange(0, 5, 0.01)
ax1.plot(x, dnorm(x), label = "standard normal",
         linewidth=4, linestyle="--")
ax1.plot(x, dexp(x, 1.5), label = r"$exponential, \lambda=\frac{3}{2}$",
         linewidth=4, linestyle=":")

ax1.legend(loc="center", fontsize=20)
ax1.text(0.35, 1, "steep", verticalalignment="center", horizontalalignment="center",
         rotation=-70, size=25, alpha=0.5, color="orange")
ax1.text(0.35, 0.45, "flat", verticalalignment="center", horizontalalignment="center",
         rotation=-10, size=25, alpha=0.5, color="blue", weight=1000)

for tick in ax1.get_xmajorticklabels():
    tick.set_font({"size": 15})


for tick in ax1.get_ymajorticklabels():
    tick.set_font({"size": 15})
    tick.set_rotation(45)

print(ax1.spines["right"].get_visible())
plt.grid()
#ax1.spines["right"].set_visible(False)
#ax1.spines["top"].set_visible(False)

plt.show()
