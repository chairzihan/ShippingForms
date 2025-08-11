
import win32com.client




def print_excel(filepath, printer_name="Nokia Secure Print"):
    try:
        print(f"Attempting to print to '{printer_name}'")

        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = False  # Keep hidden during the process

        workbook = excel.Workbooks.Open(filepath)

        # Print the workbook
        workbook.PrintOut()

        workbook.Close(SaveChanges=False)
        excel.Quit()

        print(f"The file '{filepath}' was successfully sent to '{printer_name}'.")
    except Exception as e:
        print(f"The following error occurred during printing: {e}")



print_excel(r"C:\Users\clzhong\.shippingForms\.formFiles\Shipping_Request_20250730_090840.xlsm")