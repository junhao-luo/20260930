import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 500)
y = -0.5 * abs(x - 2) + 1

plt.scatter(x, y, s=50, c=x, cmap='hsv')
plt.savefig("ex03.jpg", bbox_inches='tight')
plt.show()