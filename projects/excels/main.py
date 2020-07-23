from openpyxl import Workbook

workbook=Workbook()
sheet=workbook.active

sheet["A1"]="hello"
sheet["B1"]="hello"
workbook.save(filename="index.xlsx")
print(sheet[f"{i}{n}\t"].value)
         # sheet[f"{i}{n}"]=1
# workbook.save(filename="index.xlsx")