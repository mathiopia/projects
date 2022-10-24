import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma,zeta
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
x=np.linspace(-4,3,100)
y=np.linspace(-3,3,100)
x,y=np.meshgrid(x,y)
z=(gamma(x+1j*y))
surf=ax.plot_surface(x,y,z)
plt.show()
