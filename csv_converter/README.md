# CSV to Excel Converter

A modern desktop application to convert CSV files to Microsoft Excel (.xlsx) format. Built with Python and CustomTkinter for a sleek, user-friendly experience.

## Features
- **Modern UI:** Clean, responsive design with dark/light mode support.
- **Easy File Selection:** Integrated file browsers for selecting source and destination.
- **Fast Conversion:** Uses `pandas` and `openpyxl` for efficient data processing.
- **Status Feedback:** Real-time updates on conversion status.
- **Robust:** Includes error handling for missing or invalid files.

## Installation

1. **Clone or Download** this repository.
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### GUI Mode
1. **Run the Application:**
   ```bash
   python app.py
   ```
2. **Select Source:** Click "Browse" to select your `.csv` file.
3. **Select Destination:** Choose where to save the converted `.xlsx` file.
4. **Convert:** Click "Convert Now" to start the process.

### CLI Mode
You can also use the tool directly from the terminal:
1. **Basic Conversion:**
   ```bash
   python cli.py data.csv
   ```
2. **Specify Output Path:**
   ```bash
   python cli.py data.csv -o result.xlsx
   ```
3. **Verbose Output:**
   ```bash
   python cli.py data.csv -v
   ```

## Running Tests
To verify the conversion logic:
```bash
pytest test_converter.py
```

## Built With
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern GUI framework.
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis.
- [OpenPyXL](https://openpyxl.readthedocs.io/) - Library to read/write Excel 2010 xlsx/xlsm files.
