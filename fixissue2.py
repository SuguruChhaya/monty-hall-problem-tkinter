
from tkinter import *
import tkinter.font
from PIL import Image, ImageTk
import random

from tkinter import messagebox

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

        #*To keep track of whether the change_function has ran already.
        self.change_tracker = 0

#*I will try making a new class.
    def default(self):
        print('passed default')
        try:
            self.play_window.destroy()
        except AttributeError:
            pass

        #*Try to get the slider value
        #*I added TypeError because I set the value of self.slider_value to None after the initial simulation.
        #*This causes me to re-retrieve the value of self.slider.get()
        try:
            self.slider_value -= 1    
        except AttributeError:
            self.slider_value = self.slider.get() 
        except TypeError:
            self.slider_value = self.slider.get()

        self.play_window = Toplevel(self.startwindow)
        self.play_window.title("User play window")
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

        #*To differentiate between computer and simulation
        if self.mode.get() == 'User':
            print("lol")
        else:
            #*Simuulation time
            #*I think I can create an after function at this point
            #*Also calculate time.
            #*1. main to switch, 2. switch to final check, 3. final check to default, 4. default to main : therfore 4 parts
            if self.time_var.get() == 'MIN TIME':
                self.after_time = 0
            else:
                self.after_time = int(int(self.time_var.get()[:2]) / (self.slider.get() * 4) * 1000)
                if self.after_time < 50:
                    self.after_time = 0
            print(self.after_time)
            self.after_func = self.my_canvas.after(self.after_time, self.simulation_main)


    def user_bind(self):
        print("passed user bind")
        #*I need to follow this specific format
        #?I think I will want this is a different function because if I will inherit from this, I don't want to bind.
        #*If the bind keyword contains any of the items in the tuple, I can move it with it.
        #!Just to note: when binded, tkinter automatically creates a tag called 'current' at the end.
        #?This was false, but I know that the binding gave me a tuple error at the point where I hit the selected door.
        #*For example, if I selected door3, door1 and 2 will work without an error, but door3 doesn't.
        self.my_canvas.tag_bind('door1', '<ButtonPress-1>', lambda event, selected_door=self.door1: self.print_hi(event, selected_door))
        #?I think the bug is related to the current tag attatchedto whatever door I chose first. I will first try to remove the tag
        self.my_canvas.tag_bind('door2', '<ButtonPress-1>', lambda event, selected_door=self.door2: self.print_hi(event, selected_door))
        self.my_canvas.tag_bind('door3', '<ButtonPress-1>', lambda event, selected_door=self.door3: self.print_hi(event, selected_door))

    def print_hi(self, event, selected_door):
        print("passed hi")
        #*Try to forget all the bindings
        try:
            self.my_canvas.delete(self.down_arrow)
        #*For when object wasn't created yet
        except AttributeError:
            pass
        #!This whole tag issue might be because of the following functions!
        self.x_coord, self.y_coord = self.my_canvas.coords(selected_door)[0], self.my_canvas.coords(selected_door)[1]
        self.down_arrow = self.my_canvas.create_image(self.x_coord, self.y_coord - 120, image=self.down_arrow_image, tags='arrow')
        #*To keep track of what has been chosen by tags
        #!I will use the the down_arrow as a reference for the add_tag_below
        #self.my_canvas.addtag_below('chosen', 'arrow')

        #*Since I want to reuse this function the second time without running the change function, I am keeping track of whether it had
        #*ran already.
        if self.change_tracker == 0:
            self.change_function()
        else:
            self.final_check(selected_door)
    #*Rather than inheriting a whole class, I should try to reuse methods in the class.

    def change_function(self):
        self.change_tracker = 1
        print("passed change function")
        self.my_canvas.delete(self.select_door)
        self.change_door = self.my_canvas.create_text(300, 350, text="LAST CHANCE to switch doors!\nClick your final pick!", font=self.door_font, fill='red')
        self.door_list = [self.door1, self.door2, self.door3]
        self.show_fake_list = self.door_list.copy()
        self.change_door_list = self.door_list.copy()
        
        for item in self.door_list:
            if 'car' in self.my_canvas.gettags(item):
                self.show_fake_list.remove(item)
            #*I have to make this 'elif' just in case the 'current' had the 'car'. I cannot double remove the item.
            elif 'current' in self.my_canvas.gettags(item):
                self.show_fake_list.remove(item)
                #*Deleting the 'current tag'
                #self.my_canvas.dtag(item, 'current')
        
            #*I also cannot choose the one the person has chosen

        self.show_fake = random.choice(self.show_fake_list)
        #*I think I should nicely unbind this thing
        #!I think I need to look into this tag unbind method
        print(self.my_canvas.gettags(self.door1))
        print(self.my_canvas.gettags(self.door2))
        print(self.my_canvas.gettags(self.door3))
        print(self.door1)

        #*Re-creating the bindings
        self.change_door_list.remove(self.show_fake)
        print(self.change_door_list)
        for item in self.change_door_list:
            #!Using tuples to unbind doesn't work!!
            #*I have to use a string inside the tuple instead
            door_tag = self.my_canvas.gettags(item)[0]
            self.my_canvas.tag_unbind(door_tag, '<ButtonPress-1>')
            self.my_canvas.tag_bind(door_tag, '<ButtonPress-1>', lambda event, selected_door=item: self.print_hi(event, selected_door))
        self.show_goat()

    def show_goat(self):
        self.goat_coords = self.my_canvas.coords(self.show_fake)
        self.goat_x = self.goat_coords[0]
        self.goat_y = self.goat_coords[1]
        self.my_canvas.delete(self.show_fake)
        self.goat_image = ImageTk.PhotoImage(Image.open('images/goat.jpg'))
        self.goat_door = self.my_canvas.create_image(self.goat_x, self.goat_y, image=self.goat_image)

    def final_check(self, selected_door):
        #*First unbind all the buttons
        for item in self.change_door_list:
            door_tag = self.my_canvas.gettags(item)[0]
            self.my_canvas.tag_unbind(door_tag, '<ButtonPress-1>')

        self.coords = self.my_canvas.coords(selected_door)
        self.x = self.coords[0]
        self.y = self.coords[1]
        if 'car' in self.my_canvas.gettags(selected_door):
            self.car_image = ImageTk.PhotoImage(Image.open('images/car.jpg'))
            self.my_canvas.create_image(self.x, self.y, image=self.car_image)
            self.my_canvas.delete(self.change_door)
            self.my_canvas.create_text(300, 350, text="Congratulations!! You won the car!!", font=self.door_font, fill='red')

        else:
            self.my_canvas.create_image(self.x, self.y, image=self.goat_image)
            self.my_canvas.delete(self.change_door)
            self.my_canvas.create_text(300, 350, text="lol u noob", font=self.door_font, fill='red')
            
        self.my_canvas.delete(selected_door)
        #*I want to reset the counter value.
        self.change_tracker = 0


    def user_actions(self):
        self.default()
        self.user_bind()

    def simulation_setup(self):
        self.simulation_count = 0
        self.setup_window = Toplevel(self.startwindow)
        self.slider_intro = Label(self.setup_window, text="How many simulations do you want to perform?")
        self.slider_intro.grid(row=0, column=0)
        self.slider = Scale(self.setup_window, from_=1, to=1000, orient=HORIZONTAL, length=250)
        self.slider.grid(row=1, column=0)
        self.time_intro = Label(self.setup_window, text='How much time should the simulation take?\n(For the sake of graphics)')
        self.time_intro.grid(row=2, column=0)
        self.time_var = StringVar()
        self.time_var.set('10sec')
        time_list = ['MIN TIME', '10sec', '15sec', '20sec']
        self.time_dropbox = OptionMenu(self.setup_window, self.time_var, *time_list)
        self.time_dropbox.grid(row=3, column=0)
        self.switch_var = StringVar()
        self.switch_var.set('Switch during simulation')
        switch_or_no = ['Switch during simulation', "Don't switch during simulation"]
        self.switch_dropbox = OptionMenu(self.setup_window, self.switch_var, *switch_or_no)
        self.switch_dropbox.grid(row=4, column=0)
        self.start_button = Button(self.setup_window, text="Start simulation!", command=self.default)
        self.start_button.grid(row=5, column=0)



    def simulation_main(self):
        print('passed simulation main')
        #*The assignment of tags have already been done
        self.door_list = [self.door1, self.door2, self.door3]
        self.change_door_list = self.door_list.copy()
        self.show_fake_list = self.door_list.copy()
        self.choice_1 = random.choice(self.show_fake_list)
        #*I have to add a down_arrow function for this.
        self.show_fake_list.remove(self.choice_1)

        for item in self.show_fake_list:
            if 'car' in self.my_canvas.gettags(item):
                self.show_fake_list.remove(item)
        
        self.show_fake = random.choice(self.show_fake_list)
        self.change_door_list.remove(self.show_fake)
        self.show_goat()
        self.x_coord, self.y_coord = self.my_canvas.coords(self.choice_1)[0], self.my_canvas.coords(self.choice_1)[1]
        self.down_arrow = self.my_canvas.create_image(self.x_coord, self.y_coord - 120, image=self.down_arrow_image, tags='arrow')
        self.my_canvas.delete(self.select_door)
        self.change_door = self.my_canvas.create_text(300, 350, text="LAST CHANCE to switch doors!\nClick your final pick!", font=self.door_font, fill='red')
        #*Switch or not 
        

        if self.switch_var.get() == 'Switch during simulation':
            self.after_switch = self.my_canvas.after(self.after_time, self.simulation_switch)
        else:
            self.after_noswitch = self.my_canvas.after(self.after_time, self.simulation_noswitch)


    
    def simulation_switch(self):
        print('simulation switch')
        self.my_canvas.delete(self.down_arrow)
        self.change_door_list.remove(self.choice_1)
        self.x_coord, self.y_coord = self.my_canvas.coords(self.change_door_list[0])[0], self.my_canvas.coords(self.change_door_list[0])[1]
        self.down_arrow = self.my_canvas.create_image(self.x_coord, self.y_coord - 120, image=self.down_arrow_image, tags='arrow')
        self.final = self.my_canvas.after(self.after_time, self.final_simulation_check)
        



    def simulation_noswitch(self):
        print('simulation no switch')
        self.my_canvas.delete(self.down_arrow)
        self.x_coord, self.y_coord = self.my_canvas.coords(self.choice_1)[0], self.my_canvas.coords(self.choice_1)[1]
        self.down_arrow = self.my_canvas.create_image(self.x_coord, self.y_coord, image=self.down_arrow_image)
        self.final = self.my_canvas.after(self.after_time, self.final_simulation_check)


    def final_simulation_check(self):
        if 'car' in self.my_canvas.gettags(self.choice_1):
            self.car_image = ImageTk.PhotoImage(Image.open('images/car.jpg'))
            self.my_canvas.create_image(self.x_coord, self.y_coord, image=self.car_image)
            self.my_canvas.delete(self.change_door)
            self.my_canvas.create_text(300, 350, text="Congratulations!! You won the car!!", font=self.door_font, fill='red')
            self.simulation_count += 1
        else:
            self.my_canvas.delete(self.change_door)
            self.my_canvas.create_image(self.x_coord, self.y_coord, image=self.goat_image)
            self.my_canvas.create_text(300, 350, text="lol u noob", font=self.door_font, fill='red')

        #*I have to first store the slider value in a different variable.

        #*The reason I have to make this 1 instead of 0 is because for example if I choose 6 simulations,
        #*I will go through the loop 7 times (6, 5, 4, 3, 2, 1, 0). So I should delete the case of 0
        if self.slider_value > 1:
            #?I have to make sure the self.slider_value only gets initialized once.
            #*Basically self.default is setting the slider value to the initial value. Even if I subtract 1 from that, it will be 
            #*re-initialized when I come back. I have to do something about that.
            print(self.slider_value)
            self.next_simulation = self.my_canvas.after(self.after_time, self.default)
        else:
            print(self.slider_value)
            self.slider_value = None
            #*Create the new window which tracks the value of returns percentage
            messagebox.showinfo("Final report", f"Total number of simulations: {self.slider.get()}\nSimulation type: {self.switch_var.get()}\nTotal count of successful simulations: {self.simulation_count}\nPercentage of success: {self.simulation_count / self.slider.get()}")


    def computer_actions(self):
        self.simulation_setup()
    



class Inherit(StartWindow):
    def __init__(self):
        StartWindow.__init__(self)

a = StartWindow()
#b = Inherit()
mainloop()