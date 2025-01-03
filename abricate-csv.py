import pandas as pd
import argparse

# Function to process the Abricate tab file and generate a summary CSV
def process_abricate(input_path, output_path, identity_threshold=90, coverage_threshold=90):
    # Read the input file into a DataFrame
    df = pd.read_csv(input_path, sep='\t')

    # Check if required columns exist
    required_columns = {'#FILE', 'GENE', '%IDENTITY', '%COVERAGE'}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")

    # Create an empty DataFrame to store the gene data
    output_df = pd.DataFrame()

    # Iterate through unique file names
    for file_name in df['#FILE'].unique():
        # Filter rows for the current file name
        file_data = df[df['#FILE'] == file_name]

        # Create a dictionary to store gene attributes for the current file
        gene_attributes = {'File': file_name}

        # Iterate through rows and update the gene_attributes dictionary
        for _, row in file_data.iterrows():
            if row['%IDENTITY'] >= identity_threshold and row['%COVERAGE'] >= coverage_threshold:
                gene_attributes[row['GENE']] = 1
            else:
                gene_attributes[row['GENE']] = 0

        # Append the gene_attributes to the output DataFrame
        output_df = pd.concat([output_df, pd.DataFrame([gene_attributes])], ignore_index=True)

    # Sort columns alphabetically (excluding 'File' column)
    output_df = output_df[['File'] + sorted(output_df.columns.difference(['File']))]

    # Fill NaN values with 0
    output_df = output_df.fillna(0)

    # Write the result to a CSV file
    output_df.to_csv(output_path, index=False)
    print(f"Gene data saved to {output_path}")

# Main function for command-line execution
def main():
    parser = argparse.ArgumentParser(description="Generate a gene summary from Abricate output.")
    parser.add_argument("input_file", help="Path to the Abricate output tab file.")
    parser.add_argument("-identity", type=float, default=90, help="Minimum %%IDENTITY threshold (default: 90).")
    parser.add_argument("-coverage", type=float, default=90, help="Minimum %%COVERAGE threshold (default: 90).")
    parser.add_argument("-output", default="abricate-summary.csv", help="Output CSV file name (default: abricate-summary.csv).")

    args = parser.parse_args()

    try:
        process_abricate(
            input_path=args.input_file,
            output_path=args.output,
            identity_threshold=args.identity,
            coverage_threshold=args.coverage
        )
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
