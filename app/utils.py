import random
import os
from flask_mail import Message
from fpdf import FPDF
from . import mail

def generate_otp():
    return str(random.randint(100000,999999))

def send_otp(email, code):
    msg = Message("Your OTP Code",
                  sender="your_email@gmail.com",
                  recipients=[email])
    msg.body = f"Your login code is: {code}"
    mail.send(msg)

def generate_pdf(title, content):
    folder = "app/static/generated_pdfs"
    os.makedirs(folder, exist_ok=True)

    file_path = f"{folder}/{title}.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"{title}\n\n{content}")
    pdf.output(file_path)

    return f"generated_pdfs/{title}.pdf"
