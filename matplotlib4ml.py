import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
y3 = 0.5 * x

plt.figure(figsize=(8, 5))
plt.plot(x, y1)

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, c='r')
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

# annotation
# method 1
plt.annotate(r'$2x+1\ =\ %s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
             fontsize=18, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.3'))
# method 2
plt.text(-3.7, 3, r'$There\ are\ some\ texts.\ \mu\ \sigma_i\ \alpha_n$', fontdict={'size': 14, 'color': 'g'})


plt.figure(num=3, figsize=(8, 5))
l1, = plt.plot(x, y2, color='DarkRed', label='l1')
l2, = plt.plot(x, y1, color='DarkGreen', linewidth=2, linestyle='--', label='l2')
l3, = plt.plot(x, y3, c='b', lw=1.9, alpha=0.5, label='l3')
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am X')
plt.ylabel('I am Y')

# new ticks
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.5, 0, 2, 3],
           [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))  # data, outward, axes
ax.spines['left'].set_position(('data', -0.25))

# legend
plt.legend(handles=[l1, l2, ], labels=['line1', 'line2'], loc='best')  # loc={'best', 'upper right', ...}

plt.show()
