import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open("Goals.txt", "r") as in_f:
    homeTeamGoals = [int(i) for i in in_f.readline().strip().split()]
    awayTeamGoals = [int(i) for i in in_f.readline().strip().split()]

fig1 = plt.figure(figsize=(10, 10), facecolor="white")
ax1 = fig1.add_subplot(1, 2, 1, projection="3d")
ax2 = fig1.add_subplot(1, 2, 2, projection="3d")

x = range(1, 1 + len(awayTeamGoals))

ax1.plot(xs=x, ys=homeTeamGoals, zs=awayTeamGoals)
ax1.set_xlabel("Number of game", labelpad=10)
ax1.set_ylabel("Home team", labelpad=5)
ax1.set_zlabel("Away team", labelpad=5)


ax2.scatter(xs=x, ys=homeTeamGoals, zs=awayTeamGoals, depthshade=True,
            color="red", marker="^")

for i in range(0, 360):
    ax2.view_init(30, i)
    plt.draw()
    plt.pause(0.01)

plt.show()
