# certificate_gen_emailer
# 🎓 Certificate Generation & Email Automation (Flask)

A complete **Flask web application** to generate personalized certificates from an Excel sheet, preview them live with adjustable positioning, convert them into PDFs, and send them automatically via **Gmail with HTML email templates and attachments**.

---

## 🚀 Features

### 📤 Upload Module
- Upload **Certificate Image** (PNG/JPG)
- Upload **Excel file** with participant details
  - `Name`
  - `Email`

### 🎯 Live Adjustment
- Live **X & Y coordinate adjustment**
- **Font size** increase/decrease
- **Font color picker**
- Real‑time preview on certificate
- Default font: **Times New Roman**

### 👀 Preview & PDF Generation
- Generates certificates for all participants
- Shows preview image with respective email
- Automatically converts each certificate into **PDF**

### 📧 Email Automation
- Custom **Email Subject input**
- Uses **HTML Email Template**
- Attaches participant’s **certificate PDF**
- Custom **Sender Name**
- Gmail **App Password authentication**

### 📊 Status & Reports
- Displays sent / failed email status
- Shows error reason if failed
- Generates downloadable **Excel report**

---

## 🧱 Project Structure
```
certificate/
│
├── app.py
├── README.md
│
├── templates/
│   ├── upload.html
│   ├── adjust.html
│   ├── preview.html
│   ├── email.html
│   ├── status.html
│   └── email_template.html
│
├── static/
│   ├── live_preview.png
│   └── generated/
│
├── uploads/
│   └── certificate.png
│
├── certificates/
│   └── pdf/
│
├── reports/
│   └── email_report.xlsx
│
├── TimesNewRoman.ttf
└── requirements.txt

```
---

## 📄 Excel File Format

Your Excel file **must contain these columns**:

| Name | Email |
|------|-------|
| John Doe | john@gmail.com |

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install flask pillow pandas reportlab
Python version:

nginx
Copy code
Python 3.10+
🔐 Gmail App Password Setup
Go to Google Account → Security

Enable 2‑Step Verification

Open App Passwords

Select:

App: Mail

Device: Other

Copy the 16‑character App Password

Update in app.py:

python
Copy code
EMAIL = "yourgmail@gmail.com"
PASSWORD = "your_app_password"
▶️ How to Run
bash
Copy code
python app.py
Open in browser:

cpp
Copy code
http://127.0.0.1:5000/
🔄 Application Flow
Upload certificate image + Excel

Adjust name position, font size & color live

Preview generated certificates

Enter email subject

Send emails with PDF attachments

Download email status report

📧 Email Template
Uses email_template.html

Supports:

Drive‑hosted logos

Dynamic name ({{name}})

Professional styling

PDF attachment mention

✅ Output
Personalized Certificate PDFs

Automated Bulk Email Sending

Excel Report with:

Email

Status (Sent / Failed)

Error reason

🧑‍💻 Author
Developed for Event Certificate Automation & Bulk Emailing
