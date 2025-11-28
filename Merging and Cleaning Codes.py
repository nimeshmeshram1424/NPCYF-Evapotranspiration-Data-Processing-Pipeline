import os
import numpy as np
import pandas as pd

# Folder containing all the CSV files
folder_path = r"L:\\IDEAS Internship\\Evapotranspiration Data\\Daily Evapotranspiration Data"  # <-- use 'r' for Windows paths

# List all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Check if any CSV files were found
if not csv_files:
    print("No CSV files found in the folder!")
else:
    dataframes = []

    # Read and append each CSV file
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        dataframes.append(df)
        print(f"Loaded: {file}")

    # Merge all dataframes into one
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Save the merged CSV file
    output_file = os.path.join(folder_path, "Complete Merged CSV File.csv")
    merged_df.to_csv(output_file, index=False)

    print(f"\nMerging complete! File saved as: {output_file}")

# Read the CSV file
df = pd.read_csv("L:\\IDEAS Internship\\Complete Merged CSV File.csv")

# Remove duplicate rows
df_clean = df.drop_duplicates()

# Rename columns (modify left side to match your original headings)
df_clean.rename(columns={
    "date": "Date",
    "state": "State",
    "district": "District",
    "et_mm": "Evapotranspiration Level (mm)",
    "et_tmc": "Evapotranspiration Volume (one thousand million cubic feet)"
}, inplace=True)

# Save to a new CSV file
df_clean.to_csv("L:\\IDEAS Internship\\Complete Merged CSV File (Data Cleaned).csv", index=False)

print("Duplicates removed and columns renamed successfully!")

# Input file path
input_path = r"L:\\IDEAS Internship\\Complete Merged CSV File (Data Cleaned).csv"

# Read the merged CSV file
df = pd.read_csv(input_path)

# Information regarding merged dataset
print("Sample Data of the Merged dataset is as follows:")
print(df.head())
print("Information about the Merged dataset is as follows:")
print(df.info())
print("Brief analysis and description of the Merged dataset is as follows:")
print(df.describe())
print("The Dimension of the Merged dataset is as follows:")
print(df.shape)
print("List of columns of the Merged dataset is as follows:")
print(df.columns)
print("Range Index of the Merged dataset is as follows:")
print(df.index)
