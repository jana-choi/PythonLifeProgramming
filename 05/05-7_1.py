import matplotlib.pyplot as plt

x = [1, 4, 9, 16, 25, 36, 49, 64]

# plt.plot(x, color = "r")
# plt.plot(x, "or")
# plt.show()

y = [i for i in range(1, 9)]
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("matplotlib sample")
plt.show()