import matplotlib.pyplot as plt
import numpy as np

with open("Goals.txt", "r") as in_f:
    homeTeamGoals = [int(i) for i in in_f.readline().strip().split()]
    awayTeamGoals = [int(i) for i in in_f.readline().strip().split()]

fig1 = plt.figure(figsize=(10, 5))

ax1 = fig1.add_subplot(1, 1, 1)

ax1.boxplot(x=[homeTeamGoals, awayTeamGoals], 
            positions=[1, 8],
            sym="+", 
            whis=2, 
            widths=1,
            notch=True,
            conf_intervals=[None, [0.5,2]]
            )

ax1.set_xlim(-1, 10)
plt.xticks([1, 8], ["Home Team Goals", "Away Team Goals"])

plt.show()
