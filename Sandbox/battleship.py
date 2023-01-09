from array import *

import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("1000x600")

# Create a global variable to track the state of the canvas
state = 0
state2 = 0

seeP1 = [0] * 100
seeP2 = [0] * 100

print(f"first pos {seeP1[1]}")


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


# create frames to arange canvas
frameP1 = tk.Frame(window, bg="#eeeeee")
frameP2 = tk.Frame(window, bg="#eeeeee")

frameP1.pack(side="left")
frameP2.pack(side="right")

# Create a canvas to draw on
canvas1 = tk.Canvas(frameP1, width=220, height=400, bg="#ffffff")
canvas2 = tk.Canvas(frameP2, width=220, height=400, bg="#ffffff")
canvasShipP1 = tk.Canvas(frameP1, width=220, height=800, bg="#ffffff")
canvasShipP2 = tk.Canvas(frameP2, width=220, height=800, bg="#ffffff")

# Draw the grid
x = 10
y = 10
for seeColor in seeP1:
    seeFill = "#0000AA"
    if seeColor == 1:
        fieldColor = "#ffffff"
    canvas1.create_rectangle(x, y, x + 20, y + 20, fill=seeFill)
    x = x + 20
    if x > 200:
        x = 10
        y = y + 20

# Draw the grid
x = 10
y = 10
for seeColor in seeP2:
    seeFill = "#0000AA"
    if seeColor == 1:
        fieldColor = "#ffffff"
    canvas2.create_rectangle(x, y, x + 20, y + 20, fill=seeFill)
    x = x + 20
    if x > 200:
        x = 10
        y = y + 20



#for x in range(0, 201, 20):
#    for y in range(0, 201, 20):
#        canvas1.create_rectangle(x, y, x + 20, y + 20, fill="#0000AA")
#        canvas2.create_rectangle(x, y, x + 20, y + 20, fill="#0000AA")





# Create a button
button = tk.Button(text="Click me!", command=button_clicked)

# load images and reduce size
imageCarrier = tk.PhotoImage(file=".\Data\T_Carrier.png").subsample(2, 2)
imageBattle = tk.PhotoImage(file=".\Data\T_Battleship.png").subsample(2, 2)
imageCorvette = tk.PhotoImage(file=".\Data\T_Corvette.png").subsample(2, 2)
imageCruiser = tk.PhotoImage(file=".\Data\T_Cruiser.png").subsample(2, 2)
imageDestroyer = tk.PhotoImage(file=".\Data\T_Destroyer.png").subsample(2, 2)
imageGunBoat = tk.PhotoImage(file=".\Data\T_GunBoat.png").subsample(2, 2)
imageSubmarine = tk.PhotoImage(file=".\Data\T_Submarine.png").subsample(2, 2)

# populate canvas with ship images
canvasShipP1.create_image(100, 50, image=imageCarrier)
canvasShipP1.create_image(100, 100, image=imageBattle)
canvasShipP1.create_image(100, 150, image=imageCruiser)
canvasShipP1.create_image(100, 200, image=imageDestroyer)
canvasShipP1.create_image(100, 250, image=imageGunBoat)
canvasShipP1.create_image(100, 300, image=imageSubmarine)
canvasShipP1.create_image(100, 350, image=imageCorvette)

canvasShipP2.create_image(100, 50, image=imageCarrier)
canvasShipP2.create_image(100, 100, image=imageBattle)
canvasShipP2.create_image(100, 150, image=imageCruiser)
canvasShipP2.create_image(100, 200, image=imageDestroyer)
canvasShipP2.create_image(100, 250, image=imageGunBoat)
canvasShipP2.create_image(100, 300, image=imageSubmarine)
canvasShipP2.create_image(100, 350, image=imageCorvette)


# Place the Entry in the window
entry = tk.Entry(window)
entry.pack()  # (side="left")


# Bind a function to the ship's hull
def ship_clicked(event):
    print("Ship was clicked at", event.x, event.y)
    canvas2.create_rectangle(event.x, event.y, event.x + 20, event.y + 20, fill="#0000ff")


# Create a blue circle on the canvas
# circle = canvas1.create_oval(50, 50, 250, 250, fill="#0000ff")
# canvas1.tag_bind(circle, "<Button-1>", ship_clicked)

# Place the button in the window
button.pack()
# Place the canvas in the left frame
canvas1.pack(side="right")
canvasShipP1.pack(side="left")
# Place the canvas in the right frame
canvas2.pack(side="left")
canvasShipP2.pack(side="right")

# Run the Tkinter event loop
window.mainloop()
