# Set output to a PNG file
set terminal pngcairo enhanced font "Arial,12" size 800,600
set output 'rutherford_fit.png'

# Set the title and labels
set title 'Dispersión de Rutherford: Datos y ajuste'
set xlabel 'Ángulo θ (grados)'
set ylabel 'Número de partículas (N)'

# Set logarithmic scale for y-axis
set logscale y

# Set the grid
set grid

# Define the function to fit
f(x) = k * (sin(x/2*pi/180))**(-n)

# Initial guesses for parameters
k = 1e6
n = 4

# Perform the fit (excluding the first point at 0 degrees)
fit f(x) 'rutherford_data.txt' using 1:2 every ::1 via k, n

# Plot the data and the fitted curve
plot 'rutherford_data.txt' using 1:2 with points pt 7 ps 1.5 title 'Datos experimentales', \
     f(x) with lines lw 2 title 'Ajuste: k sin^{-n}(θ/2)'

# Add text box with fit results
set label sprintf("k = %.2e ± %.2e\nn = %.2f ± %.2f\n", k, k_err, n, n_err) \
    at graph 0.05, graph 0.95 left front

# Print the results
print sprintf("k = %.2e ± %.2e", k, k_err)
print sprintf("n = %.2f ± %.2f", n, n_err)

# Ensure all plotting is done before closing
set output