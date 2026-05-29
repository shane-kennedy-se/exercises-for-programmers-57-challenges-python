import tkinter as tk

def update_counter(event=None):
    input_str = text_widget.get("1.0", "end-1c")

    count = len(input_str)
    counter_label.config(text=f"Characters: {count}")

root = tk.Tk()

# Top label for exercise name
label = tk.Label(root, text="Exercise 2: Counting Characters!")
label.pack()

# Textbox to type 
text_widget = tk.Text(root, height=10, width=40)
text_widget.pack(padx=10, pady=10)

# Event to update update_counter function
text_widget.bind("<KeyRelease>", update_counter)

counter_label = tk.Label(root, text="Type something!")
counter_label.pack(pady=5)

root.mainloop()