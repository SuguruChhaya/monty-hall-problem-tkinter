from tkinter import *
import tkinter.font
from PIL import Image, ImageTk
import random
#!Rather than making the classes efficient, I will first focus on building the actual thing.
#*I might want to use inheritance in the future because the basic graphics is the same.
#*I find issues working in different windows in different classes
class StartWindow():

    def __init__(self):
        self.startwindow = Tk()
        self.startwindow.title("Start Window")
        self.mode_intro = Label(self.startwindow, text="Who is playing?")
        self.mode_intro.grid(row=0, column=0)
        self.mode = StringVar()
        self.mode.set("User")
        self.user_mode = Radiobutton(self.startwindow, text="User", variable=self.mode, value="User", command=self.user_actions)
        self.user_mode.grid(row=1, column=0, sticky=W)
        self.computer_mode = Radiobutton(self.startwindow, text="Computer/Simulation", variable=self.mode, value="Computer", command=self.computer_actions)
        self.computer_mode.grid(row=2, column=0, sticky=W)
        #*I will create the simulation options later.

#*I will try making a new class.
    def default(self):
        self.startwindow.destroy()
        self.play_window = Tk()
        self.my_canvas = Canvas(self.play_window, width=500, height=500, bg="white")
        self.my_canvas.grid(row=0, column=0)
        self.door1_image = ImageTk.PhotoImage(Image.open("images/door1.jpg"))
        self.door2_image = ImageTk.PhotoImage(Image.open("images/door2.jpg"))
        self.door3_image = ImageTk.PhotoImage(Image.open("images/door3.jpg"))
        self.down_arrow_image = ImageTk.PhotoImage(Image.open("images/downarrow.jpg"))
        self.host_image = ImageTk.PhotoImage(Image.open("images/host.jpg"))
        self.door1 = self.my_canvas.create_image(100, 200, image=self.door1_image, tags='door1')
        self.door2 = self.my_canvas.create_image(250, 200, image=self.door2_image, tags="door2")
        self.door3 = self.my_canvas.create_image(400, 200, image=self.door3_image, tags='door3')
        self.host = self.my_canvas.create_image(100, 400, image=self.host_image, tags="host")
        self.door_font = tkinter.font.Font(size=15)
        #self.select_door = self.my_canvas.create_text(250, 350, text="Choose a door", font = self.door_font, fill='red')
        self.select_door = self.my_canvas.create_text(300, 350, text="Select a door", font=self.door_font, fill='red')

        #*The assigning process
        all_list = ['goat', 'goat', 'car']
        assign_list = all_list.copy()
        door_1_value = random.choice(assign_list)
        self.my_canvas.itemconfig(self.door1, tags=('door1', door_1_value))
        assign_list.remove(door_1_value)
        door_2_value = random.choice(assign_list)
        self.my_canvas.itemconfig(self.door2, tags=('door2', door_2_value))
        assign_list.remove(door_2_value)
        door_3_value = random.choice(assign_list)
        self.my_canvas.itemconfig(self.door3, tags=('door3', door_3_value))
        assign_list.remove(door_3_value)


    def user_bind(self):
        #*I need to follow this specific format
        #?I think I will want this is a different function because if I will inherit from this, I don't want to bind.
        #*If the bind keyword contains any of the items in the tuple, I can move it with it.
        #!Just to note: when binded, tkinter automatically creates a tag called 'current' at the end.
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
        self.down_arrow = self.my_canvas.create_image(self.x_coord, self.y_coord - 120, image=self.down_arrow_image, tags='arrow')
        #*To keep track of what has been chosen by tags
        #!I will use the the down_arrow as a reference for the add_tag_below
        #self.my_canvas.addtag_below('chosen', 'arrow')
        self.change_function()
    #*Rather than inheriting a whole class, I should try to reuse methods in the class.

    def change_function(self):
        print(self.my_canvas.gettags(self.door1))
        print(self.my_canvas.gettags(self.door2))
        print(self.my_canvas.gettags(self.door3))
        self.my_canvas.delete(self.select_door)
        self.change_door = self.my_canvas.create_text(300, 350, text="LAST CHANCE to switch doors!\nClick your final pick!", font=self.door_font, fill='red')
        self.door_list = [self.door1, self.door2, self.door3]
        self.show_fake_list = self.door_list.copy()
        self.change_door_list = self.door_list.copy()
        
        for item in self.door_list:
            if 'car' in self.my_canvas.gettags(item) or 'current' in self.my_canvas.gettags(item):
                self.show_fake_list.remove(item)
        
            #*I also cannot choose the one the person has chosen

        self.show_fake = random.choice(self.show_fake_list)
        #*I think I should nicely unbind this thing
        self.goat_coords = self.my_canvas.coords(self.show_fake)
        print(self.goat_coords)
        self.my_canvas.delete(self.show_fake)
        self.goat_image = ImageTk.PhotoImage(Image.open('images/goat.jpg'))
        self.goat_door = self.my_canvas.create_image(self.my_canvas.coords(self.goat_coords[0], self.goat_coords[1]), image=self.goat_image)


    def user_actions(self):
        self.default()
        self.user_bind()


    def computer_actions(self):
        self.default()

    



class Inherit(StartWindow):
    def __init__(self):
        StartWindow.__init__(self)

a = StartWindow()
#b = Inherit()
mainloop()