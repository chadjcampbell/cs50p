from fpdf import FPDF


def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 40)
    pdf.cell(pdf.epw, 50, 'CS50 Shirtificate', align='C')
    pdf.ln(60)
    pdf.image("shirtificate.png", h=pdf.eph*.6,
              w=pdf.epw, keep_aspect_ratio=True)
    pdf.set_y(0)
    pdf.ln(100)
    pdf.set_font('helvetica', 'B', 20)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(pdf.epw, 50, f"{name} took CS50", align='C')
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
