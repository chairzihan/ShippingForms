import win32com.client as win32
import time

def draft_email():
    outlook = win32.Dispatch('outlook.application')

    mail = outlook.CreateItem(0)

    mail.To = "andrew.cameron@nokia.com"
    mail.Subject = "Test email (drafted using Python)"
    mail.Body = "Hello Andrew from Python!"

    # mail.Attachments.Add("C:\\path\\to\\attachment.pdf")

    # display the email in Outlook
    mail.Display()

    # time.sleep(5)




if __name__ == "__main__":
    print("## Running outlook_draft_test.py ##")
    draft_email()