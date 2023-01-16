import pygame
import random

# Initialize pygame
pygame.init()

# Board colors
BoardColors = {
    "empty": (100, 100, 200),
    "hit": (255, 0, 0),
    "miss": (255, 255, 255),
    "destroyed": (63, 63, 63)
}


# Define Board Class
class BoardClass:
    def __int__(self, board_pos):
        # Set the board position
        self.board_pos = board_pos
        # Set the board size
        self.board_size = (20, 20)
        # Set the square size
        square_size = (18, 18)

    def draw_board(self):
        # Draw the board
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                board_color = random.choice(BoardColors)
                pygame.draw.rect(screen, board_color, (self.board_pos[0] + i * self.square_size[0],
                                                       self.board_pos[1] + j * self.square_size[1],
                                                       self.square_size[0] - 1, self.square_size[1] - 1), 0)


# Set the window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# define bord colors


# Load the images
RAWimages = []
RAWimages.append(pygame.image.load("./Data/T_Carrier.png"))
RAWimages.append(pygame.image.load("./Data/T_Battleship.png"))
RAWimages.append(pygame.image.load("./Data/T_Corvette.png"))
RAWimages.append(pygame.image.load("./Data/T_Cruiser.png"))
RAWimages.append(pygame.image.load("./Data/T_Destroyer.png"))
RAWimages.append(pygame.image.load("./Data/T_GunBoat.png"))
RAWimages.append(pygame.image.load("./Data/T_Submarine.png"))

backgroundLeft = pygame.transform.scale(pygame.image.load("./Data/Background Left.png"), (200, 600))
backgroundRight = pygame.transform.scale(pygame.image.load("./Data/Background Right.png"), (200, 600))

images = []
for image in RAWimages:
    images.append(pygame.transform.scale(image, (200, 50)))

# mirrored images
mirrorImages = []
for image in images:
    mirrorImages.append(pygame.transform.flip(image, True, False))

# Create new board
p1Board = BoardClass(200, 200)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # adding backgrounds
    screen.blit(backgroundLeft, (0, 0))
    screen.blit(backgroundRight, (600, 0))

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

    p1Board.draw_board()

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
