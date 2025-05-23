import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x, m, b):
    return m * x + b

# Datos del experimento
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