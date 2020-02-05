import matplotlib.pyplot as plt 

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues)

# Set the chart title and axis titles
ax.set_title("Colored cubes", fontsize=24)
ax.set_xlabel("x value", fontsize=14)
ax.set_ylabel("cubic value", fontsize=14)

# Set the size of the ticks
ax.tick_params(axis='both', labelsize=14)

ax.axis([1, 5500, 1, 2_500_000_000_00])

plt.show()