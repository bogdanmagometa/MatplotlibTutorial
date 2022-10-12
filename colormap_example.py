import matplotlib.pyplot as plt

with open("Goals.txt", "r") as in_f:
    homeTeamGoals = [int(i) for i in in_f.readline().strip().split()]
    awayTeamGoals = [int(i) for i in in_f.readline().strip().split()]

fig1 = plt.figure(figsize=(5, 5), facecolor="white")
ax1 = fig1.add_subplot(1, 1, 1)

ax1.hist2d(x=homeTeamGoals, y=awayTeamGoals,
           bins=[range(8), range(7)], cmap=plt.cm.viridis)

fig2 = plt.figure(figsize=(5, 5), facecolor="white")
ax2 = fig2.add_subplot(1, 1, 1)

N, bins, patches = ax2.hist(x=homeTeamGoals, bins=range(8))

cmap = plt.cm.get_cmap("viridis", 7)
colors = cmap(range(7))

for color, patch in zip(colors, patches):
    patch.set_facecolor(color)

plt.show()
