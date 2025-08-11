import win32com.client as win32
import time

def draft_email(email):
    outlook = win32.Dispatch('outlook.application')

    mail = outlook.CreateItem(0)

    mail.To = email
    mail.Subject = "Module Shipping"
    mail.Body = "The excel file for a shipment of PON modules is attached to this e-mail."

    # mail.Attachments.Add("C:\\path\\to\\attachment.pdf")

    # display the email in Outlook
    mail.Display()

    # time.sleep(5)
