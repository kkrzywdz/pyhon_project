import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("800x600")

# Create a function that will be called when the button is clicked
def button_clicked():
    print("Button was clicked!")

# Create a button
button = tk.Button(text="Click me!", command=button_clicked)

# Create a canvas to draw on
canvas = tk.Canvas(window, width=300, height=300, bg="#ffffff")

# Create a blue circle on the canvas
circle = canvas.create_oval(50, 50, 250, 250, fill="#0000ff")

# Draw the ship's hull
hull = canvas.create_polygon([(100, 100), (150, 50), (200, 100), (150, 150)], fill="#0000ff")

# Draw the ship's mast
mast = canvas.create_line(150, 50, 150, 25)

# Bind a function to the ship's hull
def ship_clicked(event):
    print("Ship was clicked at", event.x, event.y)
canvas.tag_bind(hull, "<Button-1>", ship_clicked)


# Place the canvas in the window
canvas.pack()

# Place the button in the window
button.pack()

# Run the Tkinter event loop
window.mainloop()
