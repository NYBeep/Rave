import matplotlib.pyplot as plt
import numpy as np


plt.style.use('_mpl-gallery')


# make data
np.random.seed(1)
x = 4 + np.random.normal(0, 1, 200)

# plot:
fig, ax = plt.subplots()

ax.hist(x, bins=20, linewidth=0.5, edgecolor="black", color= "pink")

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 56), yticks=np.linspace(0, 56, 9))

plt.show()