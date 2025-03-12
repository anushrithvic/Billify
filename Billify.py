from tkinter import *
from PIL import ImageTk, Image
from fpdf import FPDF
import os
import subprocess
import platform

# Create the main window
Billify = Tk()
Billify.geometry('1460x830')
Billify.resizable(False, False)
Billify.title("Billify")

# Load the image using Pillow
Bg_image = ImageTk.PhotoImage(Image.open('billify.png'))

# Create a label to display the image
Label(Billify, image=Bg_image).place(x=0, y=0)

# Define the StringVar and IntVar variables
Invoice = StringVar()
Date = StringVar()
Transporter = StringVar()
Vehicle = StringVar()
LR_No = StringVar()
Trans_Gst = StringVar()
Buyer_Name = StringVar()
Address_1 = StringVar()
Address_2 = StringVar()
Address_3 = StringVar()
Address_4 = StringVar()
Buyer_gst = StringVar()
Ship_to = StringVar()
S_Address_1 = StringVar()
S_Address_2 = StringVar()
S_Address_3 = StringVar()
S_Address_4 = StringVar()
Ship_gst = StringVar()
Eway_bill = StringVar()
Tax_Type = StringVar()
check = IntVar()
Product1, Hsn_Code1, Quantity1, rate_per_quantity1, Amount1 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
Product2, Hsn_Code2, Quantity2, rate_per_quantity2, Amount2 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
Product3, Hsn_Code3, Quantity3, rate_per_quantity3, Amount3 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
P2 = IntVar()
P3 = IntVar()

# Function to handle 'Same' checkbox
same = 0
def print_selection():
    global same
    same = check.get()  # Update ss value depending on the checkbox state

# Placeholder function
def set_placeholder(entry, placeholder_text):
    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, 'end')
            entry.config(fg='black')

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, placeholder_text)
            entry.config(fg='grey')

    entry.insert(0, placeholder_text)
    entry.config(fg='grey')
    entry.bind('<FocusIn>', on_focus_in)
    entry.bind('<FocusOut>', on_focus_out)

# Invoice details
entry_invoice = Entry(Billify, width=13, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Invoice)
entry_invoice.place(x=762, y=235)
set_placeholder(entry_invoice, "Enter Invoice No")

entry_date = Entry(Billify, width=13, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Date)
entry_date.place(x=762, y=270)
set_placeholder(entry_date, "DD/MM/YYYY")

entry_eway = Entry(Billify, width=13, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Eway_bill)
entry_eway.place(x=762, y=310)
set_placeholder(entry_eway, "Enter E-Way Bill")

# Transporter details
entry_transporter = Entry(Billify, width=25, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Transporter)
entry_transporter.place(x=1135, y=230)
set_placeholder(entry_transporter, "Transporter Name")

entry_vehicle = Entry(Billify, width=25, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Vehicle)
entry_vehicle.place(x=1135, y=270)
set_placeholder(entry_vehicle, "Vehicle No.")

entry_lr_no = Entry(Billify, width=25, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=LR_No)
entry_lr_no.place(x=1135, y=310)
set_placeholder(entry_lr_no, "LR Number")

entry_trans_gst = Entry(Billify, width=25, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Trans_Gst)
entry_trans_gst.place(x=1135, y=345)
set_placeholder(entry_trans_gst, "Transporter GST No.")

# Buyer's details
entry_buyer_name = Entry(Billify, width=30, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Buyer_Name)
entry_buyer_name.place(x=250, y=235)
set_placeholder(entry_buyer_name, "Buyer Name")

entry_address_1 = Entry(Billify, width=35, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Address_1)
entry_address_1.place(x=40, y=320)
set_placeholder(entry_address_1, "Address Line 1")

entry_address_2 = Entry(Billify, width=35, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Address_2)
entry_address_2.place(x=40, y=345)
set_placeholder(entry_address_2, "Address Line 2")

entry_address_3 = Entry(Billify, width=35, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Address_3)
entry_address_3.place(x=40, y=370)
set_placeholder(entry_address_3, "Address Line 3")

entry_address_4 = Entry(Billify, width=35, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Address_4)
entry_address_4.place(x=40, y=395)
set_placeholder(entry_address_4, "Address Line 4")

