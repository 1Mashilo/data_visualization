"""
A script to generate a scatter plot of square numbers.
"""

import matplotlib.pyplot as plt

# Generate data
x = range(0, 1001)
y = [xi**2 for xi in x]

# Create a scatter plot
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(x, y, c=y, cmap='viridis', s=10, label='Square of Value')

# Customize the plot
ax.set_title("Scatter Plot of Square Numbers", fontsize=18, fontweight='bold')
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=10)
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')
ax.grid(True)

# Add legend
ax.legend()

# Show the plot
plt.show()
