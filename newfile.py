
import tkinter as tk
from tkinter import colorchooser


def pick_color():
    
    color = colorchooser.askcolor(title="Choose a Color")
    
    
    if color[1] is not None:
        
        color_label.config(text=f"Selected Color: {color[1]}", bg=color[1])


root = tk.Tk()
root.title("Tkinter Color Picker")
root.geometry("400x200")


color_label = tk.Label(root, text="Select a color using the button below", 
                       font=("Helvetica", 14), bg="lightgray", pady=20)
color_label.pack(fill="both", expand=True)


choose_button = tk.Button(root, text="Pick Color", font=("Helvetica", 12), 
                          command=pick_color)
choose_button.pack(pady=10)


root.mainloop()
