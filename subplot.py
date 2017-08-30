import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# subplot
plt.figure()
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(222)
plt.plot([0, 1], [0, 2])

plt.subplot(223)
plt.plot([-1, 1], [1, 2])

plt.subplot(224)
plt.plot([0, 2], [0, 4])


plt.figure()
plt.subplot(211)
plt.plot([0, 1], [0, 2])

plt.subplot(234)
plt.plot([0, 1], [0, 2])

plt.subplot(235)
plt.plot([0, 1], [0, 2])

plt.subplot(236)
plt.plot([0, 1], [0, 2])

# method 1: subplot2grid
plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax1')
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

# method 2: gridspec
plt.figure()
gs = gridspec.GridSpec(3, 3)
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[2, 0])
ax10 = plt.subplot(gs[2, 1])


# method 3: easy to define structure
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex='row', sharey='all')
ax11.scatter([1, 1], [2, 2])
plt.show()
