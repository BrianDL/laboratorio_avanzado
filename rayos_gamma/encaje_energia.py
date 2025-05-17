import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_gamma_ray_data(csv_file, output_dir="rayos_gamma"):
    """
    Lee datos de energía vs. canal desde un archivo CSV, grafica los datos,
    realiza un ajuste lineal, grafica el ajuste y guarda la gráfica en un archivo PNG.

    Args:
        csv_file (str): Ruta al archivo CSV que contiene los datos.
                          El archivo debe no tener encabezado y las columnas en el orden: canal, energia, cuenta.
        output_dir (str, optional): Directorio para guardar la gráfica. Por defecto es "rayos_gamma".
    """

    try:
        # 1. Carga y Preparación de Datos
        data = pd.read_csv(csv_file, header=None)  # Leer sin encabezado
        canal = data.iloc[:, 0].to_numpy()         # Valores de canal (eje x)
        energia = data.iloc[:, 1].to_numpy()       # Valores de energía (eje y)

        # 2. Ajuste Lineal
        # Realizar una regresión lineal usando la función np.polyfit.
        # polyfit devuelve los coeficientes en potencias descendentes, así que m es el primer elemento y b es el segundo.
        m, b = np.polyfit(canal, energia, 1)

        # Crear la línea ajustada
        fitted_line = m * canal + b

        # 3. Graficación
        plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura para una mejor visualización
        plt.scatter(canal, energia, label="Datos", marker='o', s=20) # Graficar los puntos de datos originales
        plt.plot(canal, fitted_line, color='red', label=f"Ajuste: y = {m:.2f}x + {b:.2f}")  # Graficar la línea de ajuste

        plt.xlabel("Canal")
        plt.ylabel("Energía")
        plt.title("Energía vs. Canal")
        plt.legend()
        plt.grid(True)

        # 4. Guardar la Gráfica
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)  # Crear el directorio de salida si no existe

        output_path = os.path.join(output_dir, "energy_vs_canal.png")
        plt.savefig(output_path)
        plt.close()  # Cerrar la figura para liberar memoria

        # 5. Imprimir los parámetros del ajuste
        print("Parámetros del ajuste lineal:")
        print(f"  m (pendiente) = {m:.2f}")
        print(f"  b (ordenada al origen) = {b:.2f}")

    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {csv_file}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    csv_file = "rayos_gamma/local_maxima_energies.csv"  # Especificar la ruta de su archivo CSV
    analyze_gamma_ray_data(csv_file)