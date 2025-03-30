# Set the output to a PNG file
set terminal pngcairo enhanced font "Arial,12" size 800,600
set output 'freq_vs_vf_plot.png'

# Set the title and labels
set title 'Potencial de Frenado vs Frecuencia'
set xlabel 'Frequency (THz)'
set ylabel 'Potencial de Frenado (V)'

# Set the grid
set grid

# Define the linear function to fit
f(x) = m*x - b

# Perform the linear fit
fit f(x) 'freq_and_vf.dat' using 1:2 via m, b

# Plot the data points and the fitted line
plot 'freq_and_vf.dat' using 1:2 with points pt 7 ps 1.5 title 'Experimental Data', \
     f(x) with lines lw 2 title 'Linear Fit'

# Add text box with fit results
set label sprintf("Slope = %.4e ± %.4e V/THz\nIntercept = %.4f ± %.4f V", \
                  m, m_err, b, b_err) \
    at graph 0.05, graph 0.95 left front

# Print the results
print sprintf("Slope = %.4e ± %.4e V/THz", m, m_err)
print sprintf("Intercept = %.4f ± %.4f V", b, b_err)

# Calculate Planck's constant
h = 1.602176E-19 * 1E-12 * m
print sprintf("Planck's constant = %.4e ± %.4e J·s", h, h * m_err / abs(m))

# Calculate work function
work_function = abs(b)
print sprintf("Work function = %.4f ± %.4f eV", work_function, b_err)

# Ensure all plotting is done before closing
set output