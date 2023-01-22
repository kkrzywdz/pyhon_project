import pygame
import random

# Initialize pygame
pygame.init()



# Define Board Class
class BoardClass():
    def __init__(self, name, board_pos, board_size):
        # Set object name
        self.name = name
        # Set the board position
        self.board_pos = board_pos
        # Set the board size
        self.board_size = board_size
        # Set the square size
        self.square_size = (18, 18)
        self.BoardColors = {
            "empty": (100, 100, 200),
            "hit": (255, 0, 0),
            "miss": (200, 200, 200),
            "destroyed": (63, 63, 63),
            "marked": (0, 128, 0)
            }
        self.field = [[0 for i in range(board_size[0])] for j in range(board_size[1])]
        self.ships = [[0 for i in range(board_size[0])] for j in range(board_size[1])]

    def initialize_test_ships(self):
        self.ships[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.ships[1] = [0, 6, 0, 0, 5, 5, 5, 5, 5, 0]
        self.ships[2] = [0, 6, 6, 0, 0, 0, 0, 0, 0, 0]
        self.ships[3] = [0, 6, 6, 0, 0, 0, 0, 0, 0, 0]
        self.ships[4] = [0, 0, 6, 0, 0, 0, 2, 0, 0, 0]
        self.ships[5] = [0, 0, 0, 0, 0, 0, 2, 0, 0, 0]
        self.ships[6] = [0, 0, 0, 0, 0, 0, 2, 0, 1, 0]
        self.ships[7] = [0, 0, 0, 0, 3, 0, 0, 0, 1, 0]
        self.ships[8] = [0, 0, 4, 0, 0, 3, 0, 0, 0, 0]
        self.ships[9] = [0, 4, 4, 4, 0, 0, 3, 0, 0, 0]

    def clicked(self, x_pos, y_pos):
        # check if board is clicked
        print(f"Board {self.name}")

        x_offset = x_pos - self.board_pos[0]
        y_offset = y_pos - self.board_pos[1]

        if 0 < x_offset < self.board_size[0]* (self.square_size[0]) and \
                0 < y_offset < self.board_size[1] * (self.square_size[1]):
            square_x = int(x_offset / (self.square_size[0]))
            square_y = int(y_offset / (self.square_size[1]))
            print(f"Board {self.name} clicked in [{square_x}][{square_y}]")
            if self.field[square_x][square_y] == 0:
                if self.ships[square_x][square_y] > 0 :
                    self.field[square_x][square_y] = 2
                    print("HIT")
                else:
                    self.field[square_x][square_y] = 1
                    print("MISS")
            else:
                print(f"[{square_x}][{square_y}] - already checked")



    def draw_board(self):
        # Draw the board
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                # board_color = random.choice(BoardColors)
                if self.field[i][j] == 0:
                    board_color = self.BoardColors["empty"]
                elif self.field[i][j] == 1:
                    board_color = self.BoardColors["miss"]
                elif self.field[i][j] == 2:
                    board_color = self.BoardColors["hit"]
                elif self.field[i][j] == 3:
                    board_color = self.BoardColors["destroyed"]
                else:
                    board_color = (0,0,0)

                pygame.draw.rect(screen, board_color, (self.board_pos[0] + i * self.square_size[0],
                                                       self.board_pos[1] + j * self.square_size[1],
                                                       self.square_size[0] - 1, self.square_size[1] - 1), 0)
    def print_fields(self):
        print (f"This is Board print field method for {self.name}")
        print (f"bord size {self.board_size[0]} x {self.board_size[1]}")
        for i in range (self.board_size[0]):
            for j in range(self.board_size[1]):
                print( self.field[i][j] , end = " ")
            print("")

# Set the window size
window_size = (800, 600)
p1BoardPos = (320, 20)
p2BoardPos = (320, 220)

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
nextTurn = pygame.transform.scale(pygame.image.load("./Data/fire_scale.png"), (29, 38))
nextTurn = pygame.transform.scale(pygame.image.load("./Data/fire_button.png"), (50, 50))

images = []
for image in RAWimages:
    images.append(pygame.transform.scale(image, (200, 50)))

# mirrored images
mirrorImages = []
for image in images:
    mirrorImages.append(pygame.transform.flip(image, True, False))

# Create new board -
# 220 for 20x20 board
# 320 for 10 x 10 board
p1Board = BoardClass("Player 1",p1BoardPos,  (10, 10))
p2Board = BoardClass("Player 2",p2BoardPos,  (10, 10))
p1Board.initialize_test_ships()
p1Board.initialize_test_ships()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 == left button

                pos_x, pos_y = pygame.mouse.get_pos()
                print(f"click! x={pos_x} y={pos_y} .")
                p1Board.clicked(pos_x, pos_y)
                p2Board.clicked(pos_x, pos_y)


    screen.fill((255, 255, 255))

    # adding backgrounds
    screen.blit(backgroundLeft, (0, 0))
    screen.blit(backgroundRight, (600, 0))
    screen.blit(nextTurn, (500, 500))

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

    #p1Board.field[random.randint(0, 9)][random.randint(0,9)] = random.randint(0,3)
    p2Board.field[random.randint(0, 9)][random.randint(0, 9)] = random.randint(0, 3)
    #p1Board.print_fields()

    p1Board.draw_board()
    p2Board.draw_board()

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
