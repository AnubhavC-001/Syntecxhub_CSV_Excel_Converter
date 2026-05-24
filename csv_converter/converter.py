import pandas as pd
import os

def convert_csv_to_excel(csv_path: str, excel_path: str) -> None:
    """
    Converts a CSV file to an Excel (.xlsx) file.
    
    Args:
        csv_path (str): The path to the source CSV file.
        excel_path (str): The path where the Excel file should be saved.
        
    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If the input file is not a valid CSV or conversion fails.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Source file not found: {csv_path}")
    
    try:
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Write to Excel
        df.to_excel(excel_path, index=False, engine='openpyxl')
        
    except pd.errors.EmptyDataError:
        raise ValueError("The source CSV file is empty.")
    except pd.errors.ParserError:
        raise ValueError("Failed to parse the CSV file. Please ensure it is valid.")
    except Exception as e:
        raise ValueError(f"An error occurred during conversion: {str(e)}")

if __name__ == "__main__":
    # Quick CLI test
    import sys
    if len(sys.argv) == 3:
        try:
            convert_csv_to_excel(sys.argv[1], sys.argv[2])
            print("Conversion successful!")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: python converter.py <input_csv> <output_excel>")
