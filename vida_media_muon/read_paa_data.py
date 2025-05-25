import os
import sys
import glob
import csv
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from paa01 import paaFile  # Assuming paa01.py contains the paaFile class



def process_paa_files(data_dir, csv_filename):
    """
    Processes paa files in a directory, identifies triggers, calculates time
    differences, and writes the results to a CSV file.

    Args:
        data_dir (str): The directory containing the paa files.
        csv_filename (str): The name of the CSV file to create.
    """
    paa_files = sorted(glob.glob(os.path.join(data_dir, "*.paa")))
    file_number = 1
    
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow( # header
            ['file_number', 'pulse_number'
            , 'time_difference', 'threshold']
            )

        for paa_file_path in paa_files:
            try:
                DataFile = paaFile(paa_file_path)
                pc = DataFile.paaGetPulseCount()

                for pulse_number in range(pc):
                    threshold = -150
                    pulse_data_v = DataFile.paaGetPulseRP(pulse_number) #or paaGetPulseRaw

                    triggers = []
                    current_min = None
                    current_min_idx = None
                    for idx,val in enumerate(pulse_data_v):
                        if current_min is None:
                            if val < threshold: 
                                current_min = val
                                current_min_idx = idx
                                
                                threshold = min(0.5*val, threshold)

                            continue
                        
                        if val < threshold:
                            if val < current_min:
                                current_min = val
                                current_min_idx = idx
                                
                                threshold = min(0.5*val, threshold)
                            
                            continue

                        triggers.append({
                            'value': val
                            , 'index': current_min_idx
                            , 'trsh': threshold
                        })

                        current_min = None
                        current_min_idx = None
                        

                    if len(triggers) >= 2:
                        # Calculate time difference between the first two triggers
                        time_difference = triggers[1]['index'] - triggers[0]['index']
                        time_difference_scaled = time_difference * 8 # Multiply by 8
                        csv_writer.writerow(
                            [file_number, pulse_number
                            , time_difference_scaled
                            , triggers[0]['trsh']])

            except Exception as e:
                print(f"Error processing file {paa_file_path}: {e}")

            file_number += 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python paa_processor.py <data_directory> <output_csv_file>")
        sys.exit(1)

    data_directory = sys.argv[1]
    output_csv_file = sys.argv[2]

    process_paa_files(data_directory, output_csv_file)
    print(f"Processing complete. Results written to {output_csv_file}")