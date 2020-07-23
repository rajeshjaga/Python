import tkinter
import pandas as pd

def submit_fields():
    path='index.xlsx'
    df1=pd.read_excel(path)
    SeriesA=df1['Date']
    SeriesB=df1['Vehicle No']
    SeriesC=df1['Rate']
    SeriesD=df1['Quantity']
    SeriesE=df1['Price']
    A=pd.Series(entry1.get())
    B=pd.Series(entry2.get())
    C=pd.Series(float(entry3.get()))
    D=pd.Series(float(entry4.get()))
    E=C*D
    SeriesA=SeriesA.append(A)
    SeriesB=SeriesB.append(B)
    SeriesC=SeriesC.append(C)
    SeriesD=SeriesD.append(D)
    SeriesE=SeriesE.append(E)
    df2=pd.DataFrame({"Date":SeriesA,"Vehicle No":SeriesB,"Rate":SeriesC,"Quantity":SeriesD,"Price":SeriesE})
    df2.to_excel(path,index=False)
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)
    entry4.delete(0,tkinter.END)


master=tkinter.Tk()

canvas=tkinter.Canvas(master,height=450,width=500,bg="#263d42")
canvas.pack()
frame = tkinter.Frame(master,bg="white")
frame.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)

tkinter.Label(frame, text="Date",width=20,height=3,bg="white",font="16").grid(row=0 )
tkinter.Label(frame, text="Vehicle NO",width=20,height=3,bg="white",font="16").grid(row=1)
tkinter.Label(frame, text="Rate",width=20,height=3,bg="white",font="16").grid(row=2)
tkinter.Label(frame, text="Quantity",width=20,height=3,bg="white",font="16").grid(row=3)

entry1= tkinter.Entry(frame,width=20,bg="#ECECEC",font="18")
entry2= tkinter.Entry(frame,width=20,bg="#ECECEC",font="18")
entry3= tkinter.Entry(frame,width=20,bg="#ECECEC",font="18")
entry4= tkinter.Entry(frame,width=20,bg="#ECECEC",font="18")

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)
entry4.grid(row=3,column=1)

tkinter.Button(frame, text="Submit",command=submit_fields ,height=2,width=10,bg="#6AC710").grid(row=6,pady=10,padx=15)


tkinter.mainloop()