import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x, m):
    return m * x

# Leer los datos del archivo mediciones.csv
voltaje, corriente = np.loadtxt('cm_electron/mediciones.csv', delimiter=',', unpack=True)

# Calcular el cuadrado de la corriente (x) y su error
corriente_cuadrado = corriente**2
error_corriente = 0.01 * corriente
error_corriente_cuadrado = 2 * corriente * error_corriente # Propagación de errores

# Definir la incertidumbre en el voltaje
error_voltaje = np.ones_like(voltaje)  # error_voltaje has the same shape as voltaje

# Realizar el ajuste lineal
popt, pcov = curve_fit(linear, corriente_cuadrado, voltaje, sigma=error_voltaje, absolute_sigma=True)

# Obtener la pendiente y su error
pendiente = popt[0]
error_pendiente = np.sqrt(pcov[0, 0])

# Imprimir resultados en español
print("Ajuste lineal realizado.")
print(f"Pendiente: {pendiente:.4f} ± {error_pendiente:.4f} V/A^2")

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.errorbar(corriente_cuadrado, voltaje, xerr=error_corriente_cuadrado, yerr=error_voltaje, fmt='o', label='Datos Experimentales')
plt.plot(corriente_cuadrado, linear(corriente_cuadrado, pendiente), 'r-', label=f'Ajuste Lineal: y = {pendiente:.3f}x')

# Etiquetas y título en español
plt.xlabel('Corriente al cuadrado (A^2)')
plt.ylabel('Voltaje (V)')
plt.title('Relación entre Voltaje y Corriente al Cuadrado')
plt.legend()
plt.grid(True)

# Guardar la gráfica en un archivo PNG
plt.savefig('cm_electron/voltaje_vs_corriente_cuadrado.png')

# Mostrar la gráfica (opcional)
# plt.show()