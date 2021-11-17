import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

airResistance = 0.1
g = 9.8
length = 1

def acceleration(w, p):
    return -w * airResistance - g/length*np.sin(p)


p, w = np.meshgrid(np.linspace(-10, 10, 20), np.linspace(-10, 10, 20))

f,ax=plt.subplots(1)

ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%g $\pi$'))
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=1.0))
ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%g $\pi$'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base=1.0))


plt.quiver(p/np.pi, w/np.pi, w/np.pi, acceleration(w, p)/np.pi)
plt.show()