entry_buyer_gst = Entry(Billify, width=30, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Buyer_gst)
entry_buyer_gst.place(x=250, y=440)
set_placeholder(entry_buyer_gst, "Buyer GST No.")

# Shipping Address
entry_ship_to = Entry(Billify, width=35, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Ship_to)
entry_ship_to.place(x=185, y=530)
set_placeholder(entry_ship_to, "Ship To")

entry_s_address1 = Entry(Billify, width=35, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=S_Address_1)
entry_s_address1.place(x=40, y=610)
set_placeholder(entry_s_address1, "Address Line 1")

entry_s_address2 = Entry(Billify, width=35, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=S_Address_2)
entry_s_address2.place(x=40, y=635)
set_placeholder(entry_s_address2, "Address Line 2")

entry_s_address3 = Entry(Billify, width=35, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=S_Address_3)
entry_s_address3.place(x=40, y=660)
set_placeholder(entry_s_address3, "Address Line 3")

entry_s_address4 = Entry(Billify, width=35, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=S_Address_4)
entry_s_address4.place(x=40, y=685)
set_placeholder(entry_s_address4, "Address Line 4")

entry_ship_gst = Entry(Billify, width=35, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Ship_gst)
entry_ship_gst.place(x=150, y=720)
set_placeholder(entry_ship_gst, "Shipping GST")

# Product details
#Product 1
entry_product1 = Entry(Billify, width=25, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Product1)
entry_product1.place(x=590, y=500)
set_placeholder(entry_product1, "Product Name 1")

entry_hsn1 = Entry(Billify, width=8, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Hsn_Code1)
entry_hsn1.place(x=826, y=500)
set_placeholder(entry_hsn1, "HSN Code")

entry_quantity1 = Entry(Billify, width=10, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Quantity1)
entry_quantity1.place(x=930, y=500)
set_placeholder(entry_quantity1, "Quantity")

entry_rate1 = Entry(Billify, width=13, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=rate_per_quantity1)
entry_rate1.place(x=1049, y=500)
set_placeholder(entry_rate1, "Rate per Qty")

entry_amount1 = Entry(Billify, width=20, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Amount1)
entry_amount1.place(x=1200, y=500)
set_placeholder(entry_amount1, "Amount")

# Product 2
entry_product2 = Entry(Billify, width=25, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Product2)
entry_product2.place(x=590, y=540)
set_placeholder(entry_product2, "Product Name 2")

entry_hsn2 = Entry(Billify, width=8, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Hsn_Code2)
entry_hsn2.place(x=826, y=540)
set_placeholder(entry_hsn2, "HSN Code")

entry_quantity2 = Entry(Billify, width=10, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Quantity2)
entry_quantity2.place(x=930, y=540)
set_placeholder(entry_quantity2, "Quantity")

entry_rate2 = Entry(Billify, width=13, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=rate_per_quantity2)
entry_rate2.place(x=1049, y=540)
set_placeholder(entry_rate2, "Rate per Qty")

entry_amount2 = Entry(Billify, width=20, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Amount2)
entry_amount2.place(x=1200, y=540)
set_placeholder(entry_amount2, "Amount")

# Product 3
entry_product3 = Entry(Billify, width=25, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Product3)
entry_product3.place(x=590, y=580)
set_placeholder(entry_product3, "Product Name 3")

entry_hsn3 = Entry(Billify, width=8, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Hsn_Code3)
entry_hsn3.place(x=826, y=580)
set_placeholder(entry_hsn3, "HSN Code")

entry_quantity3 = Entry(Billify, width=10, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Quantity3)
entry_quantity3.place(x=930, y=580)
set_placeholder(entry_quantity3, "Quantity")

entry_rate3 = Entry(Billify, width=13, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=rate_per_quantity3)
entry_rate3.place(x=1049, y=580)
set_placeholder(entry_rate3, "Rate per Qty")

entry_amount3 = Entry(Billify, width=20, bg='White', font="helvetica", insertbackground="Black", insertwidth=3, textvariable=Amount3)
entry_amount3.place(x=1200, y=580)
set_placeholder(entry_amount3, "Amount")


Checkbutton(Billify, bg='White', fg='Black', border=2, text='Same', variable=check, onvalue=1, offvalue=0,
            command=print_selection).place(x=445, y=721)


