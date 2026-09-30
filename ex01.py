import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 500)
y = -0.5 * abs(x - 2) + 1

plt.scatter(x, y, s=x**2 + 1, color=(0, 1, 0))
plt.savefig("ex01.jpg", bbox_inches='tight')
plt.show()