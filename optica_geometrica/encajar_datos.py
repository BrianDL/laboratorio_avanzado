import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Data from the experiment
s_o = np.array([12.5, 12.0, 11.5, 11.0])  # object distances in cm
s_i = np.array([33.5, 38.0, 43.5, 49.0])  # image distances in cm

# Calculate 1/s_o and 1/s_i
x = 1 / s_o
y = 1 / s_i

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Datos Experimentales')
plt.plot(x, slope * x + intercept, color='red', label=f'Encaje lineal (y = {slope:.3f}x + {intercept:.4f})')

plt.xlabel('1/s_o (cm^-1)')
plt.ylabel('1/s_i (cm^-1)')
plt.title('Verificación de la ecuación de lentes delgadas')
plt.legend()
plt.grid(True)

# Add text box with fit results
textstr = f'Pendiente = {slope:.3f} ± {std_err:.3f}\n'
textstr += f'Ordenada al origen = {intercept:.4f} ± {std_err:.4f} cm^-1\n'
textstr += f'R^2 = {r_value**2:.4f}'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=9,
         verticalalignment='top', bbox=props)

# Calculate focal length
f = 1 / abs(intercept)
f_error = std_err / intercept**2

print(f"Distancia focal calculada: {f:.1f} ± {f_error:.1f} cm")

plt.savefig('lens_equation_verification.png', dpi=300, bbox_inches='tight')
plt.show()