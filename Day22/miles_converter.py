from tkinter import *

TOKM = 1.609  # Multiply miles by TOKM to get Km

def button_clicked():
    # Get miles_input from the entry
    miles = float(miles_input.get())
    # multiply miles by TOKM and convert to int
    km = round(miles * TOKM, 2)  # Km rounded to 2 decimal places
    # Change the km solution label to km
    km_solution.config(text=f"{km}")

window = Tk()

window.title("Miles to Kilometer Converter")
window.minsize(width=220, height=100)
window.config(padx=50, pady=20)

# Input Entry to get the miles
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# A Label for Miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row= 0)

# Label for is equal to text
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Label with the Km solution text
km_solution = Label(text="0")
km_solution.grid(column=1, row=1)

# Label with Km text
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)



window.mainloop()