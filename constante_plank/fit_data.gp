# Set the output terminal (you can change this later if needed)
set terminal pngcairo enhanced font "Arial,12" size 800,600

# Set the default output file (you can change this later if needed)
set output 'output.png'

# Set some general plot settings
set title "Planck Constant Experiment Data"
set xlabel "Voltaje de Frenado (V)"
set ylabel "Corriente (A)"
set grid

# Read data from files and store in variables
azul = "azul.dat"
amarillo = "amarillo.dat"
verde = "verde.dat"
violeta = "violeta.dat"
uv = "uv.dat"

# Load the data into memory
azul_data = azul using 3:1:4:2
amarillo_data = amarillo using 3:1:4:2
verde_data = verde using 3:1:4:2
violeta_data = violeta using 3:1:4:2
uv_data = uv using 3:1:4:2

# Define colors for each dataset
azul_color = "blue"
amarillo_color = "yellow"
verde_color = "green"
violeta_color = "violet"
uv_color = "purple"

# Function to calculate frequency from wavelength
c = 299792458  # speed of light in m/s
f(wavelength) = c / (wavelength * 1e-9)  # wavelength in nm

# Define wavelengths for each color (in nm)
azul_wavelength = 450
amarillo_wavelength = 570
verde_wavelength = 530
violeta_wavelength = 400
uv_wavelength = 380

# Calculate frequencies
azul_freq = f(azul_wavelength)
amarillo_freq = f(amarillo_wavelength)
verde_freq = f(verde_wavelength)
violeta_freq = f(violeta_wavelength)
uv_freq = f(uv_wavelength)

# Print frequencies (for verification)
print sprintf("Frequencies (Hz): Azul=%.3e, Amarillo=%.3e, Verde=%.3e, Violeta=%.3e, UV=%.3e", \
              azul_freq, amarillo_freq, verde_freq, violeta_freq, uv_freq)

# Example plot command (commented out)
# plot azul_data with xyerrorbars title "Azul" lc rgb azul_color, \
#      amarillo_data with xyerrorbars title "Amarillo" lc rgb amarillo_color, \
#      verde_data with xyerrorbars title "Verde" lc rgb verde_color, \
#      violeta_data with xyerrorbars title "Violeta" lc rgb violeta_color, \
#      uv_data with xyerrorbars title "UV" lc rgb uv_color

# Notify that data is loaded
print "Data loaded successfully. Use 'load_data.gp' in your main script to access the data."