# Billify - Invoice Generation and Management System

**Billify** is a Python-based GUI application designed by **Anush Rithvic M** for generating invoices, managing customer details, and maintaining sales records. The app provides a user-friendly interface built with Tkinter and includes features for PDF invoice creation, database integration, and tax calculation.

---

![Billify](images/Billify.png)

---

## Features

- **Invoice Creation**  
  Easily input invoice details, product information, and buyer data to generate professional PDF invoices.

- **Database Integration**  
  Automatically save invoice details to a MySQL database for future reference.

- **Tax Calculation**  
  Supports both State and National tax types with automatic tax and total calculations.

- **User-Friendly Interface**  
  Simple and intuitive GUI designed with Tkinter.

- **Customization**  
  Placeholder text and form fields for seamless user interaction.

- **Number-to-Words Conversion**  
  Automatically converts numeric amounts to words in the generated PDF.

---

## Tech Stack

- **Python**: Core programming language.
- **Tkinter**: GUI framework for the application.
- **Pillow**: Image processing for the background.
- **FPDF**: PDF generation library.
- **MySQL**: Database to store invoice details.

---

## Prerequisites

Ensure the following are installed on your system:

1. **Python 3.x**  
   Download from [Python Official Website](https://www.python.org/).

2. **MySQL server**  
   Install MySQL from [MySQL Official Website](https://www.mysql.com/).

3. **Required Python libraries**  
   Install using pip:  
   ```bash
   pip install mysql-connector-python Pillow fpdf

## Installation and Setup

1. **Clone this repository**  

2. **Update database credentials**  
   Update the add_into_database function in the Billify.py script with your MySQL credentials. Replace 
   the placeholders in the following code snippet with your actual database details:
   ```Python
   connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
    )

3. **Update Company Details**  
   Update the generate_invocie function in the Billify.py script with your Company Details. 

4. **Create a MySQL table**  
   Set up the required table in your MySQL database to store invoice details. Use the following SQL 
   command:  
   ```bash
   CREATE TABLE invoices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_number VARCHAR(255),
    buyer_name VARCHAR(255),
    product_details TEXT,
    total_amount FLOAT,
    tax_type VARCHAR(50),
    tax_amount FLOAT,
    final_amount FLOAT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

5.	**Add the required background image**
    Place the Billify.png file in the same directory as the Billify.py script. This image is used as 
    the application’s background.

6.  **Run the application**
    Launch the application by running the following command in your terminal:
    ```bash
    python Billify.py

## How to Use

1. **Launch the application**  
   Run the Billify.py script to open the GUI.

2. **Input details**  
   Fill in the invoice, buyer, and product details in the respective fields.

3. **Select tax type**  
   Choose either State or National tax and click the “Generate Invoice” button to create a PDF.

4. **Database storage**
   All invoice details are automatically stored in the MySQL database for future reference.



## Contact

For questions or support, please contact:

. **Name**: Anush Rithvic M  
. **E-mail**: anushrithvic@gmail.com




 
