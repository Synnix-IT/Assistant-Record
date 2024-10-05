# Implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in
# a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

#   The orientation of the PDF should be Portrait.
#   The format of the PDF should be A4, which is 210mm wide by 297mm tall.
#   The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
#   The shirt’s image should be centered horizontally.
#   The user’s name should be on top of the shirt, in white text.


from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # // Setting image location pox (x/y), width/height,
        self.image("shirtificate.png", 10, 65, 190, 190)
        self.set_font("helvetica", "B", 45)
        self.text(45, 45, "CS50 Shirtificate")


    def footer(self):
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        self.text(70, 140, f"{name} took CS50")


# // Run the program
if __name__ == "__main__":
    name = input("What's your name? ")

    pdf = PDF()
    pdf.add_page()
    pdf.output("shirtificate.pdf")