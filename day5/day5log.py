import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 1, 100)
y_cos = np.cos(x)
y_sin = np.sin(x)
plt.plot(x, y_cos)
plt.show()
plt.ion()
plt.plot(x, y_cos)
plt.plot(x, y_cos, 'r-x')
plt.plot?
plt.plot(x, y_cos, color='red', linestyle='-', marker='x')
plt.plot(x, y_cos, x, y_sin)
plt.plot(x, y_cos)
plt.plot(x, y_sin)
# use plt.subplots() to make multiple plots.
fig, ax = plt.subplots(2, 1)
ax.plot(x, y_sin)
ax[0].plot(x, y_sin)
ax[1].plot(x, y_cos)
# plt.draw() forces the plot display to update.
plt.draw()
# plot in XKCD style!
with plt.xkcd():
    plt.plot(x, y_sin)
plt.plot(x, y_cos)
%history -f day5log.py
