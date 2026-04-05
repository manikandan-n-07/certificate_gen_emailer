<div align="center">

<img src="https://img.icons8.com/fluency/100/certificate.png" alt="CertMailer Logo" width="100" height="100"/>

# Certificate Generater And Mailer

### *Bulk Certificate Generator & Emailer — One Click, Every Certificate Delivered*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_App-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Author](https://img.shields.io/badge/Author-Manikandan_N-ff6b6b?style=for-the-badge&logo=github)](https://github.com/manikandan-n-07)

</div>

---

## Table of Contents

- [What is Certificate Generater And Mailer?](#what-is-certificate-generater-and-mailer)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [How to Use](#how-to-use)
- [Excel Format](#excel-format)
- [Configuration](#configuration)
- [Security Notes](#security-notes)
- [Contributing](#contributing)
- [Author](#author)

---

## What is Certificate Generater And Mailer?

**CertMailer** is a powerful, easy-to-use web application that automates the entire certificate generation and distribution pipeline. Upload your certificate template, provide an Excel sheet of participants, visually position names with a live preview, generate personalized PDF certificates, and bulk-email them — all from a single browser interface.

> *"From spreadsheet to inbox — every certificate, perfectly delivered."*

---

## Features

| Feature | Description |
|---|---|
| 📤 **Excel Upload** | Import participant names and emails from any `.xlsx` spreadsheet |
| 🖼️ **Certificate Template Upload** | Use your own PNG certificate design as the base template |
| 🎯 **Live Name Positioning** | Drag and adjust name placement with real-time visual preview — no guesswork |
| 🎨 **Font Customization** | Control font size and text color to perfectly match your certificate design |
| 👁️ **Bulk Preview** | Review all generated certificates with personalized names before sending |
| 📄 **PDF Generation** | Automatically converts each certificate to a high-resolution A3 PDF |
| 📧 **Bulk Email Sending** | Sends personalized HTML emails with PDF certificates attached via Gmail SMTP |
| 📊 **Email Status Report** | Download a full `.xlsx` report of sent/failed emails after each campaign |
| ✉️ **Custom Email Template** | Customize the HTML email body with a `{{name}}` placeholder for personalization |

---

## Tech Stack

```
Backend          →  Python 3 · Flask
Image Processing →  Pillow (PIL)
PDF Generation   →  ReportLab
Data Handling    →  Pandas · openpyxl
Email Delivery   →  smtplib · Gmail SMTP SSL
Frontend         →  HTML5 · Jinja2 Templates
Font             →  Times New Roman (bundled TTF)
```

---

## Project Structure

```
certificate_gen_emailer/
│
├── app.py                      # Core Flask application logic
├── requirements.txt            # Python dependencies
├── TimesNewRoman.ttf           # Bundled font for certificate text
│
├── templates/
│   ├── upload.html             # Step 1 — Upload Excel & certificate image
│   ├── adjust.html             # Step 2 — Live name position adjustment
│   ├── preview.html            # Step 3 — Preview all generated certificates
│   ├── email.html              # Step 4 — Compose & send emails
│   ├── email_template.html     # HTML email body template (customizable)
│   └── status.html             # Step 5 — Email delivery status report
│
├── static/
│   ├── live_preview.png        # Live preview image (auto-generated)
│   └── generated/             # Generated certificate images (per session)
│
├── uploads/
│   └── certificate.png         # Uploaded certificate template
│
├── certificates/
│   └── pdf/                   # Generated PDF certificates (per participant)
│
└── reports/
    └── email_report.xlsx       # Email delivery status export
```

---

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- A Gmail account with **App Password** enabled (2FA required)
- An Excel file (`.xlsx`) with participant `Name` and `Email` columns
- A PNG certificate template image

### 1. Clone the Repository

```bash
git clone https://github.com/manikandan-n-07/certificate_gen_emailer.git
cd certificate_gen_emailer
```

### 2. Install Dependencies

```bash
pip install flask pillow pandas reportlab
```

### 3. Configure Gmail Credentials

Open `app.py` and update the config section at the top:

```python
# ================= CONFIG =================
EMAIL       = "yourgmail@gmail.com"      # Your Gmail address
PASSWORD    = "your_app_password"        # Gmail App Password (NOT your login password)
SENDER_NAME = "Your Name or Org"        # Display name shown to recipients
FONT_PATH   = "TimesNewRoman.ttf"       # Font used to write names on certificates
```

> ⚠️ **Important:** Use a [Gmail App Password](https://support.google.com/accounts/answer/185833), not your regular Gmail password. Enable 2-Step Verification first, then generate an App Password under your Google Account settings.

### 4. Run the Application

```bash
python app.py
```

Open your browser and go to:
```
http://127.0.0.1:5000
```

---

## How to Use

The app follows a simple **5-step workflow**:

**Step 1 — Upload**
- Upload your Excel file (`.xlsx`) containing participant data.
- Upload your certificate template as a PNG image.
- Click **Next → Adjust**.

**Step 2 — Adjust**
- Use the live adjustment panel to set the **X position**, **Y position**, **font size**, and **text color**.
- The preview updates in real-time so you can see exactly where the name will appear.
- Click **Generate Preview** when satisfied.

**Step 3 — Preview**
- Browse through all generated certificates with personalized names.
- Each certificate is shown as a PNG thumbnail.
- Click **Proceed to Email** when ready.

**Step 4 — Email**
- Enter the **email subject** line.
- Customize `templates/email_template.html` beforehand with your desired message body (use `{{name}}` for personalized greeting).
- Click **Send All** to dispatch certificates.

**Step 5 — Status Report**
- View the delivery status for each recipient (Sent / Failed).
- Click **Download Report** to export the results as an `.xlsx` file.

---

## Excel Format

Your Excel file must have at least these two columns (exact column names required):

| Name | Email |
|---|---|
| Lunar | lunar@example.com |
| Mani | mani@example.com |
| Manilunar | manilunar@example.com |

> Column headers must be exactly `Name` and `Email` (case-sensitive).

---

## Configuration

| Variable | Location | Description |
|---|---|---|
| `EMAIL` | `app.py` | Gmail address used to send certificates |
| `PASSWORD` | `app.py` | Gmail App Password for SMTP authentication |
| `SENDER_NAME` | `app.py` | Display name shown in recipient's inbox |
| `FONT_PATH` | `app.py` | Path to the TTF font used on certificates |
| `X, Y` | `app.py` | Default starting coordinates for name placement |
| `FS` | `app.py` | Default font size for certificate names |
| `COLOR` | `app.py` | Default text color as RGB tuple |
| Email Body | `templates/email_template.html` | HTML body of the email; use `{{name}}` for recipient's name |

---

## Security Notes

- **Never commit** your Gmail credentials to a public repository. Use environment variables or a `.env` file for production use.
- Gmail App Passwords are specific to each app — revoke them anytime from your Google Account security settings.
- Consider adding a `.gitignore` to exclude `uploads/`, `certificates/`, `reports/`, and `static/generated/` folders from version control.

```gitignore
uploads/
certificates/
reports/
static/generated/
*.env
```

---

## Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes
git commit -m "Add: your feature description"

# 4. Push and open a Pull Request
git push origin feature/your-feature-name
```

Ideas for contribution: support for multiple fonts, DOCX/image certificate output, progress bar during bulk send, ZIP download of all PDFs, email preview before sending.

---

## Author

<div align="center">

# Manikandan N

*Full Stack Developer & Creator of Certificte Generator And Mailer*

[![GitHub](https://img.shields.io/badge/GitHub-@manikandan--n--07-181717?style=flat-square&logo=github)](https://github.com/manikandan-n-07)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Manikandan_N-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/manikandan-n-35a1bb294)
[![Email](https://img.shields.io/badge/Email-manilunar07@gmail.com-D14836?style=flat-square&logo=gmail)](mailto:maniluna07@gmail.com)

</div>

---
