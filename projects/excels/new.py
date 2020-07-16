from tkinter import *
import pandas as pd

def submit_fields():
    print("reached here")
    path='index.xlsx'
    df1=pd.read_excel(path)
    SeriesA=df1['Date']
    SeriesB=df1['Vehicle No']
    SeriesC=df1['Rate']
    SeriesD=df1['Quantity']
    SeriesE=df1['Price']
    A=pd.Series(entry1.get())
    B=pd.Series(entry2.get())
    C=pd.Series(entry3.get())
    D=pd.Series(entry4.get())
    E=pd.Series(entry5.get())
    SeriesA=SeriesA.append(A)
    SeriesB=SeriesB.append(B)
    SeriesC=SeriesC.append(C)
    SeriesD=SeriesD.append(D)
    SeriesE=SeriesE.append(E)
    df2=pd.DataFrame({"Date":SeriesA,"Vehicle No":SeriesB,"Rate":SeriesC,"Quantity":SeriesD,"Price":SeriesE})
    df2.to_excel(path,index=False)
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)


master=Tk()

Label(master, text="Date", anchor="e",justify=LEFT).grid(row=0)
Label(master, text="Vehicle NO").grid(row=1)
Label(master, text="Rate").grid(row=2)
Label(master, text="Quantity").grid(row=3)
Label(master, text="Price").grid(row=4)

entry1= Entry(master)
entry2= Entry(master)
entry3= Entry(master)
entry4= Entry(master)
entry5= Entry(master)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)
entry4.grid(row=3,column=1)
entry5.grid(row=4,column=1)

Button(master, text="quit",command=master.quit).grid(row=6,column=0,pady=4)
Button(master, text="submit",command=submit_fields).grid(row=6,column=1,pady=4)


mainloop()