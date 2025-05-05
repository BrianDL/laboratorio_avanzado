import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Load data from CSV
try:
    df = pd.read_csv("experimento_de_rutherford/data.csv")
except FileNotFoundError:
    print("Error: data.csv not found.  Make sure the file exists in the same directory as the script.")
    exit()
except Exception as e:
    print(f"Error reading data.csv: {e}")
    exit()

# Filter data to restrict the angle range to 0-180 degrees (and skip the first row to avoid zero angle)
df = df[df["angle"] >= 15]


# Define the fitting function
def fit_function(theta, k, n):
    return k * (np.sin( (theta * np.pi) / 360.0 ))**n

# Prepare data for fitting
theta = df["angle"]
I = df["avg"]
stdev = df["stdev"]  # Use stdev for uncertainties

# Perform the curve fit
try:
    popt, pcov = curve_fit(
        fit_function, theta, I
        , p0=[5292, 1.0] , sigma=stdev
        , absolute_sigma=True
        )
    k_fit, n_fit = popt
    perr = np.sqrt(np.diag(pcov))  # Calculate standard errors
    k_err, n_err = perr
    print(f"k = {k_fit:.2f} ± {k_err:.2f}")
    print(f"n = {n_fit:.2f} ± {n_err:.2f}")

except RuntimeError:
    print("Error: Optimization failed.  The fit may not have converged.  Try adjusting initial guess (p0).")
    exit()
except Exception as e:
    print(f"Error during curve fitting: {e}")
    exit()

# Generate points for the fitted curve
theta_fit = np.linspace(min(theta), max(theta), 100)
I_fit = fit_function(theta_fit, k_fit, n_fit)

# Create the plot
plt.figure(figsize=(10, 6))
plt.errorbar(theta, I, yerr=stdev, fmt="o", label="Datos Experimentales", capsize=5)
plt.plot(theta_fit, I_fit, "r-", label=f"Ajuste: I = k * (sin(θ/2))^n\nk = {k_fit:.2f}, n = {n_fit:.2f}")

# Add labels and title in Spanish
plt.xlabel("Ángulo (grados)", fontsize=12)
plt.ylabel("Conteo (Promedio)", fontsize=12)
plt.title("Ajuste de la Ley de Rutherford", fontsize=14)

# Add legend
plt.legend(loc="upper right", fontsize=10)

# Add grid
plt.grid(True, linestyle='--', alpha=0.5)

# Set logarithmic scale for the y-axis
plt.yscale("log")  # This is the key change

# Save the plot to a file
import os
if not os.path.exists("experimento_de_rutherford"):
    os.makedirs("experimento_de_rutherford")
plt.savefig("experimento_de_rutherford/data_fit.png")

### don't show the plot