Checkbutton(Billify, bg='#004aad', fg='Black', variable=P2, onvalue=1, offvalue=0,
            command=print_selection).place(x=560, y=540)
Checkbutton(Billify, bg='#004aad', fg='Black', variable=P3, onvalue=1, offvalue=0,
            command=print_selection).place(x=560, y=580)

#Tax_type widgets
Tax_Type_options = ["National", "State"]
Tax_Type.set("State")
O1 = OptionMenu(Billify, Tax_Type, *Tax_Type_options)
O1.config(bg='#004aad', fg="WHITE", font=('helvetica', 16))
O1.place(x=770, y=353)

# function to convert numbers to words
def number_to_word(number):
    def get_word(n):
        words = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
                 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty",
                 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninty"}
        if n <= 20:
            return words[n]
        else:
            ones = n % 10
            tens = n - ones
            return words[tens] + " " + words[ones]

    def get_all_word(n):
        d = [100, 10, 100, 100]
        v = ["", "Hundred And", "Thousand", "lakh"]
        w = []
        for i, x in zip(d, v):
            t = get_word(n % i)
            if t != "":
                t += " " + x
            w.append(t.rstrip(" "))
            n = n // i
        w.reverse()
        w = ' '.join(w).strip()
        if w.endswith("And"):
            w = w[:-3]
        return w

    arr = str(number).split(".")
    number = int(arr[0])
    crore = number // 10000000
    number = number % 10000000
    word = ""
    if crore > 0:
        word += get_all_word(crore)
        word += " crore "
    word += " Rupees " + get_all_word(number).strip() + " Only "
    if len(arr) > 1:
        if len(arr[1]) == 1:
            arr[1] += "0"
        word += "  " + get_all_word(int(arr[1]))
    return word

# function to add details into database
def add_into_database(invoice_no, date, buyer_name, tax_type, amount):
    import mysql.connector

    # Database connection
    mydb = mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12752241",
        password="CjGCEVyIFC",
        database="sql12752241"
    )
    mycursor = mydb.cursor()

    # Creating table (ensure this runs at least once to set up the table)
    # studentRecord = "CREATE TABLE IF NOT EXISTS Invoice_details( Invoice_no INT PRIMARY KEY ,Date VARCHAR(13),Buyers_name VARCHAR(30),Tax_Type VARCHAR(12),Amount VARCHAR(10))"

    # SQL query
    sql_query = """
    INSERT INTO Invoice_details (Invoice_no, Date, Buyers_name, Tax_Type, Amount)
    VALUES (%s, %s, %s, %s, %s)
    """

    val = (invoice_no, date, buyer_name, tax_type, amount)

    # Execute and commit
    try:
        mycursor.execute(sql_query, val)
        mydb.commit()
        print("Record Inserted Successfully")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        mydb.close()

