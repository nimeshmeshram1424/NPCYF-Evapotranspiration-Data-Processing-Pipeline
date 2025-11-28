import os
import numpy as np
import pandas as pd

# Input file path
input_path = r"L:\\IDEAS Internship\\Complete Merged CSV File (Data Cleaned).csv"

# Read the merged CSV file
df = pd.read_csv(input_path)

# Split into two DataFrames
df_level = df[['Date', 'State', 'District', 'Evapotranspiration Level (mm)']]
df_volume = df[['Date', 'State', 'District', 'Evapotranspiration Volume (one thousand million cubic feet)']]

# Get the folder of the input file
output_folder = os.path.dirname(input_path)

# Export both DataFrames to the same folder
df_level.to_csv(os.path.join(output_folder, 'Evapotranspiration Level.csv'), index=False)
df_volume.to_csv(os.path.join(output_folder, 'Evapotranspiration Volume.csv'), index=False)

print("Files created and exported successfully in the same folder as input:")
print("1. Evapotranspiration Level.csv")
print("2. Evapotranspiration Volume.csv")

# Input file path of the splitted files
input_path1 = r"L:\\IDEAS Internship\\Evapotranspiration Level.csv"
input_path2 = r"L:\\IDEAS Internship\\Evapotranspiration Volume.csv"

# Read the splitted CSV files
df1 = pd.read_csv(input_path1)
df2 = pd.read_csv(input_path2)

# Information regarding Evapotranspiration Level dataset
print("Sample Data of the Evapotranspiration Level dataset is as follows:")
print(df1.head())
print("Information about the Evapotranspiration Level dataset is as follows:")
print(df1.info())
print("Brief analysis and description of the Evapotranspiration Level dataset is as follows:")
print(df1.describe())
print("The Dimension of the Evapotranspiration Level dataset is as follows:")
print(df1.shape)
print("List of columns of the Evapotranspiration Level dataset is as follows:")
print(df1.columns)
print("Range Index of the Evapotranspiration Level dataset is as follows:")
print(df1.index)

# Information regarding Evapotranspiration Volume dataset
print("Sample Data of the Evapotranspiration Volume dataset is as follows:")
print(df2.head())
print("Information about the Evapotranspiration Volume dataset is as follows:")
print(df2.info())
print("Brief analysis and description of the Evapotranspiration Volume dataset is as follows:")
print(df2.describe())
print("The Dimension of the Evapotranspiration Volume dataset is as follows:")
print(df2.shape)
print("List of columns of the Evapotranspiration Volume dataset is as follows:")
print(df2.columns)
print("Range Index of the Evapotranspiration Volume dataset is as follows:")
print(df2.index)
