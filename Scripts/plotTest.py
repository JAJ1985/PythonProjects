import matplotlib.pyplot as plt

numbers = [2, 4, 1, 6]

fig, ax = plt.subplots(figsize=(4, 2.25))

ax.plot(numbers, marker="o")
ax.plot([number * 5 for number in numbers], marker="x")
ax.plot([number * 7 for number in numbers], marker="<")
ax.set_ylabel("Random Numbers")
plt.show()
