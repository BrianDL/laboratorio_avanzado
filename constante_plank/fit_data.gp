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
amarillo = "amarillo.dat"
verde = "verde.dat"
azul = "azul.dat"
violeta = "violeta.dat"
uv = "uv.dat"

# Define colors for each dataset
amarillo_color = "yellow"
verde_color = "green"
azul_color = "blue"
violeta_color = "violet"
uv_color = "purple"

# Color frequencies
amarillo_freq = 519
verde_freq = 549
azul_freq = 688
violeta_freq = 741
uv_freq = 822

# Function for linear fit
f(x) = m*x + b

# Perform fits and plot for each color
set multiplot layout 3,2 title "Curvas de frenado para diferentes colores"

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

# Azul
set title "Azul"
fit f(x) azul using 1:3 via m,b
plot azul using 1:3 with linespoints title "Data" lc rgb azul_color, \
     f(x) title "Fit" lc rgb "red"
print sprintf("Azul slope: %e", m)
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