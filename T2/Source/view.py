from Tkinter import *
from PIL import ImageTk, Image

master = Tk()

w = Canvas(master, width=500, height=600)
rectSize = 40
"""
i = 0
while i < 12:
    j = 0
    while j<12:
        w.create_rectangle(10+rectSize*j, 50+rectSize*(12-i), 10+ rectSize*j+rectSize, 50+rectSize*(12-i)+rectSize, fill="white", outline='black')
        j = j+1
    i = i+1"""

image = ImageTk.PhotoImage(Image.open("bla.png"))
imagesprite = w.create_image(400,400,image=image)

w.pack()
master.mainloop()