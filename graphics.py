from tkinter import *
from PIL import Image, ImageTk

#*I might want to use inheritance in the future because the basic graphics is the same.
class StartWindow():
    def __init__(self):
        self.startwindow = Tk()
        self.startwindow.title("Start Window")
        self.mode_intro = Label(self.startwindow, text="Who is playing?")
        self.mode_intro.grid(row=0, column=0)
        self.mode = StringVar()
        self.mode.set("User")
        self.user_mode = Radiobutton(self.startwindow, text="User", variable=self.mode, value="User", command=self.user_play)
        self.user_mode.grid(row=1, column=0, sticky=W)
        self.computer_mode = Radiobutton(self.startwindow, text="Computer/Simulation", variable=self.mode, value="Computer")
        self.computer_mode.grid(row=2, column=0, sticky=W)

        #*I will create the simulation options later.

    def user_play(self):
        self.startwindow.destroy()
        self.play_window = Tk()
        self.my_canvas = Canvas(self.play_window, width=300, height=300, bg="white")
        door1_image = ImageTk.PhotoImage(Image.open("door1.png"))
        door1_image = PhotoImage(file="door1.png")
        self.my_canvas.create_image(50, 50, image=door1_image)
        self.my_canvas.grid(row=0, column=0)

a = StartWindow()
mainloop()