# Abricate-Summary-Matrix

A Python script to process [Abricate](https://github.com/tseemann/abricate) output files and generate a binary gene presence/absence matrix in CSV format. Designed for bioinformatics workflows, this tool allows easy customization of identity and coverage thresholds for AMR gene profiling.

## Features
- Converts Abricate `.tab` output into a summarized CSV matrix.
- Supports user-defined thresholds for `%IDENTITY` and `%COVERAGE` (default: 90% each).
- Outputs a binary matrix where rows represent samples and columns represent genes.
- Lightweight and easy to integrate into bioinformatics pipelines.

## Installation
Ensure Python 3 and `pandas` are installed:
```
pip install pandas
```

## Usage
Run the script from the command line:
```
python abricate-csv.py [abricate_output_tab_file]
```

### Optional Arguments
- `-identity`: Minimum `%IDENTITY` threshold (default: 90).
- `-coverage`: Minimum `%COVERAGE` threshold (default: 90).
- `-output`: Output CSV file name (default: `abricate-summary.csv`).

### Example Command
```
python abricate-csv.py results_plasmid.tab -identity 95 -coverage 85 -output abricate-summary.csv
```

## Requirements
- Python 3.x
- pandas

## Output
The output is a CSV file with:
- **Rows**: Sample file names.
- **Columns**: Genes identified by Abricate.
- **Values**: `1` if the gene passes thresholds, `0` otherwise.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests for enhancements or bug fixes.
