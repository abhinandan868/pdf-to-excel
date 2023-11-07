import tkinter as tk
from tkinter import filedialog
import PyPDF2
import re
import pandas as pd

# Define the function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    pdf_text = ""

    pdf_reader = PyPDF2.PdfReader(pdf_path)

    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    return pdf_text

# Define the function to extract data from a PDF
def extract_data_from_pdf(pdf_path):
    data = {field: [] for field in regex_patterns}
    
    pdf_text = extract_text_from_pdf(pdf_path)
    
    for field, pattern in regex_patterns.items():
        matches = re.search(pattern, pdf_text)
        if matches:
            data[field] = matches.group(1)
        else:
            data[field] = ''

    return data

# Define the function to process the selected PDF files
def process_pdf_files():
    # Open a file dialog to select multiple PDF files
    pdf_file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])

    if pdf_file_paths:
        all_extracted_data = []

        for pdf_file_path in pdf_file_paths:
            extracted_data = extract_data_from_pdf(pdf_file_path)
            all_extracted_data.append(extracted_data)

        # Combine data from all PDFs into a single DataFrame
        combined_data = {field: [] for field in regex_patterns}
        for data in all_extracted_data:
            for field in data:
                combined_data[field].append(data[field])

        df = pd.DataFrame(combined_data)

        # Enable the "Download Excel" button and pass the DataFrame to the function
        download_excel_button.config(state="normal", command=lambda: download_excel(df))

# Define the function to download the DataFrame as an Excel file
def download_excel(dataframe):
    excel_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    if excel_file_path:
        dataframe.to_excel(excel_file_path, index=False)
        print(f"Excel file saved at: {excel_file_path}")

# Create the tkinter interface
root = tk.Tk()
root.title("PDF Data Processing")

# Define regular expressions for the fields you want to extract
regex_patterns = {
   "Transaction Date": r"Date\s*:\s*(\d{2}-\d{2}-\d{4})",
   "Our Reference Number": r"Our Reference Number\s*:\s*(\S+)",
   "L/C Number": r"L/C Number\s*:\s*(\S+)",
   "Amount for INR": r"for\s*:\s*INR ([\d,\.]+)",
   "Neg/Disc Amount": r"Neg/Disc Amount\s*:\s*INR ([\d,\.]+)",
   "Invoice Number": r"Invoice Number\s*:\s*(\S+)",
   "Draft Number": r"Draft Number\s*:\s*(\S+)",
   "GSTIN NUMBER": r"GSTIN NUMBER\s*:\s*(\S+)",
   "Amount of Bill": r"Amount of Bill\s*:\s*INR ([\d,\.]+)",
   "Negotiation Interest": r"Negotiation Interest\s*:\s*INR (\d+)",
   "Amount Credited": r"Amount Credited\s*:\s*INR ([\d,\.]+)",
   "Account Credited": r"Account Credited\s*:\s*(\S+)",
   "Postage/Cable Charge": r"Postage/Cable Charge\s*:\s*INR ([\d,\.]+)",
   "Other Charges": r"Other Charges\s*:\s*INR ([\d,\.]+)",
   "Negotiation Commission": r"Negotiation Commission\s*:\s*INR ([\d,\.]+)",
   "Discrepancy Charges": r"Discrepancy Charges\s*:\s*INR ([\d,\.]+)",
   "Goods and Service Tax": r"Goods and Service Tax\s*:\s*INR ([\d,\.]+)",
   "Other Bank Charges": r"Other Bank Charges\s*:\s*INR ([\d,\.]+)",
    # Add your regular expressions here
}

# Add a "Process PDF" button
process_button = tk.Button(root, text="Process PDF Files", command=process_pdf_files)
process_button.pack()

# Add a "Download Excel" button (initially disabled)
download_excel_button = tk.Button(root, text="Download Excel", state="disabled")
download_excel_button.pack()

root.mainloop()
