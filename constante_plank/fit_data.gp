# Set the output terminal
set terminal pngcairo enhanced font "Arial,12" size 1200,1000

# Set the output file
set output 'planck_constant_fits.png'

# Set some general plot settings
set title "Planck Constant Experiment Data and Fits"
set xlabel "V1"
set ylabel "V2"
set grid

# Read data from files and store in variables
azul = "azul.dat"
amarillo = "amarillo.dat"
verde = "verde.dat"
violeta = "violeta.dat"
uv = "uv.dat"

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

# Function for linear fit
f(x) = m*x + b

# Perform fits and plot for each color
set multiplot layout 3,2 title "Curvas de frenado para diferentes colores"

# Azul
set title "Azul"
fit f(x) azul using 1:3 via m,b
plot azul using 1:3 with linespoints title "Data" lc rgb azul_color, \
     f(x) title "Fit" lc rgb "red"
print sprintf("Azul slope: %e", m)

# Amarillo
set title "Amarillo"
fit f(x) amarillo using 1:3 via m,b
plot amarillo using 1:3 with linespoints title "Data" lc rgb amarillo_color, \
     f(x) title "Fit" lc rgb "red"
print sprintf("Amarillo slope: %e", m)

# Verde
set title "Verde"
fit f(x) verde using 1:3 via m,b
plot verde using 1:3 with linespoints title "Data" lc rgb verde_color, \
     f(x) title "Fit" lc rgb "red"
print sprintf("Verde slope: %e", m)

# Violeta
set title "Violeta"
fit f(x) violeta using 1:3 via m,b
plot violeta using 1:3 with linespoints title "Data" lc rgb violeta_color, \
     f(x) title "Fit" lc rgb "red"
print sprintf("Violeta slope: %e", m)

# UV
set title "UV"
fit f(x) uv using 1:3 via m,b
plot uv using 1:3 with linespoints title "Data" lc rgb uv_color, \
     f(x) title "Fit" lc rgb "red"
print sprintf("UV slope: %e", m)

unset multiplot

# Notify that processing is complete
print "Data processing and plotting complete. Check 'planck_constant_fits.png' for the output."