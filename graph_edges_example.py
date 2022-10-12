#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 02:03:51 2022

@author: bohdan
"""

import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize = (10, 6))
ax1 = fig.add_subplot(1, 1, 1)

x = np.arange(0, 5, 0.01)

ax1.plot(x, x, linewidth=3)
ax1.plot(x, x**2, linewidth=3)
ax1.plot(x, np.e**x, linewidth=3)

ax1.yaxis.set_ticks_position("right")
ax1.spines["top"].set_visible(False)



