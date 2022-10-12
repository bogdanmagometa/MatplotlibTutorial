#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 02:23:55 2022

@author: bohdan
"""

import numpy as np
import matplotlib.pyplot as plt

print(plt.style.available)

plt.style.use("classic")

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(1, 1, 1)

x = np.arange(0, 10, 0.01)
ax1.plot(x, np.tan(x), label="y=tan(x)")

ax1.set_ylim(-10, 10)
ax1.legend(loc="upper right", fontsize=20)

plt.show()

