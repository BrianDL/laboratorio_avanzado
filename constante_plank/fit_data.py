import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define linear function for fitting
def linear(x, m, b):
    return m * x + b

# Function to read data from file
def read_data(filename):
    return np.loadtxt(filename, usecols=(0, 2))

# Function to perform fit and plot
def fit_and_plot(ax, data, color, title):
    x, y = data[:, 0], data[:, 1]

    if title == 'Uv':
        n_right = 6
        n_left = 3
    elif title == 'Amarillo':
        n_right = 2
        n_left = 3
    elif title == 'Verde':
        n_right = 3
        n_left = 3
    else:
        n_right = 4
        n_left = 3

    print(color, n_left, n_right)

    # Fit for positive x
    popt_pos, _ = curve_fit(linear, x[:n_right], y[:n_right])

    # Fit for negative x
    popt_neg, _ = curve_fit(linear, x[-n_left:], y[-n_left:])

    # Find intersection
    intersection_x = (popt_neg[1] - popt_pos[1]) / (popt_pos[0] - popt_neg[0])
    intersection_y = linear(intersection_x, *popt_pos)

    # Plot
    ax.plot(x, y, 'o', color=color, label='Data')
    ax.plot(x, linear(x, *popt_pos), 'r-', label='Positive fit')
    ax.plot(x, linear(x, *popt_neg), 'gray', label='Negative fit')
    ax.set_title(title)
    ax.set_xlabel('Voltage (V)')
    ax.set_ylabel('Current (nA)')
    ax.legend()

    # Adjust limits to data only
    total_x = max(x) - min(x)
    toatl_y = max(y) - min(y)

    ax.set_xlim(min(x) - total_x*0.05, max(x) + total_x*0.05)
    ax.set_ylim(min(y) - toatl_y*0.05, max(y) + toatl_y*0.05)
    
    return intersection_x, intersection_y

# Main script
colors = ['amarillo', 'verde', 'azul', 'violeta', 'uv']
plot_colors = ['orange', 'green', 'blue', 'violet', 'purple']
frequencies = [519, 549, 688, 741, 822]

fig, axs = plt.subplots(3, 2, figsize=(15, 20))
fig.suptitle("Curvas de frenado para diferentes colores")

intersections = []

for i, (color, plot_color, freq) in enumerate(zip(colors, plot_colors, frequencies)):
    # if i == len(colors) -1: break

    data = read_data(f"{color}.dat")
    ax = axs[i // 2, i % 2]
    int_x, int_y = fit_and_plot(ax, data, plot_color, color.capitalize())
    intersections.append((freq, int_x))
    print(f"{color.capitalize()} intersection point: ({int_x:.6e}, {int_y:.6e})")

# Remove the empty subplot
fig.delaxes(axs[2, 1])

plt.tight_layout()
plt.savefig('planck_constant_fits.png')

# Print table of colors, frequencies, and y=0 intersects
print("\nColor\t\tFrequency (Hz)\tIntersection with y=0 (V)")
print("--------------------------------------------------------")
for color, (freq, int_x) in zip(colors, intersections):
    print(f"{color}\t\t{freq:.2e}\t{abs(int_x):.4f}")

# Write data to freq_and_vf.dat
with open("freq_and_vf.dat", "w") as f:
    f.write("# Frequency (Hz)\tIntersection with y=0 (V)\n")
    for freq, int_x in intersections:
        f.write(f"{freq:.2f}\t{abs(int_x):.4f}\n")


# Plot frequency vs. intersection voltage
freq_array = np.array([freq for freq, _ in intersections])
voltage_array = np.array([(int_x) for _, int_x in intersections])

# Perform linear fit
def linear_fit(x, m, b):
    return m * x + b

popt, pcov = curve_fit(linear_fit, freq_array, voltage_array)
m, b = popt
m_err, b_err = np.sqrt(np.diag(pcov))

# Calculate Planck's constant
e = 1.602176634e-19  # elementary charge in Coulombs
h = e * 1e-12 * m  # convert THz to Hz
h_err = m_err * e * 1e-12

# Calculate work function
work_function = abs(b)
work_function_err = b_err
plt.figure(figsize=(10, 6))
plt.plot(freq_array, voltage_array, 'o', label='Data')
plt.plot(freq_array, linear_fit(freq_array, m, b), 'r-', label='Linear Fit')
plt.xlabel('Frequency (THz)')
plt.ylabel('Intersection Voltage (V)')
plt.title('Frequency vs. Intersection Voltage')
plt.grid(True)
plt.legend()

# Add text box with fit results
plt.text(0.05, 0.95, f'Slope = {m:.4e} ± {m_err:.4e} V/THz\n'
                     f'Intercept = {b:.4f} ± {b_err:.4f} V\n'
                     f"Planck's constant = {h:.4e} ± {h_err:.4e} J·s\n"
                     f'Work function = {work_function:.4f} ± {work_function_err:.4f} eV',
         transform=plt.gca().transAxes, verticalalignment='top', 
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.savefig('freq_vs_voltage_fit.png')

# Print results to console
print(f"Slope = {m:.4e} ± {m_err:.4e} V/THz")
print(f"Intercept = {b:.4f} ± {b_err:.4f} V")
print(f"Planck's constant = {h:.4e} ± {h_err:.4e} J·s")
print(f"Work function = {work_function:.4f} ± {work_function_err:.4f} eV")