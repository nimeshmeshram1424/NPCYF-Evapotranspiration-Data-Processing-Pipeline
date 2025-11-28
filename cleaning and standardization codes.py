import os
import numpy as np
import pandas as pd

# Folder containing all the downloaded CSV files
folder_path = r"L:\\IDEAS Internship\\Evapotranspiration Data\\Daily Evapotranspiration Data"

# List all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Check if any CSVs exist
if not csv_files:
    print("No CSV files found.")
else:
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        num_rows = len(df)
        print(f"{file}: {num_rows} rows") # This gives count of rows in each csv file.

    print(f"\nCounted rows for {len(csv_files)} CSV files.")

# Loop through each CSV file
for file in csv_files:
    file_path = os.path.join(folder_path, file)

    # Read the CSVs
    df = pd.read_csv(file_path)

    # Remove completely empty rows
    df.dropna(how='all', inplace=True)

    # Remove rows that just contain spaces
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df.dropna(how='all', inplace=True)
    
    # Convert columns to Lowercase and strip spaces
    df.columns = df.columns.str.strip().str.lower()

    # Rename ET columns to a uniform naming system
    rename_map = {
        'et (mm)': 'et_mm',
        'evapotranspiration level (mm)': 'et_mm',
        'actual et': 'et_mm',
        'aet_mm': 'et_mm',
        'et level': 'et_mm',
        'evapotranspiration level': 'et_mm',

        'evapotranspiration volume (one thousand million cubic feet)': 'et_tmc',
        'volume (tmc)': 'et_tmc',
        'et volume': 'et_tmc',
        'et vol': 'et_tmc',
        'volume (mcm)': 'et_mcm'
    }

    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    # Convert MCM to TMC if present
    if 'et_mcm' in df.columns:
        df['et_tmc'] = df['et_mcm'] / 28.3168466
        df.drop(columns=['et_mcm'], inplace=True)

    # Fix ET Level
    if 'et_mm' in df.columns:
        df['et_mm'] = pd.to_numeric(df['et_mm'], errors='coerce')
        df.loc[df['et_mm'] < 0, 'et_mm'] = np.nan
        
    # Fix ET Volume
    if 'et_tmc' in df.columns:
        df['et_tmc'] = pd.to_numeric(df['et_tmc'], errors='coerce')
        df.loc[df['et_tmc'] < 0, 'et_tmc'] = np.nan
        
    # Standardize text columns (STATE & DISTRICT in ALL CAPS)
    if 'state' in df.columns:
        df['state'] = df['state'].astype(str).str.upper().str.strip()

    if 'district' in df.columns:
        df['district'] = df['district'].astype(str).str.upper().str.strip()

    # Clean and reformat date column (dd-mm-yyyy)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['date'] = df['date'].dt.strftime('%d-%m-%Y')

    # Save cleaned file (overwrite original). Original files were Backed up by copying them.
    df.to_csv(file_path, index=False)

    print(f"Cleaned and saved: {file} ({len(df)} rows left)")

print("\nAll CSV files cleaned and standardized successfully!")
