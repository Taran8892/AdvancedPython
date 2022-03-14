from flat import Bill, Flatmate
from reports import PdfReport

a = float(input("Hey user, enter the bill amount: "))
p = input("Enter the period: ")
f1 = input("Flatmate1 name: ")
d1 = int(input(f"Number of days {f1} lived: "))
f2 = input("Flatmate2 name: ")
d2 = int(input(f"Number of days {f2} lived: "))

the_bill = Bill(amount=a, period=p)
o1 = Flatmate(name=f1, days_in_house=d1)
o2 = Flatmate(name=f2, days_in_house=d2)

print(f"{f1} Pays: ", o1.pays(bill=the_bill, flatmate2=o2))
print(f"{f2} Pays: ", o2.pays(the_bill, o1))
filename = p + "_Report.pdf"

pdf_report = PdfReport(filename)
pdf_report.generate(flatmate1=o1, flatmate2=o2, bill=the_bill)


