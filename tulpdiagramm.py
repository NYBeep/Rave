import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x= ['a', 'b', 'c', 'd']
numbricounts = [40, 100, 30, 55]
bar_labels = ['a', 'b', 'c', 'd']
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

ax.bar(x, numbricounts, label=bar_labels, color=bar_colors)

ax.set_ylabel('nimetus')
ax.set_title('Pealkiri')
plt.show()