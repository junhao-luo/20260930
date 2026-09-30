import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 400)
y = np.sin(2 * x) + 0.5 * np.cos(5 * x)

plt.fill_between(x, 0, y, alpha=0.25)
plt.plot(x, y)
plt.scatter(x, y, s=35, c=y, cmap='viridis')

plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.savefig("ex06.jpg", bbox_inches='tight')
plt.show()