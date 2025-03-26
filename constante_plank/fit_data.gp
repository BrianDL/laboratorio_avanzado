# Set the output terminal
set terminal pngcairo enhanced font "Arial,12" size 1200,1000

# Set the output file
set output 'planck_constant_fits.png'

# Set some general plot settings
set title "Planck Constant Experiment Data and Fits"
set grid
set key off

# Read data from files and store in variables
amarillo = "amarillo.dat"
verde = "verde.dat"
azul = "azul.dat"
violeta = "violeta.dat"
uv = "uv.dat"

# Use stats to get max_x and max_y for each dataset
stats amarillo using 1:3 name "AMARILLO" nooutput
stats verde using 1:3 name "VERDE" nooutput
stats azul using 1:3 name "AZUL" nooutput
stats violeta using 1:3 name "VIOLETA" nooutput
stats uv using 1:3 name "UV" nooutput

# Define colors for each dataset
amarillo_color = "orange"
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
fit [-0.2:] f(x) amarillo using 1:3 via m,b 
x_margin = 0.05 * (AMARILLO_max_x - AMARILLO_min_x)
y_margin = 0.05 * (AMARILLO_max_y - AMARILLO_min_y)
set xrange [AMARILLO_min_x - x_margin : AMARILLO_max_x + x_margin]
set yrange [AMARILLO_min_y - y_margin : AMARILLO_max_y + y_margin]
plot amarillo using 1:3 with linespoints lc rgb amarillo_color, \
     f(x) lc rgb "red"
print sprintf("Amarillo slope: %e", m)

# Verde
set title "Verde"
fit f(x) verde using 1:3 every ::14::16 via m,b
x_margin = 0.05 * (VERDE_max_x - VERDE_min_x)
y_margin = 0.05 * (VERDE_max_y - VERDE_min_y)
set xrange [VERDE_min_x - x_margin : VERDE_max_x + x_margin]
set yrange [VERDE_min_y - y_margin : VERDE_max_y + y_margin]
plot verde using 1:3 with linespoints lc rgb verde_color, \
     f(x) lc rgb "red"
print sprintf("Verde slope: %e", m)

# Azul
set title "Azul"
fit f(x) azul using 1:3 every ::14::16 via m,b
x_margin = 0.05 * (AZUL_max_x - AZUL_min_x)
y_margin = 0.05 * (AZUL_max_y - AZUL_min_y)
set xrange [AZUL_min_x - x_margin : AZUL_max_x + x_margin]
set yrange [AZUL_min_y - y_margin : AZUL_max_y + y_margin]
plot azul using 1:3 with linespoints lc rgb azul_color, \
     f(x) lc rgb "red"
print sprintf("Azul slope: %e", m)

# Violeta
set title "Violeta"
fit f(x) violeta using 1:3 every ::14::16 via m,b
x_margin = 0.05 * (VIOLETA_max_x - VIOLETA_min_x)
y_margin = 0.05 * (VIOLETA_max_y - VIOLETA_min_y)
set xrange [VIOLETA_min_x - x_margin : VIOLETA_max_x + x_margin]
set yrange [VIOLETA_min_y - y_margin : VIOLETA_max_y + y_margin]
plot violeta using 1:3 with linespoints lc rgb violeta_color, \
     f(x) lc rgb "red"
print sprintf("Violeta slope: %e", m)

# UV
set title "UV"
fit f(x) uv using 1:3 every ::14::16 via m,b
x_margin = 0.05 * (UV_max_x - UV_min_x)
y_margin = 0.05 * (UV_max_y - UV_min_y)
set xrange [UV_min_x - x_margin : UV_max_x + x_margin]
set yrange [UV_min_y - y_margin : UV_max_y + y_margin]
plot uv using 1:3 with linespoints lc rgb uv_color, \
     f(x) lc rgb "red"
print sprintf("UV slope: %e", m)

unset multiplot

# Notify that processing is complete
print "Data processing and plotting complete. Check 'planck_constant_fits.png' for the output."