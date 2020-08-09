'''
I am just going to try make a simulator first because I think that is going to be the hardest.
'''
import random
import tkinter

#*To copy a list, I have to use the .copy() method.

#*I need to make a class to manage the status of the door by a class.

class Doors():
    def __init__(self, behind):
        self.behind = behind

change_counter = 0
no_change_counter = 0
for i in range(100000):

    all_list = ['goat', 'goat', 'car']
    assign_list = all_list.copy()
    door_1_value = random.choice(assign_list)
    door_1 = Doors(door_1_value)
    assign_list.remove(door_1_value)
    door_2_value = random.choice(assign_list)
    door_2 = Doors(door_2_value)
    assign_list.remove(door_2_value)
    door_3_value = random.choice(assign_list)
    door_3 = Doors(door_3_value)
    assign_list.remove(door_3_value)

    door_list = [door_1, door_2, door_3]
    change_choices = door_list.copy()
    door_list_copy = door_list.copy()
    user_choice = random.choice(door_list_copy)
    door_list_copy.remove(user_choice)

    for item in door_list_copy:
        if item.behind == "car":
            door_list_copy.remove(item)

    open_choice = random.choice(door_list_copy)
    change_choices.remove(open_choice)

    #*Door after change
    change_choices.remove(user_choice)
    change_final_door = change_choices[0]

    no_change_final_door = user_choice
    if change_final_door.behind == 'car':
        change_counter += 1
    elif no_change_final_door.behind == 'car':
        no_change_counter += 1
    
print("Times car was behind when changed: " + str(change_counter))
print("Times car was behind when didn't change: " + str(no_change_counter))







