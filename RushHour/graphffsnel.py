import matplotlib.pyplot as plt
import numpy as np

# Data
algorithms = ['RandomMove', 'LegalMove', 'RepeatMove']
moves = [13228.7527, 13154.1084, 2865.1301]
loops = [73826.2884, 13154.1084, 2865.1301]

# Set up bar width and positions
barWidth = 0.3
r1 = np.arange(len(moves))
r2 = [x + barWidth for x in r1]

# Creating the bar chart with increased size
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the size as needed

# Plotting
ax.bar(r1, loops, color='r', width=barWidth, label='Game Loops')
ax.bar(r2, moves, color='b', width=barWidth, label='Moves')

# Adding labels and titles
ax.set_xlabel('Algorithm', fontweight='bold')
ax.set_ylabel('Counts', fontweight='bold')
ax.set_xticks([r + barWidth/2 for r in range(len(moves))], algorithms)
plt.title('Comparison of Moves and Game Loops per Algorithm')

# Setting up the legend outside the plot
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to fit everything
plt.tight_layout()

# Save the plot as a PNG file, adjusting the bounding box to include the legend
plt.savefig('Algorithm_tests/barding.png', bbox_inches='tight')  # Replace with your desired path

plt.close(fig)  # Close the figure to free up memory
