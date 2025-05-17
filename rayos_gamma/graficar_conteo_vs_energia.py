#!/usr/bin/env python


import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_energy_vs_count(csv_file, output_dir="rayos_gamma"):
    """
    Lee datos de canal y conteo desde un archivo CSV, convierte los canales a energía usando la fórmula E = 1.77c - 19.73,
    grafica la energía contra el conteo y guarda la gráfica en un archivo PNG.

    Args:
        csv_file (str): Ruta al archivo CSV que contiene los datos. El archivo debe no tener encabezado y las columnas en el orden: canal, conteo.
        output_dir (str, optional): Directorio para guardar la gráfica. Por defecto es "rayos_gamma".
    """
    try:
        # 1. Carga de Datos
        data = pd.read_csv(csv_file, header=None)
        canal = data.iloc[:, 0].to_numpy()
        conteo = data.iloc[:, 1].to_numpy()

        # 2. Conversión de Canal a Energía
        energia = 1.77 * canal - 19.73

        # 3. Graficación
        plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura
        plt.scatter(energia, conteo, label="Datos", marker='o', s=5) # Graficar los puntos de datos
        plt.yscale('log')

        plt.xlabel("Energía (keV)")  # Etiqueta del eje x en español
        plt.ylabel("Conteo")  # Etiqueta del eje y en español
        plt.title("Energía vs. Conteo")  # Título de la gráfica en español
        plt.legend()  # Mostrar la leyenda
        plt.grid(True)  # Agregar una grilla

        # 4. Guardar la Gráfica
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)  # Crear el directorio de salida si no existe

        output_path = os.path.join(output_dir, "energia_vs_conteo.png")  # Ruta de salida en español
        plt.savefig(output_path)  # Guardar la gráfica
        plt.close()  # Cerrar la figura para liberar memoria

    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {csv_file}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def get_arg(argname: str) -> str | None:
    """
    Retrieves the value of a command-line argument.

    Args:
        argname: The name of the argument (without the leading '--').

    Returns:
        The value of the argument if found, otherwise None.
    """
    try:
        index = sys.argv.index(f"--{argname}")
        return sys.argv[index + 1]
    except (ValueError, IndexError):
        return None


if __name__ == "__main__":
    
    csv_file = "rayos_gamma/Eu-152.csv" \
        if (fname:= get_arg('file')) is None else fname 

    print("file:", csv_file)    
    plot_energy_vs_count(csv_file)