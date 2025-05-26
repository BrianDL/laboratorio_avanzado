import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats as stats

def plot_decay_time_histogram(csv_file, output_png, initial_guess=(300, 2.2, 1)):
    """
    Plots a histogram of decay times from a CSV file, fits an exponential curve,
    and saves the plot to a PNG file.  Calculates chi-squared and uncertainties.

    Args:
        csv_file (str): Path to the CSV file containing the data.
                         The file should have columns: 'file_number', 'pulse_number',
                         'time_difference', 'threshold'.
        output_png (str): Path to save the generated histogram plot as a PNG file.
        initial_guess (tuple): Initial guess for the fitting parameters (A, tau, C).
                                 Defaults to (300, 2.2, 1).
    """

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file)
    df = df[df['time_difference'] >= 500]

    # Extract the 'time_difference' column and convert it to microseconds
    decay_times_ns = df['time_difference'].values
    decay_times_us = decay_times_ns / 1000.0

    # Create the histogram
    bins = 15
    hist = plt.hist(decay_times_us, bins=bins, color='skyblue', edgecolor='black')[0]
    bin_edges = plt.hist(decay_times_us, bins=bins, color='skyblue', edgecolor='black')[1]

    # Define the exponential function to fit
    def exponential_func(x, A, tau, C):
        return A * np.exp(-x / tau) + C

    # Fit the exponential curve
    popt, pcov = curve_fit(exponential_func, bin_edges[:-1], hist, p0=initial_guess)

    # Extract the fitted parameters
    A, tau, C = popt

    # Calculate uncertainties
    perr = np.sqrt(np.diag(pcov))
    dA, dtau, dC = perr

    # Generate points for the fitted curve
    x_fit = np.linspace(decay_times_us.min(), decay_times_us.max(), 100)
    y_fit = exponential_func(x_fit, A, tau, C)

    # Calculate chi-squared
    residuals = hist - exponential_func(bin_edges[:-1], A, tau, C)
    chi_squared = np.sum(residuals**2)
    degrees_of_freedom = len(hist) - 3  # Number of bins - number of fitted parameters

    # Plot the fitted curve
    plt.plot(x_fit, y_fit, 'r-', label=f'Ajuste: A={A:.2f} ± {dA:.2f}, τ={tau:.2f} μs ± {dtau:.2f}, C={C:.2f} ± {dC:.2f}')

    # Add labels and title
    plt.xlabel('Tiempo de Decaimiento (μs)')
    plt.ylabel('Conteo')
    plt.title('Histograma del Tiempo de Decaimiento')
    plt.legend()
    plt.grid(True)

    # Save the plot to a PNG file
    plt.savefig(output_png)
    plt.close()  # Close the figure to free memory

    # Print the fit results to the console
    print("Resultados del Ajuste:")
    print(f"  A = {A:.2f} ± {dA:.2f}")
    print(f"  τ = {tau:.2f} μs ± {dtau:.2f}")
    print(f"  C = {C:.2f} ± {dC:.2f}")
    print(f"  Chi-squared = {chi_squared:.2f}")
    print(f"  Grados de libertad = {degrees_of_freedom}")
    print(f"  Reducción Chi-cuadrado = {chi_squared/degrees_of_freedom:.2f}")


if __name__ == "__main__":
    csv_file = "vida_media_muon/picos_dobles.csv"
    output_png = "vida_media_muon/histograma.png"
    plot_decay_time_histogram(csv_file, output_png)