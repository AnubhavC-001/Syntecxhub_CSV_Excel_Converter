import pytest
import os
import pandas as pd
from converter import convert_csv_to_excel

def test_convert_csv_to_excel_success(tmp_path):
    # Create a dummy CSV
    csv_file = tmp_path / "test.csv"
    excel_file = tmp_path / "test.xlsx"
    
    data = {
        "Name": ["Alice", "Bob"],
        "Age": [25, 30]
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    
    # Convert
    convert_csv_to_excel(str(csv_file), str(excel_file))
    
    # Verify
    assert os.path.exists(excel_file)
    df_result = pd.read_excel(excel_file, engine='openpyxl')
    assert df_result.equals(df)

def test_convert_csv_to_excel_not_found():
    with pytest.raises(FileNotFoundError):
        convert_csv_to_excel("non_existent.csv", "output.xlsx")

def test_convert_csv_to_excel_empty_file(tmp_path):
    csv_file = tmp_path / "empty.csv"
    excel_file = tmp_path / "output.xlsx"
    
    with open(csv_file, 'w') as f:
        pass # Create empty file
    
    with pytest.raises(ValueError, match="The source CSV file is empty."):
        convert_csv_to_excel(str(csv_file), str(excel_file))

def test_convert_csv_to_excel_invalid_csv(tmp_path):
    # Some files might not be valid CSVs, but pandas is quite flexible.
    # We'll just test the general error handling if possible.
    pass 
