import matplotlib.pyplot as plt
import numpy as np

# Configure the Plot Style
plt.style.use('seaborn-v0_8-whitegrid')

# Create a single figure (Adjusted width for a single graph)
fig, ax = plt.subplots(figsize=(8, 6))

# Define the Input Size (n) and Budget Constant (W)
n = np.linspace(1, 50, 400)
W = 50 

# SPACE COMPLEXITY MATH
greedy_space = n                              # O(n) auxiliary space
dp_space = n * W                              # O(n * W) cache space

# PLOT SPACE COMPLEXITY
ax.plot(n, dp_space, label='DP Space: $O(n \\times W)$', color='#e74c3c', linewidth=3)
ax.plot(n, greedy_space, label='Greedy Space: $O(n)$', color='#3498db', linewidth=3)

ax.fill_between(n, greedy_space, dp_space, color='#e74c3c', alpha=0.1)

# FORMATTING
ax.set_title('Space Complexity (Memory)', fontsize=14, fontweight='bold', pad=10)
ax.set_xlabel('Number of Startups ($n$)', fontsize=12, fontweight='bold')
ax.set_ylabel('Memory Usage (Stored States)', fontsize=12, fontweight='bold')
ax.legend(loc='upper left', fontsize=11, frameon=True, shadow=True)
ax.set_xlim(1, 50)
ax.set_ylim(0, max(dp_space))

# Add a master title centered above the graph
plt.suptitle('Memory Overhead and Cache Scaling', fontsize=16, fontweight='bold', y=1.02)

plt.tight_layout()

# Save the image
plt.savefig('space_complexity_chart.png', dpi=300, bbox_inches='tight')
plt.show()