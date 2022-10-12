import matplotlib.pyplot as plt

with open("Goals.txt", "r") as in_f:
    homeTeamGoals = [int(i) for i in in_f.readline().strip().split()]
    awayTeamGoals = [int(i) for i in in_f.readline().strip().split()]

fig1 = plt.figure(figsize=(5, 5), facecolor="white")
ax1 = fig1.add_subplot(1, 1, 1)

counts, xedges, yedges, Image = ax1.hist2d(x=homeTeamGoals, y=awayTeamGoals,
                                           bins=[range(8), range(7)])

extent = [xedges[-1], xedges[0], yedges[-1], yedges[0]] # left, right, bottom, top
fig2 = plt.figure(figsize=(10, 10))
ax2 = fig2.add_subplot(1, 1, 1)
im = ax2.imshow(counts, extent=extent)


plt.show()