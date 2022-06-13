def print_word():
    pass


class Game:
    def __init__(self, to_gues):
        self.word = to_gues
        self.tries = 3
        self.your_letters = []

    def add_new_letter(self, letter):
        letter = letter.lower()
        if letter not in self.your_letters:
            print("Adding " + letter + " to letters")
            self.your_letters.append(letter)

        else:
            print("Letter already in use :(")
            self.tries -= 1

    def print_your_letter(self):
        print("print_your_letter")
        print("Your Letters: [" + "] [".join(self.your_letters) + "]")

    def


if __name__ == '__main__':
    print("Started")
    game = Game("hangman")
    print(game.word)
    game.print_your_letter()
    game.add_new_letter("h")
    game.add_new_letter("H")
    game.add_new_letter("a")
    game.add_new_letter("N")
    game.add_new_letter("g")
    game.add_new_letter("k")
    game.print_your_letter()
