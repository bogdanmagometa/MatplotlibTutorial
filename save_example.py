#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 02:45:04 2022

@author: bohdan
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(1, 1, 1)

x = np.arange(0, 100, 0.01)

ax1.plot(x, np.log2(x))

ax1.set_xlim(-1, 100)
ax1.set_ylim(-1, 8)

plt.savefig("images/save_example.pdf", dpi=100, orientation="portrait")
plt.show()
