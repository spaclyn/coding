import pandas as pd
import numpy as np

# Import the CSV file
try:
    df = pd.read_csv('movies.csv')
    print("File imported successfully!")
    print(f"Original shape: {df.shape}")
except FileNotFoundError:
    print("Error: movies.csv file not found. Please make sure it's in the correct directory.")
    exit()
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# Display initial info
print("\nInitial data info:")
print(df.info())
print("\nFirst few rows:")
print(df.head())

# Data cleaning steps
print("\nStarting data cleaning...")

# Check for missing values
print("\n1. Missing values before cleaning:")
print(df.isnull().sum())

# Clean column names (remove special characters, make consistent)
df.columns = df.columns.str.strip().str.upper().str.replace('-', '_').str.replace(' ', '_')
print(f"\n2. Cleaned column names: {list(df.columns)}")

# Create a copy to avoid chained assignment warnings
df_clean = df.copy()

# 4. Handle missing values - FIXED VERSION
# For numeric columns, fill with median only if there are values
numeric_columns = ['YEAR', 'RATING', 'VOTES', 'RUNTIME', 'GROSS']
for col in numeric_columns:
    if col in df_clean.columns:
        # Convert to numeric, forcing errors to NaN
        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
        
        # Only fill if we have some valid values
        if not df_clean[col].isnull().all():  # If not all values are NaN
            median_val = df_clean[col].median()
            # Check if median is not NaN before filling
            if not pd.isna(median_val):
                df_clean[col] = df_clean[col].fillna(median_val)
            else:
                # If all values are NaN, fill with 0
                df_clean[col] = df_clean[col].fillna(0)
        else:
            # If all values are NaN, fill with 0
            df_clean[col] = 0

# For text columns, fill with 'Unknown'
text_columns = ['MOVIES', 'GENRE', 'ONE_LINE', 'STARS']
for col in text_columns:
    if col in df_clean.columns:
        df_clean[col] = df_clean[col].fillna('Unknown')

# Clean specific columns --Fixed VERSION
if 'YEAR' in df_clean.columns:
    # Convert to integer safely
    df_clean['YEAR'] = pd.to_numeric(df_clean['YEAR'], errors='coerce')
    # Replace any remaining NaN with 0 before converting to int
    df_clean['YEAR'] = df_clean['YEAR'].fillna(0)
    df_clean['YEAR'] = df_clean['YEAR'].astype(int)

if 'RATING' in df_clean.columns:
    df_clean['RATING'] = pd.to_numeric(df_clean['RATING'], errors='coerce')
    df_clean['RATING'] = df_clean['RATING'].fillna(0)

if 'VOTES' in df_clean.columns:
    # Remove commas and convert to numeric
    df_clean['VOTES'] = df_clean['VOTES'].astype(str).str.replace(',', '')
    df_clean['VOTES'] = pd.to_numeric(df_clean['VOTES'], errors='coerce')
    df_clean['VOTES'] = df_clean['VOTES'].fillna(0).astype(int)

if 'RUNTIME' in df_clean.columns:
    # Extract numbers from runtime (remove 'min' etc.)
    df_clean['RUNTIME'] = df_clean['RUNTIME'].astype(str).str.extract('(\d+)')[0]
    df_clean['RUNTIME'] = pd.to_numeric(df_clean['RUNTIME'], errors='coerce')
    df_clean['RUNTIME'] = df_clean['RUNTIME'].fillna(0).astype(int)

if 'GROSS' in df_clean.columns:
    # Clean gross earnings (remove $, M, commas)
    df_clean['GROSS'] = df_clean['GROSS'].astype(str).str.replace('$', '').str.replace('M', '').str.replace(',', '')
    df_clean['GROSS'] = pd.to_numeric(df_clean['GROSS'], errors='coerce')
    df_clean['GROSS'] = df_clean['GROSS'].fillna(0)

if 'GENRE' in df_clean.columns:
    # Clean genre column
    df_clean['GENRE'] = df_clean['GENRE'].str.strip().str.title()

# Remove duplicates
initial_rows = len(df_clean)
df_clean = df_clean.drop_duplicates()
final_rows = len(df_clean)
print(f"\n3. Removed {initial_rows - final_rows} duplicate rows")

#Check for missing values after cleaning
print("\n4. Missing values after cleaning:")
print(df_clean.isnull().sum())

# Display cleaned data info
print("\nCleaned data info:")
print(df_clean.info())
print("\nFirst few rows of cleaned data:")
print(df_clean.head())

# Summary statistics
print("\nSummary statistics:")
print(df_clean.describe())

# Save cleaned data
try:
    df_clean.to_csv('movies_cleaned.csv', index=False)
    print("\nCleaned data saved as 'movies_cleaned.csv'")
except Exception as e:
    print(f"Error saving cleaned file: {e}")

print("\nData cleaning completed successfully!")