import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

fig1 = plt.figure(figsize=(4, 4), facecolor="orange")
ax1 = fig1.add_subplot(1, 1, 1)

target_img = mpimg.imread("./images/target_img.png")

ax1.plot(range(1000), [i**1.1 for i in range(1000)], linewidth=4)
ax1.imshow(target_img)

plt.show()



