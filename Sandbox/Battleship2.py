import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Set the board size
board_size = (20, 20)

# Set the square size
square_size = (18, 18)

# Set the board position
board_pos = (220, 20)

# define bord colors
board_color_enpty = 100, 100, 200
board_color_hit = 255, 0, 0
board_color_miss = 255, 255, 255
board_color_destroied = 63, 63, 63


# Load the images
RAWimages = []
RAWimages.append(pygame.image.load("./Data/T_Carrier.png"))
RAWimages.append(pygame.image.load("./Data/T_Battleship.png"))
RAWimages.append(pygame.image.load("./Data/T_Corvette.png"))
RAWimages.append(pygame.image.load("./Data/T_Cruiser.png"))
RAWimages.append(pygame.image.load("./Data/T_Destroyer.png"))
RAWimages.append(pygame.image.load("./Data/T_GunBoat.png"))
RAWimages.append(pygame.image.load("./Data/T_Submarine.png"))

backgroundLeft  = pygame.transform.scale (pygame.image.load("./Data/Background Left.png"), (200, 600))
backgroundRight = pygame.transform.scale (pygame.image.load("./Data/Background Right.png"), (200, 600))

images = []
for image in RAWimages:
    images.append(pygame.transform.scale (image, (200,50)))

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

    screen.fill((255, 255, 255))

    #adding backgrounds
    screen.blit(backgroundLeft, (0,0))
    screen.blit(backgroundRight, (600,0))

    # Blit the image to the screen
    x = 0
    y = 0
    for image in images:
        screen.blit(image, (x, y))
        y = y + 60

    x = 600
    y = 0
    for image in mirrorImages:
        screen.blit(image, (x, y))
        y = y + 60

    # Draw the board
    for i in range(board_size[0]):
        for j in range(board_size[1]):

            board_color = random.choice([board_color_miss,board_color_enpty, board_color_destroied, board_color_hit])

            pygame.draw.rect(screen, board_color, (board_pos[0] + i * square_size[0],
                                                       board_pos[1] + j * square_size[1],
                                                       square_size[0] - 1, square_size[1] - 1), 0)



    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
