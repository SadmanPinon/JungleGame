from Display import Display
from blessed import Terminal  
from Model import * 

class Game():
    term = Terminal()
    dashboardText = "Welcome to JungleBoard"
    model = Model()
    def __init__(self):
        self.board = self.updateBoard()   
        
        self.display = Display(game=self)        
        

    def start(self):
        self.__feedbackLoop()
        




    ##Intent Functions ------------------------------------------------------------------------------------------------------------------------
    def __feedbackLoop(self):

        while not self.__IsFinished():
            self.display.drawBoard()
            input = self.display.takeInput()
            self.__processInput(input)


    def updateBoard(self):
        board = [[0 for col in range(7)] for row in range(9)] 
        for row in range(0,9):
            for col in range(0,7):
                piece = self.model.board[row][col].occupiedPiece
                if  piece == None:
                    board[row][col]=f"  X  "
                else: 
                    #Assign Pieces its subscript based on which team they are in 
                    if piece.team == Player.One:
                        board[row][col]=self.term.pink(f'  {piece.type.value}\u2081 ')
                    else: 
                        board[row][col]=self.term.purple(f'  {piece.type.value}\u2082 ')
                    

                
        return board

    def __IsFinished(self):
        return False 
    
    def __processInput(self,input):
        if len(input.strip()) != 2:            
            self.dashboardText = f"Invalid Input! Your input should be 2 characters, you gave {len(input.strip())}"

    

    

    


    