import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Set the board size
board_size = (10, 10)

# Set the square size
square_size = (20, 20)

# Set the board position
board_pos = (100, 100)

# define bord colors
board_color_enpty = 100, 100, 200
board_color_hit = 255, 0, 0
board_color_miss = 255, 255, 255
board_color_destroied = 63, 63, 63


# Load the images
images = []
images.append(pygame.image.load("./Data/T_Carrier.png"))
images.append(pygame.image.load("./Data/T_Battleship.png"))
images.append(pygame.image.load("./Data/T_Corvette.png"))
images.append(pygame.image.load("./Data/T_Cruiser.png"))
images.append(pygame.image.load("./Data/T_Destroyer.png"))
images.append(pygame.image.load("./Data/T_GunBoat.png"))
images.append(pygame.image.load("./Data/T_Submarine.png"))

# mirrored images
mirrorImages = []
for image in images:
    mirrorImages.append(pygame.transform.flip(image, True, False))

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

    # Draw the board
    for i in range(board_size[0]):
        for j in range(board_size[1]):

            board_color = random.choice([board_color_miss,board_color_enpty, board_color_destroied, board_color_hit])

            pygame.draw.rect(screen, board_color, (board_pos[0] + i * square_size[0],
                                                       board_pos[1] + j * square_size[1],
                                                       square_size[0] - 1, square_size[1] - 1), 0)
            #pygame.Surface.fill((255, 0, 0))


    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
