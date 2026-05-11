import matplotlib.pyplot as plt

x = [0, 1, 2, 0]
y = [0, 2, 0, 0]

plt.plot(x, y)
plt.fill(x, y, alpha=0.3)
plt.show()