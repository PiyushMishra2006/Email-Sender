# 📧 Python Email Sender

A professional desktop Email Sender application built with **Python** and **Tkinter**. This application allows users to send emails with a modern graphical interface, support for multiple recipients, file attachments, and customizable HTML email templates.

---

## 🚀 Features

- 📨 Send emails using Gmail SMTP
- ✅ Email address validation
- 👥 Send emails to multiple recipients
- 📎 Attach files to emails
- 🖥️ User-friendly Tkinter GUI
- 🎨 Send professionally formatted HTML emails
- 📂 Multiple email templates
  - Welcome
  - Interview Invitation
  - Newsletter
- 🔽 Template selection using a dropdown menu
- ⚠️ Error handling and status updates

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- SMTP (`smtplib`)
- EmailMessage (`email.message`)
- HTML & CSS
- Regular Expressions (Regex)

---

## 📁 Project Structure

```
Email Sender/
│
├── attachments/
├── templates/
│   ├── welcome.html
│   ├── interview.html
│   └── newsletter.html
│
├── email_sender.py
├── email_sender_gui.py
├── README.md
```

---

## ⚙️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Email-Sender.git
```

2. Open the project folder.

3. Run the application:

```bash
python email_sender_gui.py
```

4. Enter:
   - Sender Email
   - Gmail App Password
   - Receiver Email(s)
   - Subject
   - Body
   - Select an Email Template
   - (Optional) Attach a file

5. Click **Send**.

---

## 📌 Future Improvements

- Email Scheduler
- SQLite Email History
- Export Sent Email Logs
- Dark Mode
- Executable (.exe) Packaging

---

## ⭐ Support

If you found this project helpful, consider giving the repository a ⭐ on GitHub!
