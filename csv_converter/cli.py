import argparse
import sys
import os
from converter import convert_csv_to_excel

def main():
    parser = argparse.ArgumentParser(
        description="Convert CSV files to Excel (.xlsx) format via Command Line."
    )
    
    parser.add_argument(
        "input", 
        help="Path to the source CSV file."
    )
    
    parser.add_argument(
        "-o", "--output", 
        help="Path to the output Excel file. If not provided, it will use the input filename with .xlsx extension."
    )
    
    parser.add_argument(
        "-v", "--verbose", 
        action="store_true", 
        help="Enable verbose output."
    )

    args = parser.parse_args()

    # Determine output path if not provided
    input_path = args.input
    output_path = args.output
    
    if not output_path:
        output_path = os.path.splitext(input_path)[0] + ".xlsx"

    if args.verbose:
        print(f"Converting: {input_path} -> {output_path}")

    try:
        convert_csv_to_excel(input_path, output_path)
        print(f"Successfully converted: {output_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
