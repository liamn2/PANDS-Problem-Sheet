# Program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# plottask.py
# Author: Liam Nutley
import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-np.pi,np.pi,100)

# the function, which is y = sin(x) here
y = x

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the functions
plt.plot(x,y, 'b', label='f(x) = x')
plt.plot(x,y**2, 'c', label='g(x) = x**2')
plt.plot(x,y**3, 'r', label='h(x) = x**3')

plt.legend(loc='upper left')

# show the plot
plt.show()