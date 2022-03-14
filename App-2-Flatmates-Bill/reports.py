import os
import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file that containes data about the flatmates such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(flatmate1.pays(bill, flatmate2))
        flatmate2_pay = str(flatmate1.pays(bill, flatmate1))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=12, style='B')
        pdf.cell(w=150, h=40, txt="Period", border=0, align="C")
        pdf.cell(w=150, h=40, txt=bill.period, border=0, align="C", ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=10)
        pdf.cell(w=150, h=25, txt=flatmate1.name, align="C", border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, align="C", ln=1)

        pdf.cell(w=150, h=25, txt=flatmate2.name, align="C", border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, align="C", border=0)

        pdf.output(f"files/{self.filename}")
        webbrowser.open('file://' + os.path.realpath(f"files/{self.filename}"))
