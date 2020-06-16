import tkinter as tk
from tkinter import *
import os


root = tk.Tk()


def openProjects():
    path = "C:/Users/hp/Documents/github/html"
    os.chdir(path)
    


canvas = tk.Canvas(root, height=700, width=450, bg="#001ef0")
canvas.pack(padx=0, pady=0)
frame = tk.Frame(canvas, bg="#ffffff")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
label1 = tk.Label(root, text="hello")
canvas.pack()
but1 = tk.Button(frame, text="New project", bg="#00c3c3",)
but1.place(relheight=0.05, relwidth=0.3, relx=0.025, rely=0.95)
but2 = tk.Button(frame, text="Open project", bg="#00c3c3")
but2.place(relheight=0.05, relwidth=0.3, relx=0.35, rely=0.95)
but3 = tk.Button(frame, text="Delete Project", bg="#00c3c3")
but3.place(relheight=0.05, relwidth=0.3, relx=0.675, rely=0.95)


root.mainloop()
