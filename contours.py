import matplotlib.pyplot as plt
import numpy as np

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)


def f(x, y):  # the height function
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

# use plt.contourf to fill contours
# X, Y and value for (X, Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)

# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
# add label
plt.clabel(C, inline=True, colors='black')

plt.xticks(())
plt.yticks(())
plt.show()
