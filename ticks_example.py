#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 20:50:37 2022

@author: bohdan
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter, NullFormatter
import numpy as np

def phi(x):
    return 1 / np.sqrt(2*np.pi) * np.e**(-x**2 / 2)

fig = plt.figure(figsize=(9, 6))
ax1 = fig.add_subplot(1, 1, 1)

ax1.plot(np.arange(-4, 4, 0.01), phi(np.arange(-4, 4, 0.01)), color="black", 
         linewidth=4)
ax1.grid()
ax1.set_xlim(-5, 5)
ax1.set_ylim(0, 0.5)
ax1.set_title(label="p.d.f. of normal distribution", pad=10, 
              fontdict={"fontsize": 20})

# locator
ax1.xaxis.set_major_locator(MultipleLocator(3))
ax1.xaxis.set_minor_locator(MultipleLocator(1))

# formatter
ax1.xaxis.set_major_formatter(NullFormatter())
ax1.xaxis.set_minor_formatter(FormatStrFormatter(r"$\frac{%d}{pi}$"))

# other
xTickLabels = [int(i) for i in ax1.get_xticks().tolist()]
print(len(ax1.get_ymajorticklabels()[1].get_text()))

plt.show()
