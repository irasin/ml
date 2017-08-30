import matplotlib.pyplot as plt

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]
# add_axes
# below are all percentages
left, bottom, width, height = 0.05, 0.05, 0.85, 0.85
ax1 = fig.add_axes([left, bottom, width, height])  # main axes
ax1.plot(x, y, c='r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

ax2 = fig.add_axes([0.2, 0.6, 0.25, 0.25])  # inside axes
ax2.plot(y, x, c='b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')


# different method with add axes: axes
####################################
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, c='g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()
