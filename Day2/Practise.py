#File Handling
import csv 
from openpyxl import Workbook 
from openpyxl.styles import Font 

wb = Workbook()
ws = wb.active

csv_file_path = 'C:/Users/kavya/17_day_challenge/Day2/sample.csv'
excel_file_path = 'C:/Users/kavya/17_day_challenge/Day2/sample.xlsx'


ws.title = "Formatted Data"

bold_font = Font(bold=True)

try:
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)

        # Read the header row first
        header = next(reader)
        ws.append(header)

        # Apply bold formatting to each cell in the header row
        for cell in ws[1]:
            cell.font = bold_font

        # Write the rest of the data rows
        for row in reader:
            ws.append(row)

    wb.save(excel_file_path)
    print(f"Successfully created {excel_file_path} with bold headers.")
except FileNotFoundError:
    print(f"Error: The file {csv_file_path} was not found.")


lines = [
    ["120", "R", "12/07/2025", "M"],
    ["121", "G", "13/07/2025", "F"],
    ["122", "B", "14/07/2025", "M"]
]



try:
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as f:  # Open in append mode
        writer = csv.writer(f)
        for line in lines: 
            writer.writerow(line)
        # Write a new row of data
    
    print(f"Successfully added data to {csv_file_path}")
except FileNotFoundError:
    print(f"Error: The file {csv_file_path} was not found.")

import datetime as dt  

date_time = dt.datetime.now()
print(date_time)