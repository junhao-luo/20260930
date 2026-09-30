import matplotlib.pyplot as plt
import numpy as np

x = np.arange(9)
y = x**2

plt.plot(x, y, '--')
plt.scatter(x, y, s=y**0.5 * 20, c=x, cmap='plasma')

plt.title('Square Growth Analysis')
plt.xlabel('Input')
plt.ylabel('Square Value')
plt.axis([0, 8.5, 0, 70])
plt.tick_params(axis='both', labelsize=12)
plt.grid()

plt.savefig("ex07.jpg", bbox_inches='tight')
plt.show()