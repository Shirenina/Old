from tkinter import *
import time

root = Tk()
root.title("Точное время")
root.resizable(width=False, height=False)

watch = Label(root, font = "Gothic 100", background="lightblue")

def sec():
    watch.after(1000, sec) #after(self, ms, func=None, *args) -  Call function once after given time.
    watch['text'] = time.strftime("%H:%M:%S")


watch.pack()
sec()

root.mainloop()