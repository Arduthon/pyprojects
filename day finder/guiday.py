import datetime
import tkinter as tk
from tkinter import messagebox

def calculate_days():
    try:
        a = int(entry_birth_year.get())
        b = int(entry_till_year.get())
        c = int(entry_month.get())
        d = int(entry_day.get())
        
        # Get the weekday of the input birth year
        e = int(datetime.date(a, c, d).weekday())
        
        days = ["Mon", "Tues", "Wed", "Thus", "Fri", "Sat", "Sun"]
        result = ""
        
        for x in range(a, b):
            weekDay_num = datetime.date(x, c, d).weekday()
            if weekDay_num == e:
                result += f"{days[weekDay_num]} {x}\n"
        
        # Display the result in the Text widget
        result_text.delete("1.0", tk.END)  # Clear previous result
        result_text.insert(tk.END, result)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values!")
    except Exception as error:
        messagebox.showerror("Error", f"An error occurred: {error}")

def clear_data():
    # Clear all entry fields and result text
    entry_birth_year.delete(0, tk.END)
    entry_till_year.delete(0, tk.END)
    entry_month.delete(0, tk.END)
    entry_day.delete(0, tk.END)
    result_text.delete("1.0", tk.END)

# Create main window
window = tk.Tk()
window.title("Weekday Finder App")
window.geometry("300x400")  # Fixed window size
window.resizable(False, False)  # Disable resizing

# Background color for the window
window.configure(bg="#f0f0f5")

# Create labels and entry fields with colors
label_birth_year = tk.Label(window, text="Birth Year:", bg="#f0f0f5", fg="#000")
label_birth_year.grid(row=0, column=0, padx=10, pady=10)
entry_birth_year = tk.Entry(window, bg="#ffffff", fg="#000")
entry_birth_year.grid(row=0, column=1, padx=10, pady=10)

label_till_year = tk.Label(window, text="Till Year:", bg="#f0f0f5", fg="#000")
label_till_year.grid(row=1, column=0, padx=10, pady=10)
entry_till_year = tk.Entry(window, bg="#ffffff", fg="#000")
entry_till_year.grid(row=1, column=1, padx=10, pady=10)

label_month = tk.Label(window, text="Month:", bg="#f0f0f5", fg="#000")
label_month.grid(row=2, column=0, padx=10, pady=10)
entry_month = tk.Entry(window, bg="#ffffff", fg="#000")
entry_month.grid(row=2, column=1, padx=10, pady=10)

label_day = tk.Label(window, text="Day:", bg="#f0f0f5", fg="#000")
label_day.grid(row=3, column=0, padx=10, pady=10)
entry_day = tk.Entry(window, bg="#ffffff", fg="#000")
entry_day.grid(row=3, column=1, padx=10, pady=10)

# Create buttons with color
calc_button = tk.Button(window, text="Find Weekdays", command=calculate_days, bg="#4CAF50", fg="white")
calc_button.grid(row=4, column=0, pady=10, padx=10)

clear_button = tk.Button(window, text="Clear", command=clear_data, bg="#f44336", fg="white")
clear_button.grid(row=4, column=1, pady=10, padx=10)

# Create a text area to display results with color
result_text = tk.Text(window, height=10, width=30, bg="#e0f7fa", fg="#000")
result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
window.mainloop()
