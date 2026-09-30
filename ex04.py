import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(3 * x)

plt.plot(x, y)
plt.fill_between(x, -1, y, color='yellow', alpha=0.3)
plt.savefig("ex04.jpg", bbox_inches='tight')
plt.show()