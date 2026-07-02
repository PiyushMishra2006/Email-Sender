import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
from email_sender import send_email,is_valid_email

root = tk.Tk()
#Root Info
root.title("Email Sender")
root.geometry("600x600")
heading = tk.Label(root,text="Email Sender",font=("Arial",20,"bold"))
heading.pack(pady=20)
#Sender Email Input
sender_label = tk.Label(root,text="Sender Email: ")
sender_label.pack()
sender_entry = tk.Entry(root,width=40)
sender_entry.pack(pady=5)
#App Password Input
password_label = tk.Label(root,text="App Password: ")
password_label.pack()
password_entry = tk.Entry(root,width=40,show="*")
password_entry.pack(pady=5)
#Recipient Email Input
recipient_label = tk.Label(root,text="Recipient Email: ")
recipient_label.pack()
recipient_entry = tk.Entry(root,width=40)
recipient_entry.pack(pady=5)
#Subject Input
subject_label = tk.Label(root,text="Subject: ")
subject_label.pack(pady=5)
subject_entry = tk.Entry(root,width=40)
subject_entry.pack(pady=5)
#Template drop down
tk.Label(root,text="Template").pack()
template_var = tk.StringVar()
template_var.set("welcome")
template_dropdown = ttk.Combobox(
    root,
    textvariable=template_var,
    values=["welcome","newsletter","interview"],
    state="readonly"
)
template_dropdown.pack(pady=5)
#Message Input
message_label = tk.Label(root,text="Message: ")
message_label.pack(pady=5)
message_text = tk.Text(root,width=40,height=8)
message_text.pack(pady=5)

file_path = ""
attachment_label = tk.Label(root,text="No File Selected")
attachment_label.pack()
def browse_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path : 
        attachment_label.config(text=os.path.basename(file_path))
    else :
        attachment_label.config(text="No File Selected")

browse_button = tk.Button(root,text="Browse Attachment",command=browse_file)
browse_button.pack(pady=10)

def send():
    status_label.config(text="Status: Sending...")
    send_button.config(state="disabled")
    sender_email = sender_entry.get()
    app_password = password_entry.get()
    receiver_email = recipient_entry.get()
    subject = subject_entry.get()
    body = message_text.get("1.0",tk.END)
    template_name = template_var.get()

    if not is_valid_email(sender_email):
        messagebox.showerror("Invalid Email","Please Enter a valid sender email address.")
        status_label.config(text="Status: Ready")
        send_button.config(state="normal")
        return
    if not is_valid_email(receiver_email):
        messagebox.showerror("Invalid Email","Please Enter a valid receiver email address.")
        status_label.config(text="Status: Ready")
        send_button.config(state="normal")
        return 
    success,message = send_email(sender_email,app_password,receiver_email,subject,body,file_path,template_name)
    if success:
        status_label.config(text="Status: Email Sent!")
        messagebox.showinfo("Success",message)
    else:
        status_label.config(text="Status: Failed!")
        messagebox.showerror("Error",message)
    send_button.config(state="normal")


def clear_fields():
    global file_path
    sender_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
    recipient_entry.delete(0,tk.END)
    subject_entry.delete(0,tk.END)
    message_text.delete("1.0",tk.END)
    file_path = ""
    attachment_label.config(text="No Files Selected")
    status_label.config(text="Status: Ready")

status_label = tk.Label(root,text="Status: Ready")
status_label.pack(pady=5)
send_button = tk.Button(root,text="Send Email",command=send)
send_button.pack(pady=10)

clear_button = tk.Button(root,text="Clear",command=clear_fields)
clear_button.pack(pady=5)
root.mainloop()