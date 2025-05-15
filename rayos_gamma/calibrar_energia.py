import csv
import matplotlib.pyplot as plt
import os

def graph_eu152_data(file_path):
    """
    Graphs data from a CSV file containing channel and count measurements
    from Eu-152 decay, plotting count vs. channel on a log scale as a
    scatter plot (no lines), and saving the plot to a file in the same
    directory as the data file.  Also finds and displays local maxima.
    Saves the local maxima found to a CSV file.
    Args:
        file_path (str): The path to the CSV file.  The file should contain
                           no header row, with the first column representing
                           the channel and the second column representing the count.
    Returns:
        bool: True if the graph was successfully created and saved, False otherwise.
    """
    # 1. Data Loading and Processing
    channels = []
    counts = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)  # Use csv.reader for simple CSV files
        for row in reader:
            try:
                channel = int(row[0])
                count = int(row[1])
                channels.append(channel)
                counts.append(count)
            except (ValueError, IndexError) as e:
                print(f"Skipping row due to error: {e}. Row data: {row}")  # Handle bad data robustly.
                continue  # Skip to the next row
    if not channels or not counts:
        print("No valid data found in the file.")
        return False

    # 2. Find Local Maxima
    channel_cuts = [
        37, 63, 122, 175, 350, 500, 600, 750
    ] + [channels[-1]]
    maxima_indices = find_local_maxima(channels, counts, channel_cuts)

    # 3. Plotting
    plt.figure(figsize=(10, 6))  # Adjust figure size for better readability
    plt.yscale('log')  # Set y-axis to a logarithmic scale

    # 4. Plot Maxima Lines
    for i in maxima_indices:
        plt.axvline(x=channels[i], color='gray', linewidth=1)

    plt.scatter(channels, counts, s=10)  # Use plt.scatter for a dispersion plot

    # 5. Labels and Title (in Spanish)
    plt.xlabel("Canal", fontsize=12)  # Channel
    plt.ylabel("Conteo (Escala Logarítmica)", fontsize=12)  # Count (Logarithmic Scale)
    plt.title("Espectro de Decaimiento de Eu-152", fontsize=14)  # Eu-152 Decay Spectrum

    # 6. Save the Plot
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    name, ext = os.path.splitext(filename)
    output_file_path = os.path.join(directory, f"{name}_graph.png")
    plt.savefig(output_file_path)  # Save as PNG - a widely compatible format
    plt.close()  # Close the figure to free memory
    print(f"Graph saved to: {output_file_path}")

    # 7. Save Local Maxima to CSV
    local_maxima_file = os.path.join(directory, "local_maxima.csv")
    with open(local_maxima_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in maxima_indices:
            writer.writerow([channels[i], counts[i]])
    print(f"Local maxima saved to: {local_maxima_file}")

    return True


def find_local_maxima(channels, counts, channel_cuts):
    """
    Finds indices of local maxima in the data. A point is considered a
    local maximum if it is greater than its immediate neighbors.
    Args:
        channels (list): List of corresponding channel values.
        counts (list): List of corresponding count values.
        channel_cuts (list): List of channel values that define segments.
    Returns:
        list: List of indices of local maxima.
    """
    maxima_indices = []
    ini = 0
    segmented = 0
    for i, val in zip(channels, counts):
        if i < channel_cuts[segmented]:
            continue
        fin = i
        segment = counts[ini:fin]
        max_val = max(segment)
        max_index_in_segment = segment.index(max_val)
        maxima_indices.append(ini + max_index_in_segment)
        segmented += 1
        ini = i
    return maxima_indices


# Example Usage (replace with your actual file path)
file_path = "rayos_gamma/Eu-152.csv"  # Example path.  Make sure this file exists!
if graph_eu152_data(file_path):
    print("Graphing process completed successfully.")
else:
    print("Graphing process failed.")