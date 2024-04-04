from tkinter import *
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스","토끼에서 마우스가 클릭됨")

window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "C:\Users\why10\OneDrive\바탕 화면\i-seed\images.jfif")
label1 = Label(window, image = photo)

label1.bind("<button>",clickImage)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()
