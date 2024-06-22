import tkinter as tk
from tkinter import messagebox
import os
import logging

# Set up logging
# logging.basicConfig(filename='app.log', level=logging.DEBUG,
#                     format='%(asctime)s:%(levelname)s:%(message)s')


def repeat_and_save():
    paragraph = text_entry.get("1.0", tk.END).strip()
    num_str = num_entry.get().strip()

    if not paragraph:
        logging.error("No paragraph entered.")
        messagebox.showerror("Error", "Please enter a paragraph.")
        return

    if not num_str.isdigit():
        logging.error("Invalid number entered: %s", num_str)
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    num = int(num_str)

    # Repeat the paragraph with each repetition on a new line
    repeated_paragraph = (paragraph + '\n') * num

    try:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        file_path = os.path.join(desktop, "repeated_paragraph.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(repeated_paragraph)
        logging.info("File saved successfully at %s", file_path)
        messagebox.showinfo("Success", f"Paragraph repeated and saved successfully on desktop!")
    except Exception as e:
        logging.error("Error while saving file: %s", e)
        messagebox.showerror("Error", f"An error occurred while saving the file: {e}")


# Set up the main application window
root = tk.Tk()
root.title("Paragraph Repeater")

# Bold font
bold_font = ('Helvetica', 10, 'bold')

# Paragraph entry
tk.Label(root, text="Enter Paragraph:", font=bold_font).pack(pady=5)
text_entry = tk.Text(root, wrap=tk.WORD, width=50, height=5, font=('Helvetica', 10))
text_entry.pack(pady=5)

# Number entry
tk.Label(root, text="Enter Number:", font=bold_font).pack(pady=5)
num_entry = tk.Entry(root, font=('Helvetica', 10))
num_entry.pack(pady=5)

# Repeat and save button
repeat_button = tk.Button(root, text="Repeat and Save", command=repeat_and_save, bg='blue', fg='white', font=bold_font)
repeat_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
