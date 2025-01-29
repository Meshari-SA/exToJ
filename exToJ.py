import pandas as pd
import json
import sys

def excel_to_json(excel_file_path, json_file_path):
    """
    Converts an Excel file to a JSON file.

    Parameters:
    excel_file_path (str): Path to the input Excel file.
    json_file_path (str): Path to the output JSON file.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file_path)
        
        # Convert datetime columns to custom string format
        for column in df.select_dtypes(include=['datetime']):
            df[column] = df[column].dt.strftime('%d %b %Y %H:%M:%S')
        
        # Remove newline characters from all string columns
        for column in df.select_dtypes(include=['object']):
            df[column] = df[column].str.replace('\n', ' ', regex=True)

        # Convert the DataFrame to a JSON object
        json_data = df.to_dict(orient='records')

        # Write the JSON data to a file
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        print(f"JSON file saved to: {json_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("""
        
        
    ███████╗██╗  ██╗████████╗ ██████╗      ██╗
    ██╔════╝╚██╗██╔╝╚══██╔══╝██╔═══██╗     ██║
    ████╗    ╚███╔╝    ██║   ██║   ██║     ██║
    ██╔══╝   ██╔██╗    ██║   ██║   ██║██   ██║
    ███████╗██╔╝ ██╗   ██║   ╚██████╔╝╚█████╔╝
    ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚════╝ 
                                         v0.1 By github.com/Meshari-SA
                                         
                                         
    [+] extoj - Excel to JSON Converter  
    [+] Convert Excel files into JSON format seamlessly  
    [+] Usage: python extoj.py <input_excel_file> <output_json_file>  

  
    """)
    
    if len(sys.argv) != 3:
        print("Usage: python exToJ.py <input_excel_file> <output_json_file>")
        print("")
        sys.exit(1)
    
    
    excel_file_path = sys.argv[1]
    json_file_path = sys.argv[2]
    
    if not json_file_path.endswith(".json"):
        json_file_path += ".json"
    
    excel_to_json(excel_file_path, json_file_path)