# function to Generate Invoice
def generate_invoice():
      # pdf initialization
      pdf = FPDF('P', 'mm', 'A4')

      # CREATING INVOICE PDF

      pdf.add_page()
      pdf.set_auto_page_break(auto=True, margin=5)

      # LINES AND BORDER

      pdf.set_line_width(0.6)
      pdf.rect(80, 5, 50, 10)
      pdf.rect(5, 15, 200, 50)
      pdf.rect(5, 65, 100, 30)
      pdf.rect(105, 65, 100, 30)
      pdf.rect(5, 95, 100, 10)
      pdf.rect(105, 95, 100, 10)
      pdf.rect(5, 105, 100, 40)
      pdf.rect(105, 105, 100, 40)
      pdf.rect(5, 145, 10, 10)
      pdf.rect(15, 145, 65, 10)
      pdf.rect(80, 145, 25, 10)
      pdf.rect(105, 145, 25, 10)
      pdf.rect(130, 145, 25, 10)
      pdf.rect(155, 145, 50, 10)

      pdf.rect(5, 155, 10, 40)
      pdf.rect(15, 155, 65, 40)
      pdf.rect(80, 155, 25, 40)
      pdf.rect(105, 155, 25, 40)
      pdf.rect(130, 155, 25, 40)
      pdf.rect(155, 155, 50, 40)


      pdf.rect(5, 195, 10, 8)
      pdf.rect(15, 195, 65, 8)
      pdf.rect(80, 195, 25, 8)
      pdf.rect(105, 195, 50, 8)
      pdf.rect(155, 195, 50, 8)

      pdf.rect(5, 203, 100, 45)
      pdf.rect(105, 203, 100, 45)
      pdf.rect(5, 248, 200, 10)
      pdf.rect(105, 258, 100, 35)
      pdf.rect(5, 258, 100, 35)

      pdf.line(105, 211.75, 205, 211.75)
      pdf.line(105, 220.50, 205, 220.50)
      pdf.line(105, 229.25, 205, 229.25)
      pdf.line(105, 238.00, 205, 238.00)
      pdf.line(155, 203.00, 155, 248.00)

      #Calculations

      Total_amount = int(Amount1.get())

      if P2.get() == 1 :
          Total_amount += int(Amount2.get())
      if P3.get() == 1 :
          Total_amount += int(Amount3.get())

      if Tax_Type.get() == "State":
          TAX = round(float(Total_amount) * 0.025)
          GVT = str((TAX * 2) + float(Total_amount))
      else:
          TAX = round(float(Total_amount) * 0.05)
          GVT = str(TAX + int(Total_amount))

      n2w = number_to_word(GVT)

      # Writing into pdf
      pdf.set_font("Arial", 'B', size=15)

      pdf.cell(ln=0, align='C', w=0, h=1, txt="TAX INVOICE")
      pdf.cell(ln=1, w=0, h=10, txt="")
      pdf.cell(ln=1, w=0, h=1, txt="")

      pdf.set_font("Arial", 'B', size=25)

      pdf.cell(ln=1, align='C', w=0, h=10, txt="[Company Name]") # Change the Name to your Company Name
      pdf.cell(ln=1, w=0, h=1, txt="")

      pdf.set_font("Arial", 'B', size=13)

      pdf.cell(ln=1, align='C', w=0, h=10, txt="Address")  # <----------------- Enter your Address
      pdf.cell(ln=2, align='C', w=0, h=1, txt="Taluk , District")  # <--------- Enter your Taluk,District
      pdf.cell(ln=2, align='C', w=0, h=10, txt="State. PH | 1234567890 |") # <- Enter your State, Change the Phone Number
      pdf.cell(ln=2, align='C', w=0, h=1, txt="GST TIN:XXX123YYY456ZZ") # <-- Enter your GST TIN

      # Invoice  Details and Transporter's Details

      pdf.set_font("helvetica", 'B', size=10)
      pdf.cell(ln=1, w=0, h=1, txt="        ")
      pdf.cell(ln=1, w=0, h=10, txt="        ")
      pdf.cell(ln=1, w=0, h=1, txt="        ")
      pdf.cell(30, 10, txt='INVOICE')
      pdf.cell(10, 10, txt=':', align="L")
      pdf.cell(60, 10, txt=Invoice.get(), align="L")
      pdf.cell(45, 10, txt='TRANSPORTER')
      pdf.cell(5, 10, txt=':')
      pdf.cell(50, 10, txt=Transporter.get(), align="L", ln=True)
      pdf.cell(30, 1, txt='DATE')
      pdf.cell(10, 1, txt=':', align='L')
      pdf.cell(60, 1, txt=Date.get())
      pdf.cell(45, 1, txt='VEHICLE NO')
      pdf.cell(5, 1, txt=':')
      pdf.cell(50, 1, txt=Vehicle.get(), align="L", ln=True)
      pdf.cell(30, 10, txt='EWAY BILL NO ')
      pdf.cell(10, 10, txt=':', align="L")
      pdf.cell(60, 10, txt=Eway_bill.get())
      pdf.cell(45, 10, txt='LR NO')
      pdf.cell(5, 10, txt=':')
      pdf.cell(50, 10, txt=LR_No.get(), align='L', ln=True)
      pdf.cell(50, 1, txt='')
      pdf.cell(50, 1, txt='')
      pdf.cell(45, 1, txt="TRANSPORTER'S GSTIN")
      pdf.cell(5, 1, txt=":")
      pdf.cell(50, 1, txt=Trans_Gst.get(), align='L', ln=True)

      # Biller Details and Shipper Details

      pdf.cell(ln=1, w=0, h=10, txt="        ")

      pdf.set_font("helvetica", 'B', size=13)

      pdf.cell(w=100, h=5, txt="BUYER ( Billing Address : )")
      pdf.cell(w=100, h=5, txt="Shipping Address :  ")

      pdf.cell(ln=1, w=0, h=10, txt="        ")

      pdf.cell(100, 10, txt=Buyer_Name.get())
      if same == 1:
          pdf.cell(100, 10, txt=Buyer_Name.get(), ln=True)
      else:
          pdf.cell(100, 10, txt=Ship_to.get(), ln=True)

      pdf.set_font("helvetica", 'B', size=10)

      pdf.cell(100, 1, txt=Address_1.get())
      if same == 1:
          pdf.cell(100, 1, txt=Address_1.get(), ln=True)
      else:
          pdf.cell(100, 1, txt=S_Address_1.get(), ln=True)

      pdf.cell(100, 10, txt=Address_2.get())
      if same == 1:
          pdf.cell(100, 10, txt=Address_2.get(), ln=True)
      else:
          pdf.cell(100, 10, txt=S_Address_2.get(), ln=True)

      pdf.cell(100, 1, txt=Address_3.get())
      if same == 1:
          pdf.cell(100, 1, txt=Address_3.get(), ln=True)
      else:
          pdf.cell(100, 1, txt=S_Address_3.get(), ln=True)

      pdf.cell(100, 10, txt=Address_4.get())
      if same == 1:
          pdf.cell(100, 10, txt=Address_4.get(), ln=True)
      else:
          pdf.cell(100, 10, txt=Address_4.get(), ln=True)

      pdf.cell(100, 1, txt="GSTIN : " + Buyer_gst.get())
      if same == 1:
          pdf.cell(100, 1, txt="GSTIN : " + Buyer_gst.get(), ln=True)
      else:
          pdf.cell(100, 1, txt="GSTIN : " + Ship_gst.get(), ln=True)

      # PRODUCT DETAIL

      pdf.cell(ln=1, w=0, h=2, txt="        ")

      pdf.set_font('Arial', 'B', size=10)

      pdf.cell(5, 9, txt="")
      pdf.cell(65, 10, txt="PRODUCT",align="C")
      pdf.cell(25, 10, txt="HSN.CODE",align="C")
      pdf.cell(25, 9, txt="NO.OF",align="C")
      pdf.cell(25, 9, txt="RATE PER",align="C")
      pdf.cell(50, 9, txt="AMOUNT",align="C",ln=1)

      pdf.cell(5, 1, txt="")
      pdf.cell(65, 0, txt="")
      pdf.cell(25, 0, txt="")
      pdf.cell(25, 1, txt="QUANTITY",align="C")
      pdf.cell(25, 1, txt="QUANTITY",align="C")
      pdf.cell(50, 1, txt="",ln=1)

      # User PRODUCT DETAILS

      pdf.cell(5, 10, txt="1.")
      pdf.cell(65, 10, txt=Product1.get())
      pdf.cell(25, 10, txt=Hsn_Code1.get(), align="C")
      pdf.cell(25, 10, txt=Quantity1.get(), align="C")
      pdf.cell(25, 10, txt=rate_per_quantity1.get(), align="C")
      pdf.cell(40, 10, txt=Amount1.get(), align="R", ln=1)

      if P2.get() == 1:
          pdf.cell(5, 1, txt="2.")
          pdf.cell(65, 1, txt=Product2.get())
          pdf.cell(25, 1, txt=Hsn_Code2.get(), align="C")
          pdf.cell(25, 1, txt=Quantity2.get(), align="C")
          pdf.cell(25, 1, txt=rate_per_quantity2.get(), align="C")
          pdf.cell(40, 1, txt=Amount2.get(), align="R", ln=1)
      else:
          pdf.cell(5, 1, txt="",ln=1)

      if P3.get() == 1:
          pdf.cell(5, 10, txt="3.")
          pdf.cell(65, 10, txt=Product3.get())
          pdf.cell(25, 10, txt=Hsn_Code3.get(), align="C")
          pdf.cell(25, 10, txt=Quantity3.get(), align="C")
          pdf.cell(25, 10, txt=rate_per_quantity3.get(), align="C")
          pdf.cell(40, 10, txt=Amount3.get(), align="R", ln=1)
      else:
          pdf.cell(5, 10, txt="",ln=1)

      pdf.cell(w=0, h=20, txt='',ln=1)

      pdf.cell(5, 10, txt="")
      pdf.cell(65, 10, txt="")
      pdf.cell(25, 10, txt="")
      pdf.cell(50, 10, txt="            TOTAL AMOUNT :",align="C")
      pdf.cell(40, 10, txt=str(Total_amount), align="R",ln=1)

      # Bank Details and GST

      # GST

      pdf.set_font("helvetica", 'B', size=13)

      pdf.cell(95, 8, txt="COMPANY BANK DETAIL'S:")

      pdf.set_font('Arial', 'B', size=10)

      pdf.cell(65, 8, txt="    AMOUNT BEFORE TAX :")
      pdf.cell(25, 8, txt=str(Total_amount), align="R", ln=True)

      pdf.cell(95, 10, txt="BANK NAME  : Bank of India")   # <----- Change to your Bank
      pdf.cell(65, 10, txt="CGST 2.5%", align="C")

      if Tax_Type.get() == "State":
          pdf.cell(25, 9, txt=str(round(float(TAX))), align="R", ln=True)
      else:
          pdf.cell(35, 9, txt="-", align="C", ln=True)

      pdf.cell(95, 9, txt="BANK BRANCH: Coimbatore")  # <--------------- Enter your Branch
      pdf.cell(65, 9, txt="SGST 2.5%", align="C")

      if Tax_Type.get() == 'State':
          pdf.cell(25, 9, txt=str(round(float(TAX))), align="R", ln=True)
      else:
          pdf.cell(35, 9, txt="-", align="C", ln=True)

      pdf.cell(95, 9, txt="ACCOUNT NO : 0000000000") # <------------ Enter your Account Number
      pdf.cell(65, 9, txt="IGST   5%", align="C")

      if Tax_Type.get() == "National":

          pdf.cell(25, 9, txt=str(round(float(TAX))), align="R", ln=True)
      else:
          pdf.cell(35, 9, txt="-", align="C", ln=True)

      pdf.cell(95, 9, txt="IFSC CODE  : XXX123456") # <------------- Enter your IFSC Code
      pdf.cell(65, 9, txt=" GRAND TOTAL AMOUNT :")
      pdf.cell(25, 8, txt=str(round(float(GVT))), align="R", ln=True)

      pdf.set_font("helvetica", 'B', size=11)
      pdf.cell(40, 12, txt="AMOUNT IN WORDS :  ")
      pdf.set_font("helvetica", 'B', size=10)
      pdf.cell(160, 12, txt=n2w, ln=1)

      # Disclaimer and SRI KUMARAN MILLS

      pdf.set_font("helvetica", 'U', size=12)
      pdf.cell(100, 10, txt="Declaration")
      pdf.set_font("helvetica", 'B', size=11)
      pdf.cell(100, 10, txt="For [Company's Name]", align='L', ln=1)  # <------ Company Name
      pdf.set_font("helvetica", 'B', size=10)
      pdf.cell(100, 1, txt="We declare that this invoice shows the ")
      pdf.cell(100, 1, txt="", ln=1)
      pdf.cell(100, 10, txt="actual price of the goods described and  ")
      pdf.cell(100, 10, txt="", ln=1)
      pdf.cell(100, 1, txt="that all particulars are true and correct.")
      pdf.cell(100, 8, txt="", ln=1)
      pdf.cell(100, 1, txt="THIS IS A COMPUTER GENERATED INVOICE")
      pdf.cell(90, 1, txt="Authorised Signatory", align='R', ln=1)

      # Save PDF dynamically based on Invoice Number
      pdf.output(f"invoice_{Invoice.get()}.pdf")


      # Automatically open the generated PDF
      if platform.system() == "Windows":
          os.startfile(f"invoice_{Invoice.get()}.pdf")
      elif platform.system() == "Darwin":  # macOS
          subprocess.call(["open", f"invoice_{Invoice.get()}.pdf"])
      else:  # Linux or other OS
          subprocess.call(["xdg-open", f"invoice_{Invoice.get()}.pdf"])

      # Saves data in database
      add_into_database(int(Invoice.get()),Date.get(),Buyer_Name.get(),Tax_Type.get(),str(round(float(GVT))))

Button(Billify, text="Click Here to Generate INVOICE", command=generate_invoice).place(x=1135, y=100)

# Run the application
Billify.mainloop()
