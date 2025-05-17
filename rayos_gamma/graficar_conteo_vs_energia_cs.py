import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the path to the data file
data_file = "rayos_gamma/Cs-137.csv"

# Define the output path for the plot
output_file = "rayos_gamma/plot_cs137.png"

# Define the energy calculation function
def calcular_energia(canal):
    """Calculates energy from channel using the formula."""
    return 1.77 * canal - 19.73

# Read the data from the CSV file
try:
    data = pd.read_csv(data_file, header=None, names=['canal', 'conteo'])
except FileNotFoundError:
    print(f"Error: El archivo '{data_file}' no fue encontrado.")
    exit()
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
    exit()

# Calculate energy for each channel
data['energia'] = data['canal'].apply(calcular_energia)

# Filter data between 500 and 750 energy
filtered_data = data[(data['energia'] >= 550) & (data['energia'] <= 750)]

# Find the maximum count in the filtered data
if not filtered_data.empty:
    max_count = filtered_data['conteo'].max()
    max_energy = filtered_data.loc[filtered_data['conteo'] == max_count, 'energia'].values[0]  # Get corresponding energy
else:
    max_count = 0
    max_energy = 0
    print("No data found within the energy range of 500-750.")

# Create the plot
plt.figure(figsize=(10, 6))  # Adjust figure size as needed

plt.scatter(data['energia'], data['conteo'], label='Conteo vs. Energía', s=5)

# Add vertical line at maximum count energy
if max_count > 0:
    plt.axvline(x=max_energy, color='r', linestyle='--', label=f'Máximo conteo: {max_count:.2f} a {(max_energy):.2f} KeV')

# Add labels and title in Spanish
plt.xlabel('Energía (KeV)')
plt.ylabel('Conteo')
plt.title('Espectro de rayos gamma de Cs-137')

# Add legend
plt.legend()

# Add grid
plt.grid(True)

# Save the plot to a PNG file
try:
    plt.savefig(output_file)
    print(f"Gráfico guardado como '{output_file}'")
except Exception as e:
    print(f"Error al guardar el gráfico: {e}")
