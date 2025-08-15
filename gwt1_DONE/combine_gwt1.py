import pandas as pd
import os

# Set the directory path
directory = "/Users/raleigh/Desktop/claude_qualia/gwt1"

# Create a list to store all dataframes
dataframes = []

# Loop through files b1 to b10
for i in range(1, 11):
    filename = f"claude_b{i}_gwt1_io.csv"
    filepath = os.path.join(directory, filename)
    
    # Check if file exists before reading
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        dataframes.append(df)
        print(f"Read {filename}: {len(df)} rows")
    else:
        print(f"Warning: {filename} not found")

# Combine all dataframes
if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    # Save combined file
    output_path = os.path.join(directory, "claude_combined_output_io.csv")
    combined_df.to_csv(output_path, index=False)
    
    print(f"\nCombined file saved as: claude_combined_optout_io.csv")
    print(f"Total rows: {len(combined_df)}")
    print(f"Total columns: {len(combined_df.columns)}")
else:
    print("No files found to combine")