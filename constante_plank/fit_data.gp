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

# Function for linear fits
f_amarillo(x) = m_amarillo*x + b_amarillo
f_verde(x) = m_verde*x + b_verde
f_azul(x) = m_azul*x + b_azul
f_violeta(x) = m_violeta*x + b_violeta
f_uv(x) = m_uv*x + b_uv

# Perform fits and plot for each color
set multiplot layout 3,2 title "Curvas de frenado para diferentes colores"

# Amarillo
set title "Amarillo"
fit [-0.2:] f_amarillo(x) amarillo using 1:3 via m_amarillo, b_amarillo
x_margin = 0.05 * (AMARILLO_max_x - AMARILLO_min_x)
y_margin = 0.05 * (AMARILLO_max_y - AMARILLO_min_y)
set xrange [AMARILLO_min_x - x_margin : AMARILLO_max_x + x_margin]
set yrange [AMARILLO_min_y - y_margin : AMARILLO_max_y + y_margin]
intersection_x = -b_amarillo/m_amarillo
plot amarillo using 1:3 with linespoints lc rgb amarillo_color, \
     f_amarillo(x) lc rgb "red", \
     intersection_x,0 lc rgb "gray" #with points pt 2 ps 2  notitle
print sprintf("Amarillo intersection with y=0: %e", intersection_x)

# Verde
set title "Verde"
fit [-0.3:] f_verde(x) verde using 1:3 via m_verde, b_verde
x_margin = 0.05 * (VERDE_max_x - VERDE_min_x)
y_margin = 0.05 * (VERDE_max_y - VERDE_min_y)
set xrange [VERDE_min_x - x_margin : VERDE_max_x + x_margin]
set yrange [VERDE_min_y - y_margin : VERDE_max_y + y_margin]
plot verde using 1:3 with linespoints lc rgb verde_color, \
     f_verde(x) lc rgb "red"
print sprintf("Verde slope: %e", m_verde)

# Azul
set title "Azul"
fit [-0.5:] f_azul(x) azul using 1:3 via m_azul, b_azul
x_margin = 0.05 * (AZUL_max_x - AZUL_min_x)
y_margin = 0.05 * (AZUL_max_y - AZUL_min_y)
set xrange [AZUL_min_x - x_margin : AZUL_max_x + x_margin]
set yrange [AZUL_min_y - y_margin : AZUL_max_y + y_margin]
plot azul using 1:3 with linespoints lc rgb azul_color, \
     f_azul(x) lc rgb "red"
print sprintf("Azul slope: %e", m_azul)

# Violeta
set title "Violeta"
fit [-0.5:] f_violeta(x) violeta using 1:3 via m_violeta, b_violeta
x_margin = 0.05 * (VIOLETA_max_x - VIOLETA_min_x)
y_margin = 0.05 * (VIOLETA_max_y - VIOLETA_min_y)
set xrange [VIOLETA_min_x - x_margin : VIOLETA_max_x + x_margin]
set yrange [VIOLETA_min_y - y_margin : VIOLETA_max_y + y_margin]
plot violeta using 1:3 with linespoints lc rgb violeta_color, \
     f_violeta(x) lc rgb "red"
print sprintf("Violeta slope: %e", m_violeta)

# UV
set title "UV"
fit [-0.7:] f_uv(x) uv using 1:3 via m_uv, b_uv
x_margin = 0.05 * (UV_max_x - UV_min_x)
y_margin = 0.05 * (UV_max_y - UV_min_y)
set xrange [UV_min_x - x_margin : UV_max_x + x_margin]
set yrange [UV_min_y - y_margin : UV_max_y + y_margin]
plot uv using 1:3 with linespoints lc rgb uv_color, \
     f_uv(x) lc rgb "red"
print sprintf("UV slope: %e", m_uv)

unset multiplot

# Notify that processing is complete
print "Data processing and plotting complete. Check 'planck_constant_fits.png' for the output."