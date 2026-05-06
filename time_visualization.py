import matplotlib.pyplot as plt
import numpy as np

# Configure the Plot Style
plt.style.use('seaborn-v0_8-whitegrid')

# Create a single figure (Adjusted width for a single graph)
fig, ax = plt.subplots(figsize=(8, 6))

# Define the Input Size (n) and Budget Constant (W)
n = np.linspace(1, 50, 400)
W = 50 

# TIME COMPLEXITY MATH
greedy_time = n * np.log2(np.maximum(n, 1.1)) # O(n log n)
dp_time = n * W                               # O(n * W)

# PLOT TIME COMPLEXITY
ax.plot(n, dp_time, label='DP Time: $O(n \\times W)$', color='#e74c3c', linewidth=3)
ax.plot(n, greedy_time, label='Greedy Time: $O(n \\log n)$', color='#3498db', linewidth=3)

ax.fill_between(n, greedy_time, dp_time, color='#e74c3c', alpha=0.1)

# FORMATTING
ax.set_title('Time Complexity', fontsize=14, fontweight='bold', pad=10)
ax.set_xlabel('Number of Startups ($n$)', fontsize=12, fontweight='bold')
ax.set_ylabel('Computational Time (Operations)', fontsize=12, fontweight='bold')
ax.legend(loc='upper left', fontsize=11, frameon=True, shadow=True)
ax.set_xlim(1, 50)
ax.set_ylim(0, max(dp_time))

# Add a master title centered above the graph
plt.suptitle('Computational Time Growth Rate', fontsize=16, fontweight='bold', y=1.02)

plt.tight_layout()

# Save the image
plt.savefig('time_complexity_chart.png', dpi=300, bbox_inches='tight')
plt.show()