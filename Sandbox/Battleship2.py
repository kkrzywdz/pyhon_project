import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Load the image
image = pygame.image.load("./Data/T_Battleship.png")

# Load the images
images = []
images.append(pygame.image.load("./Data/T_Carrier.png"))
images.append(pygame.image.load("./Data/T_Battleship.png"))
images.append(pygame.image.load("./Data/T_Corvette.png"))
images.append(pygame.image.load("./Data/T_Cruiser.png"))
images.append(pygame.image.load("./Data/T_Destroyer.png"))
images.append(pygame.image.load("./Data/T_GunBoat.png"))
images.append(pygame.image.load("./Data/T_Submarine.png"))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the image to the screen
    x = 0
    y = 0
    for image in images:
        screen.blit(image, (x, y))
        y = y + 100

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
