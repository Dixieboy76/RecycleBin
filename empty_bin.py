from tkinter import *
import customtkinter
import winshell
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Function to get a list of items in the recycle bin
def get_recycle_bin_items():
    recycle_bin_items = list(winshell.recycle_bin())
    return recycle_bin_items

# Function to display items in the text box
def display_items():
    # Clear the text box
    my_text.delete("1.0", "end")

    # Get a list of items in the recycle bin
    recycle_bin_items = get_recycle_bin_items()

    # Display items in the the recycle bin
    items_text = "\n".join([f"Item Name: {item.original_filename()}\nItem Recycle Date: {item.recycle_date}" for item in recycle_bin_items])
    my_text.insert("end", items_text)

# Function to empty the recycle bin
def empty_bin():
    # Get a list of items in the recycle bin
    recycle_bin_items = get_recycle_bin_items()

    # Display items in the the recycle bin
    items_text = "\n".join([f"Item Name: {item.original_filename()}\nItem Recycle Date: {item.recycle_date}" for item in recycle_bin_items])
    confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to permanently delete the following items from your Recycle Bin?")

    if confirmation:
        # Empty the Recycle Bin without confirmation
        winshell.recycle_bin().empty(confirm=False)
        messagebox.showinfo("Success", "Recycle Bin has been emptied.")
        my_text.delete("1.0", "end") # Clear the text box after emptying
    else:
        messagebox.showinfo("Cancelled", "Empty Operation Cancelled.")

# Create App
root = customtkinter.CTk()
root.title("Recycle Bin")
root.geometry("700x300")

# Add icon to the window
icon_path = "recycle.ico"
root.iconbitmap(icon_path)

# Create A Textbox
my_text = customtkinter.CTkTextbox(root, width=650, height=200)
my_text.pack(pady=25)

# Create Frame to hold buttons
button_frame = customtkinter.CTkFrame(root)
button_frame.pack()

# Add "Get Items" Button
get_items_button =customtkinter.CTkButton(button_frame, text="Get Items", command=display_items)
get_items_button.pack(side="left", padx=10)

# Add "Empty Bin" Button
empty_bin_button = customtkinter.CTkButton(button_frame, text="Empty Bin", command=empty_bin)
empty_bin_button.pack(side="left", padx=10)

# Start the Tkinter main loop
root.mainloop()