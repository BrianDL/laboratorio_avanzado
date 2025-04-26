import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x, m, b):
    return m * x + b

# Datos del experimento
# corriente = np.array([0.00, 0.30, 0.60, 0.90, 1.20, 1.51, 1.80, 2.10, 2.40, 2.70, 3.00])  # Corriente en A
# campo_magnetico = np.array([-0.042, 0.156, 0.367, 0.585, 0.794, 1.012, 1.218, 1.436, 1.653, 1.874, 2.083])  # Campo magnético en mT
# error_campo_magnetico = np.array([0.004, 0.002, 0.003, 0.002, 0.003, 0.003, 0.003, 0.003, 0.003, 0.002, 0.002]) #Error del campo magnetico en mT

### get these three variables from a file named campo_magnetico.csv
corriente, campo_magnetico, error_campo_magnetico = \
    np.loadtxt('cm_electron/campo_magnetico.csv'
    , delimiter=',', unpack=True)

campo_magnetico = 1000*campo_magnetico # convertir a mT

# Ajuste lineal
popt, pcov = curve_fit(linear, corriente, campo_magnetico, sigma=error_campo_magnetico)
pendiente, intercepto = popt
error_pendiente = np.sqrt(pcov[0, 0])
error_intercepto = np.sqrt(pcov[1, 1])

# Imprimir resultados en español
print("Ajuste lineal realizado.")
print(f"Pendiente: {pendiente:.4f} ± {error_pendiente:.4f} mT/A")
print(f"Intercepto: {intercepto:.4f} ± {error_intercepto:.4f} mT")

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.errorbar(corriente, campo_magnetico, xerr=0, yerr=error_campo_magnetico, fmt='o', label='Datos Experimentales')
plt.plot(corriente, linear(corriente, pendiente, intercepto), 'r-', label=f'Ajuste Lineal: y = {pendiente:.3f}x + {intercepto:.3f}')

# Etiquetas y título en español
plt.xlabel('Corriente (A)')
plt.ylabel('Campo Magnético (mT)')
plt.title('Relación entre Corriente y Campo Magnético')
plt.legend()
plt.grid(True)

### guardar a un archivo
plt.savefig('cm_electron/campo_magnetico_vs_corriente.png')

# Mostrar la gráfica
# plt.show()