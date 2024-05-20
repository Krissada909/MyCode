from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import sys
import tkinter as tk
from datetime import datetime
import os

if len(sys.argv) > 1:
    username = sys.argv[1]
    print("Username:", username)
else:
    print("Username not provided")

def add_image_to_pdf(pdf_path, image_path, output_pdf_path):
    try:
        # อ่าน PDF
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        # เพิ่มรูปภาพเข้าไปใน PDF
        for page in reader.pages:
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            can.drawImage(image_path, 3.49 * 130, 11.0 * 76.2 - 9 * 72 - 0.43 * 72, width=0.8 * 72, height=0.3 * 72)
            can.save()
            packet.seek(0)
            overlay_pdf = PdfReader(packet)
            page.merge_page(overlay_pdf.pages[0])
            writer.add_page(page)

        # บันทึก PDF ที่แก้ไขแล้ว
        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)

        print("Image added to PDF successfully.")
    except Exception as e:
        print(f"Error adding image to PDF: {str(e)}")

timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S_")



path = r"\\N2N-BANK\Users\Administrator\Downloads\Excel\InvoiceSignature"
# สร้างโฟลเดอร์ใหม่หากยังไม่มี
os.makedirs(path, exist_ok=True)

# กำหนดชื่อไฟล์
output_filename = f"Invoic(ต้นฉบับ){timestamp}.pdf"
output_path = os.path.join(path, output_filename)


username = "ken"
# ตรวจสอบ username และเรียกใช้ฟังก์ชันเพื่อเพิ่มรูปภาพลงใน PDF
if username == "sa":
    print("Username is sa")
    add_image_to_pdf(r"\\N2N-BANK\Users\Administrator\Downloads\Excel\Invoice\pdfmmanuscript.pdf", "Ting Digital Sign.png", output_path)
    # เปิดโฟลเดอร์
    os.startfile(path)

elif username == "ken":
    print("Username is bank")
    add_image_to_pdf(r"\\N2N-BANK\Users\Administrator\Downloads\Excel\Invoice\pdfmmanuscript.pdf", "Ken-Signature.png", output_path)
    # เปิดโฟลเดอร์
    os.startfile(path)