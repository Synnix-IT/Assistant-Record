from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png", 10, 65, 190, 190)
pdf.set_font("helvetica", "B", size = 45)
pdf.text(45, 45, txt = "CS50 Shirtificate")
pdf.set_font("helvetica", "B", size = 25)
pdf.set_text_color(255, 255, 255)
pdf.text(70, 140, txt = f"{name} took CS50")
pdf.output("shirtificate.pdf")
