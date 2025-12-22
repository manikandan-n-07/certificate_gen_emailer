from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
import pandas as pd
import os, smtplib
from email.message import EmailMessage

app = Flask(__name__)

# ================= CONFIG =================
EMAIL = "yourgmail@gmail.com"
PASSWORD = "your_app_password"    # Gmail App Password
SENDER_NAME = "sender_name"
FONT_PATH = "TimesNewRoman.ttf"

# ================= STATE ==================
data = []
people = []

X, Y, FS = 1750, 1300, 90
COLOR = (0, 0, 0)

# ================= ROUTES =================

@app.route("/")
def upload():
    return render_template("upload.html")

@app.route("/adjust", methods=["POST"])
def adjust():
    global data

    os.makedirs("uploads", exist_ok=True)
    request.files["certificate"].save("uploads/certificate.png")

    df = pd.read_excel(request.files["excel"])
    data = df.to_dict("records")

    generate_live_preview(X, Y, FS, COLOR)
    return render_template("adjust.html", x=X, y=Y, fs=FS)

@app.route("/live")
def live():
    global X, Y, FS, COLOR

    X = int(request.args["x"])
    Y = int(request.args["y"])
    FS = int(request.args["fs"])

    hex_color = request.args.get("color", "#000000")
    COLOR = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

    generate_live_preview(X, Y, FS, COLOR)
    return "", 204

@app.route("/preview", methods=["POST"])
def preview():
    global people
    people = []

    os.makedirs("static/generated", exist_ok=True)
    os.makedirs("certificates/pdf", exist_ok=True)

    for i, p in enumerate(data):
        name = p["Name"]
        email = p["Email"]

        img = Image.open("uploads/certificate.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT_PATH, FS)

        draw.text((X, Y), name, fill=COLOR, font=font)

        img_path = f"static/generated/{i}.png"
        img.save(img_path)

        pdf_path = f"certificates/pdf/{name}.pdf"
        c = canvas.Canvas(pdf_path, pagesize=(3508, 2480))
        c.drawImage(img_path, 0, 0, 3508, 2480)
        c.save()

        people.append({
            "name": name,
            "email": email,
            "preview": f"{i}.png",
            "pdf": pdf_path
        })

    return render_template("preview.html", people=people)

@app.route("/email")
def email():
    return render_template("email.html")

@app.route("/send", methods=["POST"])
def send():
    subject = request.form["subject"]

    with open("templates/email_template.html", "r", encoding="utf-8") as f:
        html_template = f.read()

    results = []
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(EMAIL, PASSWORD)

    for p in people:
        try:
            msg = EmailMessage()
            msg["From"] = f"{SENDER_NAME} <{EMAIL}>"
            msg["To"] = p["email"]
            msg["Subject"] = subject

            html_body = html_template.replace("{{name}}", p["name"])
            msg.set_content("Please view this email in HTML format.")
            msg.add_alternative(html_body, subtype="html")

            with open(p["pdf"], "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="pdf",
                    filename=f"{p['name']}.pdf"
                )

            smtp.send_message(msg)
            results.append({"Email": p["email"], "Status": "Sent", "Reason": ""})

        except Exception as e:
            results.append({"Email": p["email"], "Status": "Failed", "Reason": str(e)})

    smtp.quit()

    os.makedirs("reports", exist_ok=True)
    pd.DataFrame(results).to_excel("reports/email_report.xlsx", index=False)

    return render_template("status.html", results=results)

@app.route("/download")
def download():
    return send_file("reports/email_report.xlsx", as_attachment=True)

# ================= HELPER =================

def generate_live_preview(x, y, fs, color):
    img = Image.open("uploads/certificate.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, fs)
    draw.text((x, y), "Sample Name", fill=color, font=font)
    img.save("static/live_preview.png")

# ================= RUN ====================

if __name__ == "__main__":
    app.run(debug=True)
