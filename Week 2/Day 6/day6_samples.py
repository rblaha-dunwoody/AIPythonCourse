import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Basic plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
#plt.plot(x, y, label="Trend", color="orange", linestyle="--", marker="o")
#plt.legend()
#plt.show()

# Line plot
#plt.plot([1, 2, 3], [10, 20, 30], label="Trend")
#plt.title("Line Plot")
#plt.xlabel("X-axis")
#plt.ylabel("Y-axis")
#plt.legend()
#plt.show()

# Bar chart
categories = ["A", "B", "C"]
values = [10, 15, 7]
#plt.bar(categories, values, color="blue")
#plt.title("Bar Chart")
#plt.show()

# Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
#plt.hist(data, bins=4, color="green", edgecolor="black")
#plt.title("Histogram")
#plt.show()

# Scatterplot
x = [1, 2, 3, 4, 5]
y = [10, 12, 25, 30, 45]
#plt.scatter(x, y, color="red")
#plt.title("Scatter Plot")
#plt.show()

data = np.random.rand(5, 5)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("HeatMap")
plt.show()
