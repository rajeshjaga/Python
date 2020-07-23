from openpyxl import load_workbook


workbook = load_workbook(filename="index.xlsx")
List=["A","B","C","D","E"]
sheet = workbook.active
no_of_bills=int(input("please enter the round of bills"))

for i in List:
    for  n in  range (1,no_of_bills):
        print(sheet[f"{i}{n}\t"].value)