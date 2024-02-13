import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import argparse

def main(inputFolder, outputFolder):
    files_to_plot = [
        'P1_Temperatures_Processed(degC).csv',
        'P2_Temperatures_Processed(degC).csv',
        'P3_Temperatures_Processed(degC).csv',
        'P4_Temperatures_Processed(degC).csv'
    ]

    dataframes = {}
    for file_name in files_to_plot:
        file_path = os.path.join(inputFolder, file_name)
        dataframes[file_name] = pd.read_csv(file_path)

    fig, axes = plt.subplots(nrows=1, ncols=len(files_to_plot), figsize=(5 * len(files_to_plot), 6))

    for idx, file_name in enumerate(files_to_plot):
        df = dataframes[file_name]

        time_column = df.columns[0]
        temperature_columns = df.columns[1:].tolist()

        df['Time (hours)'] = df[time_column] / 3600

        if 'Time (hours)' in temperature_columns:
            temperature_columns.remove('Time (hours)')

        ax = axes[idx]

        for column in temperature_columns:
            ax.plot(df['Time (hours)'], df[column], label=column)

        ax.set_xlim(0, 4)
        ax.set_xticks([0, 1, 2, 3, 4])
        ax.legend()
        ax.grid(True)
        ax.set_title(f'Timeseries of {file_name}')
        ax.set_xlabel('Time (hours)')
        ax.set_ylabel('Temperature (deg.C)')

    os.makedirs(os.path.join(outputFolder), exist_ok=True)
    plt.tight_layout()
    plt.savefig(outputFolder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFolder", help="Path to the input folder containing CSV files")
    parser.add_argument("outputFolder", help="Path to the output folder for saving plots")
    args = parser.parse_args()

    main(args.inputFolder, args.outputFolder)
