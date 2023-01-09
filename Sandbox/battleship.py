import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("1000x600")

# Create a global variable to track the state of the canvas
state = 0
state2 = 0

# Create a frame to hold the canvases
frame = tk.Frame(window)
frame.pack(side="left")


# Create a function that will be called when the button is clicked
def button_clicked():
    text = entry.get()

    global state
    global state2
    print(f"Button was clicked! {state2} - You entered: {text}")
    state = (state + 1) % 2
    state2 = state2 + 1
    canvas1.delete("all")
    if state == 0:
        canvas1.create_rectangle(50, 50, 250, 250, fill="#0000ff")
    else:
        canvas1.create_rectangle(50, 50, 250, 250, fill="#00ff00")
    canvas2.create_rectangle(state2 * 20, state2 * 20, state2 * 20 + 20, state2 * 20 + 20, fill="#0000ff")

# Create a button
button = tk.Button(text="Click me!", command=button_clicked)

# Create a canvas to draw on
canvas1 = tk.Canvas(frame, width=400, height=400, bg="#ffffff")
canvas2 = tk.Canvas(window, width=400, height=400, bg="#ffffff")

# Draw the grid
for x in range(0, 401, 20):
    for y in range(0, 401, 20):
        canvas1.create_rectangle(x, y, x + 20, y + 20, fill="#0000AA")
        canvas2.create_rectangle(x, y, x + 20, y + 20, fill="#0000AA")

# Draw the ship's mast
mast = canvas1.create_line(150, 50, 150, 25)

# Place the Entry in the window
entry = tk.Entry(frame)
entry.pack()


# Bind a function to the ship's hull
def ship_clicked(event):
    print("Ship was clicked at", event.x, event.y)
    canvas2.create_rectangle(event.x, event.y, event.x + 20, event.y + 20, fill="#0000ff")


# Create a blue circle on the canvas
circle = canvas1.create_oval(50, 50, 250, 250, fill="#0000ff")

canvas1.tag_bind(circle, "<Button-1>", ship_clicked)


# Place the button in the window

# Place the canvas in the window
canvas1.pack(side="left")
canvas2.pack(side="right")
button.pack()

# Run the Tkinter event loop
window.mainloop()
