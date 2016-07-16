from time import *
import matplotlib.pyplot as plt
import numpy as np
import math as ma



def f(x, t):
    return (np.exp(-(x-3*t)**2))*np.sin(3*np.pi*(x-t))





t_start = -1
t_stop = 1
t_values = np.linspace(t_start, t_stop, 60)
x = np.linspace(-6,6,1201)




max_f = f(x, t_stop)


counter = 0
for t in t_values:
    y = f(x, t)
    plt.plot(x, y, axis=[x[0], x[-1], -0.1, max_f],
         xlabel='x', ylabel='f', legend='s=%4.2f' % 5,
         hardcopy='tmp%04d.png' % counter)
    counter += 1



movie('tmp*.png')
