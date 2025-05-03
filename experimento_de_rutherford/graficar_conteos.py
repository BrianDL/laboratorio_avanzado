import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from CSV
try:
    df = pd.read_csv("experimento_de_rutherford/data.csv")
except FileNotFoundError:
    print("Error: data.csv not found.  Make sure the file exists in the same directory as the script.")
    exit()
except Exception as e:
    print(f"Error reading data.csv: {e}")
    exit()


# Set up the plot
plt.figure(figsize=(10, 6))  # Adjust figure size for better readability
plt.errorbar(
    df["angle"],
    df["avg"],
    yerr=df["stdev"],
    fmt="o-",  # 'o-' means circles connected by lines
    capsize=5,  # Add caps to error bars
    label="Promedio ± Desviación Estándar",
)

# Set logarithmic scale for y-axis (avg and stdev)
plt.yscale("log")

# Add labels and title in Spanish
plt.xlabel("Theta (grados)", fontsize=12)
plt.ylabel("Conteo promedio (log N)", fontsize=12)  
plt.title("Variación del Conteo en Función del Ángulo", fontsize=14)

# Add legend
plt.legend(loc="upper right", fontsize=10)

# Improve appearance (optional)
plt.grid(True, linestyle='--', alpha=0.5)  # Add a grid for better readability

# Add Spanish annotations for the axes
plt.xticks(df["angle"]) # ensures that all the angle values are shown

# Save the plot to a file
plt.savefig("experimento_de_rutherford/data.png")  # Save the figure

# Optionally, show the plot as well
# plt.tight_layout()  # Adjust layout to prevent labels from overlapping
# plt.show()