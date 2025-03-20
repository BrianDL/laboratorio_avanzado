import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data from the experiment
theta = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135])
N = np.array([28198732, 5267, 333, 44, 28, 8, 2, 3, 6, 2])

# Define the function to fit
def func(x, k, n):
    return k * np.sin(np.radians(x)/2)**(-n)

# Perform the fit (excluding the first point at 0 degrees)
popt, pcov = curve_fit(func, theta[1:], N[1:], p0=[1e6, 4])

# Extract the optimized parameters
k_fit, n_fit = popt
k_err, n_err = np.sqrt(np.diag(pcov))

# Calculate R-squared
residuals = N[1:] - func(theta[1:], *popt)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((N[1:] - np.mean(N[1:]))**2)
r_squared = 1 - (ss_res / ss_tot)

# Generate points for the fitted curve
theta_fit = np.linspace(1, 135, 1000)
N_fit = func(theta_fit, *popt)

# Create the plot
plt.figure(figsize=(10, 6))
plt.semilogy(theta, N, 'bo', label='Datos experimentales')
plt.semilogy(theta_fit, N_fit, 'r-', label='Ajuste: $k \sin^{-n}(\theta/2)$')
plt.xlabel('Ángulo θ (grados)')
plt.ylabel('Número de partículas (N)')
plt.title('Dispersión de Rutherford: Datos y ajuste')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.2)

# Add text box with fit results
textstr = f'k = {k_fit:.2e} ± {k_err:.2e}\n'
textstr += f'n = {n_fit:.2f} ± {n_err:.2f}\n'
textstr += f'R² = {r_squared:.4f}'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=9,
         verticalalignment='top', bbox=props)

# Save the figure
plt.savefig('rutherford_fit.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"k = {k_fit:.2e} ± {k_err:.2e}")
print(f"n = {n_fit:.2f} ± {n_err:.2f}")
print(f"R² = {r_squared:.4f}")