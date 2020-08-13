from tkinter import *
import tkinter.font
from PIL import Image, ImageTk

#*I might want to use inheritance in the future because the basic graphics is the same.
class UserGame():

    @staticmethod
    def user_start():
        UserGame()
        

    def __init__(self):
        self.startwindow.destroy()
        self.play_window = Tk()
        self.play_window.title("User play window")
        self.my_canvas = Canvas(self.play_window, width=500, height=500)
        self.my_canvas.grid(row=0, column=0)
        #*Have to make sure to add a self.
        self.door1_image = ImageTk.PhotoImage(Image.open("images/door1.jpg"))
        self.door2_image = ImageTk.PhotoImage(Image.open("images/door2.jpg"))
        self.door3_image = ImageTk.PhotoImage(Image.open("images/door3.jpg"))
        self.down_arrow_image = ImageTk.PhotoImage(Image.open("images/downarrow.jpg"))
        self.host_image = ImageTk.PhotoImage(Image.open("images/host.jpg"))
        self.door1 = self.my_canvas.create_image(100, 200, image=self.door1_image, tags="door1")
        self.door2 = self.my_canvas.create_image(250, 200, image=self.door2_image, tags="door2")
        self.door3 = self.my_canvas.create_image(400, 200, image=self.door3_image, tags='door3')
        self.host = self.my_canvas.create_image(100, 400, image=self.host_image)
        self.door_font = tkinter.font.Font(size=15)
        #self.select_door = self.my_canvas.create_text(250, 350, text="Choose a door", font = self.door_font, fill='red')
        self.change_door = self.my_canvas.create_text(300, 350, text="Select a door", font=self.door_font, fill='red')

        #*I will create the simulation options later.

    def user_play(self):
        #*I need to follow this specific format
        #?I think I will want this is a different function because if I will inherit from this, I don't want to bind.
        self.my_canvas.tag_bind('door1', '<ButtonPress-1>', lambda event, selected_door=self.door1: self.print_hi(event, selected_door))
        self.my_canvas.tag_bind('door2', '<ButtonPress-1>', lambda event, selected_door=self.door2: self.print_hi(event, selected_door))
        self.my_canvas.tag_bind('door3', '<ButtonPress-1>', lambda event, selected_door=self.door3: self.print_hi(event, selected_door))

    def print_hi(self, event, selected_door):
        #*Try to forget all the bindings
        try:
            self.my_canvas.delete(self.down_arrow)
        #*For when object wasn't created yet
        except AttributeError:
            pass
        self.x_coord, self.y_coord = self.my_canvas.coords(selected_door)[0], self.my_canvas.coords(selected_door)[1]
        self.down_arrow = self.my_canvas.create_image(self.x_coord, self.y_coord - 120, image=self.down_arrow_image)


        
startwindow = Tk()
startwindow.title("Start Window")
mode_intro = Label(startwindow, text="Who is playing?")
mode_intro.grid(row=0, column=0)
mode = StringVar()
mode.set("User")
user_mode = Radiobutton(startwindow, text="User", variable=mode, value="User", command=StartWindow)
user_mode.grid(row=1, column=0, sticky=W)
computer_mode = Radiobutton(startwindow, text="Computer/Simulation", variable=mode, value="Computer")
computer_mode.grid(row=2, column=0, sticky=W)

mainloop()