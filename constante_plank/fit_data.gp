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
amarillo_int_x = (AMARILLO_min_y - b_amarillo)/m_amarillo
plot AMARILLO_min_y lc rgb "gray" \
     , f_amarillo(x) lc rgb "red" \
     , amarillo using 1:3 with linespoints lc rgb amarillo_color
print sprintf("Amarillo intersection with y=0: %e", amarillo_int_x)

# Verde
set title "Verde"
fit [-0.2:] f_verde(x) verde using 1:3 via m_verde, b_verde
x_margin = 0.05 * (VERDE_max_x - VERDE_min_x)
y_margin = 0.05 * (VERDE_max_y - VERDE_min_y)
set xrange [VERDE_min_x - x_margin : VERDE_max_x + x_margin]
set yrange [VERDE_min_y - y_margin : VERDE_max_y + y_margin]
verde_int_x = (VERDE_min_y - b_verde)/m_verde
plot VERDE_min_y lc rgb "gray" \
     , f_verde(x) lc rgb "red" \
     , verde using 1:3 with linespoints lc rgb verde_color
print sprintf("Verde intersection with y=0: %e", verde_int_x)

# Azul
set title "Azul"
fit [-0.5:] f_azul(x) azul using 1:3 via m_azul, b_azul
x_margin = 0.05 * (AZUL_max_x - AZUL_min_x)
y_margin = 0.05 * (AZUL_max_y - AZUL_min_y)
set xrange [AZUL_min_x - x_margin : AZUL_max_x + x_margin]
set yrange [AZUL_min_y - y_margin : AZUL_max_y + y_margin]
azul_int_x = (AZUL_min_y - b_azul)/m_azul
plot AZUL_min_y lc rgb "gray" \
     , f_azul(x) lc rgb "red" \
     , azul using 1:3 with linespoints lc rgb azul_color
print sprintf("Azul intersection with y=0: %e", azul_int_x)

# Violeta
set title "Violeta"
fit [-0.5:] f_violeta(x) violeta using 1:3 via m_violeta, b_violeta
x_margin = 0.05 * (VIOLETA_max_x - VIOLETA_min_x)
y_margin = 0.05 * (VIOLETA_max_y - VIOLETA_min_y)
set xrange [VIOLETA_min_x - x_margin : VIOLETA_max_x + x_margin]
set yrange [VIOLETA_min_y - y_margin : VIOLETA_max_y + y_margin]
violeta_int_x = (VIOLETA_min_y - b_violeta)/m_violeta
plot VIOLETA_min_y lc rgb "gray" \
     , f_violeta(x) lc rgb "red" \
     , violeta using 1:3 with linespoints lc rgb violeta_color
print sprintf("Violeta intersection with y=0: %e", violeta_int_x)

# UV
set title "UV"
fit [-0.5:] f_uv(x) uv using 1:3 via m_uv, b_uv
x_margin = 0.05 * (UV_max_x - UV_min_x)
y_margin = 0.05 * (UV_max_y - UV_min_y)
set xrange [UV_min_x - x_margin : UV_max_x + x_margin]
set yrange [UV_min_y - y_margin : UV_max_y + y_margin]
uv_int_x = (UV_min_y - b_uv)/m_uv
plot UV_min_y lc rgb "gray" \
     , f_uv(x) lc rgb "red" \
     , uv using 1:3 with linespoints lc rgb uv_color
print sprintf("UV intersection with y=0: %e", uv_int_x)

unset multiplot

# Print table of colors, frequencies, and y=0 intersects
print "\nColor\t\tFrequency (Hz)\tIntersection with y=0 (V)"
print "--------------------------------------------------------"
print sprintf("%.2fE12\t\t%.4f", amarillo_freq, abs(amarillo_int_x))
print sprintf("%.2fE12\t\t%.4f", verde_freq, abs(verde_int_x))
print sprintf("%.2fE12\t\t%.4f", azul_freq, abs(azul_int_x))
print sprintf("%.2fE12\t\t%.4f", violeta_freq, abs(violeta_int_x))
print sprintf("%.2fE12\t\t%.4f", uv_freq, abs(uv_int_x))