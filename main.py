from Display import Display
from Game import Game

def main():
    game = Game()
    display = Display(game=game)
    display.drawBoard()

main()
