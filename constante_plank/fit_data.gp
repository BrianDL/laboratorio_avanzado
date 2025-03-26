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

# Use stats to get max_x and max_y for each dataset
stats amarillo using 1:3 name "AMARILLO" nooutput
stats verde using 1:3 name "VERDE" nooutput
stats azul using 1:3 name "AZUL" nooutput
stats violeta using 1:3 name "VIOLETA" nooutput
stats uv using 1:3 name "UV" nooutput


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
fit [-0.2:] f(x) amarillo using 1:3 via m,b 

# Calculate 5% of the range for x and y
x_margin = 0.05 * (AMARILLO_max_x - AMARILLO_min_x)
y_margin = 0.05 * (AMARILLO_max_y - AMARILLO_min_y)

# Set x and y ranges based on the amarillo dataset with 5% margin
set xrange [AMARILLO_min_x - x_margin : AMARILLO_max_x + x_margin]
set yrange [AMARILLO_min_y - y_margin : AMARILLO_max_y + y_margin]

plot amarillo using 1:3 \
     with linespoints title "Data" lc rgb amarillo_color \
     , f(x) title "Fit" lc rgb "red"
print sprintf("Amarillo slope: %e", m)

# Reset ranges to autoscale for the next plot
set autoscale x
set autoscale y

# Verde
set title "Verde"
fit f(x) verde using 1:3 every ::14::16 via m,b
set autoscale xfix
set autoscale yfix
plot verde using 1:3 with linespoints title "Data" lc rgb verde_color, \
     f(x) title "Fit" lc rgb "red"
print sprintf("Verde slope: %e", m)
set autoscale

# Azul
set title "Azul"
fit f(x) azul using 1:3 every ::14::16 via m,b
set autoscale xfix
set autoscale yfix
plot azul using 1:3 with linespoints title "Data" lc rgb azul_color, \
     f(x) title "Fit" lc rgb "red"
print sprintf("Azul slope: %e", m)
set autoscale
# Violeta
set title "Violeta"
fit f(x) violeta using 1:3 every ::14::16 via m,b
set autoscale xfix
set autoscale yfix
plot violeta using 1:3 with linespoints title "Data" lc rgb violeta_color, \
     f(x) title "Fit" lc rgb "red"
print sprintf("Violeta slope: %e", m)
set autoscale

# UV
set title "UV"
fit f(x) uv using 1:3 every ::14::16 via m,b
set autoscale xfix
set autoscale yfix
plot uv using 1:3 with linespoints title "Data" lc rgb uv_color, \
     f(x) title "Fit" lc rgb "red"
print sprintf("UV slope: %e", m)
set autoscale

unset multiplot

# Notify that processing is complete
print "Data processing and plotting complete. Check 'planck_constant_fits.png' for the output."