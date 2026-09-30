import matplotlib.pyplot as plt

square = [0, 1, 4, 9, 16, 25, 36, 49, 64]

plt.plot(square, 'g-.x', lw=3)
plt.title('Test Chart', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square', fontsize=14)

plt.axis([0, 8.5, 0, 65])
plt.xticks(range(9))
plt.yticks(range(0, 61, 10))
plt.tick_params(axis='both', labelsize=12, color='red')
plt.grid()

plt.savefig("ex05.jpg", bbox_inches='tight')
plt.show()