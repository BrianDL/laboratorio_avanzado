import matplotlib.pyplot as plt
import numpy as np

# Data from the experiment
theta = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135])
N = np.array([28198732, 5267, 333, 44, 28, 8, 2, 3, 6, 2])

# Create the plot
plt.figure(figsize=(10, 6))
plt.semilogy(theta, N, 'bo-')  # Use semilogy for logarithmic y-axis
plt.xlabel('Ángulo θ (grados)')
plt.ylabel('Número de partículas (N)')
plt.title('Dispersión de Rutherford: Partículas detectadas vs Ángulo')
plt.grid(True, which="both", ls="-", alpha=0.2)

# Add some padding to the y-axis
plt.ylim(1, plt.ylim()[1]*2)

# Save the figure
plt.savefig('rutherford_dispersion.png', dpi=300, bbox_inches='tight')
plt.close()