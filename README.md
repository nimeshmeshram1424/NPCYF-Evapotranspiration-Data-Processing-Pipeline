# NPCYF-Evapotranspiration-Data-Processing-Pipeline

A Data Cleaning and Transformation Pipeline for Evapotranspiration (ET) Datasets Supporting NPCYF.

## Project Overview

This repository contains the complete data processing pipeline developed as part of a child project under the National Platform for Crop Yield Forecasting (NPCYF).
The project focuses on the collection, cleaning, organization, and transformation of daily Evapotranspiration (ET) data across all states and districts of India.

Since the parent NPCYF project requires accurate and structured hydro-meteorological inputs for crop yield forecasting, this project provides a high-quality, analysis-ready ET dataset to support model development, validation, and environmental research.

## Objective

1. To prepare a clean, consistent, and analysis-ready Evapotranspiration dataset by:

2. Collecting daily ET Level and ET Volume data from trusted government portals (OGD Platform India).

3. Cleaning, standardizing, merging and splitting the data into separate ET Level and ET Volume files.

4. Transforming raw vertical data into a uniform, district-wise transposed, time-series structured format.

5. Providing a benchmark dataset that supports NPCYF’s automated data-acquisition and crop forecasting workflows.

## Dataset Description

The processed dataset consists of five primary attributes:

1. Date

2. State Name

3. District Name

4. Evapotranspiration Level (mm)

5. Evapotranspiration Volume (one thousand million cubic feet)

**Dataset Size**

**a. Raw files combined:** 526,775 rows

**b. After cleaning:** 523,797 rows

**c. Final processing:** Two separate CSV files (ET Level & ET Volume), each containing
 
- 523,797 rows

- 4 standardized columns

**Transposed Format**

Both final cleaned files were transformed manually into a structured time-series grid with:

- 846 rows (days)

- 640 columns (districts)

Each row represents one date; each column represents one district.

## Data Cleaning & Transformation Pipeline

Key Steps

**Standardization** – Applied uniform formatting to:

- State and district names

- Date formats

- ET Level and Volume fields

**Error Handling** – Removed structural inconsistencies, fixed formatting issues, and eliminated duplicate entries.

**Data Merging** – Combined multiple ET CSV files into a unified dataset.

**Data Cleaning** – Removed Duplicates and made column headings consistent. 

**Data Splitting** – Generated two separate files:

- Evapotranspiration Level.csv

- Evapotranspiration Volume.csv

**Manual Transformation** – Transposed vertically long data into structured, district-wise, time-series format.

**Final Export** – Generated clean CSV outputs ready for analysis.

## Full Python Pipeline

The complete implementation used to automate the merging, cleaning, standardizing, splitting, and exporting of ET data is provided in:

### Appendix 6.1 – Python Pipeline (Full Implementation)

This appendix contains all Python scripts developed for the automated processing of Evapotranspiration (ET) datasets. It includes the full workflow for:

- Cleaning and correcting structural inconsistencies

- Standardizing dates, state names, and district names

- Merging multiple ET CSV files

- Column Consistences and Cleaning

- Splitting the unified dataset into ET Level and ET Volume files

- Exporting clean, analysis-ready outputs

All corresponding code files referenced in the appendix are organized within the repository for easy navigation and reproducibility.

## Key Achievements

1. Cleaned and standardized all ET records; removed duplicate state/district entries and fixed formatting inconsistencies.

2. Merged multiple raw datasets into one complete, lossless master file.

3. Split the dataset into two focused components — ET Level and ET Volume — reducing complexity and improving analytical clarity.

4. Ensured consistent columns (Date, State, District, ET values), enabling easy appending of future datasets.

5. Produced a final 846-row clean dataset ready for statistical analysis, modeling, visualization, and integration into NPCYF workflows.

## Technical Contributions

1. Automated merging, cleaning, standardization, and exporting using Python scripts.

2. Eliminated structural errors, duplicates, missing-value issues, and non-uniform text entries.

3. Designed a modular, reusable data architecture suitable for daily, monthly, or yearly ET updates.

4. Delivered datasets directly usable for spatial analysis, time-series studies, and machine-learning applications.

## Analysis & Key Findings

1. ET Level and Volume display clear seasonal signatures aligned with known climatic zones.

2. Cleaning significantly improved data consistency and removed errors across files.

3. The transformed dataset supports reliable temporal and spatial trend analysis. enabling accurate trend identification, regional comparison, and long-term monitoring.

4. Final outputs serve as **benchmark datasets** for validating automated ET acquisition in the NPCYF parent project.

## Future Directions

1. Integrate additional ET datasets from ISRO–Bhuvan (NHP AET products).

2. Build an automated Python pipeline for real-time ET ingestion.

3. Combine ET with rainfall, soil moisture, vegetation indices, etc., for enhanced forecasting.

4. Apply GIS-based ET mapping and hotspot analysis.

5. Develop time-series forecasting (ARIMA/LSTM) and anomaly detection models.

6. Conduct long-term validation on crop performance across agro-climatic regions.

## Sources

OGD Platform India – Hydro-meteorological datasets

National Water Informatics Centre (NWIC)

National Hydrology Project (NHP), ISRO–Bhuvan Portal

## Contact

For queries or collaboration:
Name: Nimesh Meshram
Email: nimeshmeshram2069@gmail.com
