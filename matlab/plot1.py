import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np


fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

x=np.arange(0.0, 2*np.pi, 0.1)
y1=np.sin(x)
y2=np.cos(x)

ax1.plot(x,y1, 'b--')
ax2.plot(x,y2, 'r--')

ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')

plt.show()

