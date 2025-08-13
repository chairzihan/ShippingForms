import win32com.client as win32
import time

def draft_email(email, attachment):
    outlook = win32.Dispatch('outlook.application')

    mail = outlook.CreateItem(0)

    mail.To = email
    mail.Subject = "Module Shipping"
    mail.Body = "The excel file for a shipment of PON modules is attached to this e-mail."

    mail.Attachments.Add(attachment)

    # display the email in Outlook
    mail.Display()

    # time.sleep(5)


if __name__ == "__main__":
    print("## Running outlook_draft_test.py ##")
    draft_email("something@gmail.com", r"C:\Users\clzhong\.shippingForms\.formFiles\Shipping_Request_20250812_135115.xlsm")