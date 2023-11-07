# PDF to SQL and Excel Converter

This Python application allows you to extract data from multiple PDF files, perform data extraction and transformation, and then save the data to a MySQL database and an Excel file.

## Features

- Extract specific data fields from multiple PDF files.
- Process and clean extracted data.
- Import cleaned data into a MySQL database.
- Export data to an Excel file for further analysis.

## Getting Started

### Prerequisites

- Python 3.x
- PyPDF2
- Pandas
- SQLAlchemy
- MySQL database
- Tkinter (for the graphical interface)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-to-sql-excel-converter.git
   cd pdf-to-sql-excel-converter
Install the required Python packages:
bash
Copy code
pip install PyPDF2 pandas sqlalchemy
Usage
Run the application:

bash
Copy code
python pdf_to_sql_excel.py
Click the "Process PDF Files" button in the graphical interface to select and process multiple PDF files.

The extracted data is displayed in a GUI window.

The cleaned data is imported into a MySQL database.

The data is also exported to an Excel file named "output.xlsx."

Configuration
Before running the application, make sure to configure your MySQL database connection in the pdf_to_sql_excel.py file.

python
Copy code
# Database connection details
db_username = "your-username"
db_password = "your-password"
db_host = "your-host"  # e.g., "localhost" or an IP address
db_name = "your-database-name"
Please replace the placeholders (`your-username`, `your-password`, `your-host`, `your-database-name`, and `your-email@example.com`) with your specific information.

Contact
For questions or support, please contact jabhi86839.com.
