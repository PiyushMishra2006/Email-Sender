import smtplib
from email.message import EmailMessage
import mimetypes
import os

#Validation email function
def is_valid_email(email):
    return '@' in email and '.' in email

#Attach File Function
def attach_file(email,file_path):
    with open(file_path,"rb") as file:
        file_data = file.read()

        mime_type,_ = mimetypes.guess_type(file_path)
        if mime_type is None:
            mime_type = "application/octet-stream"

        maintype,subtype = mime_type.split('/')
        email.add_attachment(
            file_data,
            maintype=maintype,
            subtype=subtype,
            filename = os.path.basename(file_path)
        )

#Email Sending Function
def send_email(sender_email,app_password,receiver_email,subject,body,file_path,template_name):
    #Email preparation
    email = EmailMessage()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject
    email.set_content(body)
    with open(f"templates/{template_name}.html","r",encoding="utf-8") as file :
        html_body = file.read()
    html_body = html_body.replace("{{subject}}",subject)
    html_body = html_body.replace("{{body}}",body)
    html_body = html_body.replace("{{name}}",receiver_email.split('@')[0])
    email.add_alternative(html_body,subtype="html")
    if file_path:
        try:
            attach_file(email, file_path)
        except Exception as e:
            print("Attachment Error:", e)
            return
        else:
            print("No Attachment will be sent")
    try :
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login(sender_email,app_password)
            smtp.send_message(email)
            return True,"Email sent successfully"
    except Exception as e:
        return False,str(e)
