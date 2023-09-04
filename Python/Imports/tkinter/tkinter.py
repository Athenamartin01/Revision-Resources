# Used to Create basic window applications easily
import tkinter as tk

def Function():
    pass


root = tk.Tk(className='calc') #Creates a new window witht title calc
root.title("Calculator") #Names the window calculator 

My_label = tk.Label(root, text = "Hello World") #Creates Label

My_button = tk.Button(root, text="click me", state="disabled", padx=50, pady=50, fg = "orange", bg ="#ffffff",  command=Function) 
#Creates a button which isn't clickable, padx,y increases the size of the button
#command is used to select a function which the button should run when it is pressed
#fg and bg makes the foreground and background, orange and purple 

Text_Box = tk.Entry(root, width = 10, height = 10, borderwidth = 10)
Text_Box.get() #takes the string from the text box
Text_Box.insert(0, "I AM A TEXT BOX") #adds text to the text box 

My_label.pack() #Displays it on screen in the first open spot
My_label.grid(row=0, column=0) #places in a grid order

My_button.destroy() #Removes the button

root.mainloop() #Opens the window