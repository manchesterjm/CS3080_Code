import numpy as np
import matplotlib.pyplot as plt

x_pts = np.linspace(0, 2 * np.pi)

for i in range(1, 7) :
    y_pts = np.sin(x_pts * i)
    plt.subplot(7, 1, i)
    plt.plot(x_pts, y_pts)
    
plt.show()