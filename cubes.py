import matplotlib.pyplot as plt

# Generate data for the first five cubic numbers
x_values_5 = list(range(1, 6))
y_values_5 = [x**3 for x in x_values_5]

# Generate data for the first 5,000 cubic numbers
x_values_5000 = list(range(1, 5001))
y_values_5000 = [x**3 for x in x_values_5000]

# Create a figure with two subplots (one for each plot)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot the first five cubic numbers
ax1.plot(x_values_5, y_values_5, marker='o', markersize=8)
ax1.set_title("First Five Cubic Numbers")
ax1.set_xlabel("Number")
ax1.set_ylabel("Cubic Value")

# Plot the first 5,000 cubic numbers with a colormap
cmap = plt.get_cmap("viridis")
ax2.scatter(x_values_5000, y_values_5000, c=x_values_5000, cmap=cmap, s=10)
ax2.set_title("First 5,000 Cubic Numbers (Colored)")
ax2.set_xlabel("Number")
ax2.set_ylabel("Cubic Value")


# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()
