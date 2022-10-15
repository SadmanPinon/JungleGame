
class Game():


    def __init__(self):
        self.board =  [[0 for col in range(7)] for row in range(9)] 
        for row in range(0,9):
            for col in range(0,7):
                self.board[row][col]=f"   X   "

    