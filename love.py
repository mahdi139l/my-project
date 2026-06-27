import tkinter as tk 
from tkinter import messagebox 

root = tk.Tk()
root.title(" do you like me ? ")
root.geometry("300x150")
label = tk.Label(root , text = "do you like me ?" , font = ("Arial" , 14 ))
label.pack(pady = 20 )

def yes_action() : 
    messagebox.showinfo("answer" , "i love you .❤")
yes_button = tk.Button (root , text = "yes" , font = ("Arial" , 12 ) , width = 10  , command = yes_action ) 
yes_button.pack(side = "left" , padx = 30 , pady = 10 )

no_button = tk.Button(root , text = "no" , font = ("Arial" , 12 ) , width = 10 ) 
no_button.pack(side = "right" , padx = 30 , pady = 10 )

root.mainloop()
