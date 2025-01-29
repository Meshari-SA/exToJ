
# **exToJ - Excel to JSON Converter**

🎯 **exToJ** is a simple yet powerful command-line tool that converts Excel files (`.xlsx`) into structured JSON format. It ensures seamless data transformation while handling datetime formats and removing unwanted newline characters.

## 🚀 Features

✅ Converts Excel (`.xlsx`) files to JSON format  
✅ Automatically formats datetime columns as `DD MMM YYYY HH:MM:SS`  
✅ Cleans newline characters in string fields  
✅ Command-line usage for efficiency  
✅ Lightweight and easy to use  

## 📌 Installation

Ensure you have Python installed, then install the necessary dependencies:

```bash
pip install pandas openpyxl
```

## ⚡ Usage

Run the script from the command line:

```bash
python extoj.py <input_excel_file> <output_json_file>
```

### Example:

```bash
python extoj.py sample.xlsx output.json
```

This will generate a JSON file (`output.json`) with properly formatted data.

## 🔧 Requirements

- Python 3.x
- `pandas` and `openpyxl` libraries

## 🛠️ How It Works

1. Reads the Excel file (`.xlsx`).
2. Converts all datetime columns into the format: `27 Jan 2025 15:04:12`.
3. Cleans string values by removing newline characters (`\n`).
4. Exports the data into a structured JSON file.

## 🎨 Banner

```plaintext
███████╗██╗  ██╗████████╗ ██████╗      ██╗
██╔════╝╚██╗██╔╝╚══██╔══╝██╔═══██╗     ██║
████╗    ╚███╔╝    ██║   ██║   ██║     ██║
██╔══╝   ██╔██╗    ██║   ██║   ██║██   ██║
███████╗██╔╝ ██╗   ██║   ╚██████╔╝╚█████╔╝
╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚════╝ 

[+] extoj - Excel to JSON Converter  
[+] Convert Excel files into JSON format seamlessly  
[+] Usage: python extoj.py <input_excel_file> <output_json_file>  
```

## ⚠️ Notes

- The output JSON file preserves column names as keys.
- Ensure the Excel file follows a structured format with headers in the first row.
- If an output filename is given without `.json`, the script will automatically append it.

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

## 📜 License

This project is licensed under the **MIT License**.

