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
        
        winner = "Player 1" if self.model.winner == Player.One else "Player 2"
        print(f"Game Finished! {winner} Wins!")

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
                        if piece == self.model.selectedPiece: 
                            
                            board[row][col]=self.term.yellow_bold_underline(f'  {piece.type.value}\u2081 ')
                        else:
                            board[row][col]=self.term.pink(f'  {piece.type.value}\u2081 ')
                    else:
                        if piece == self.model.selectedPiece:                                                      
                            board[row][col]=self.term.yellow_bold_underline(f'  {piece.type.value}\u2082 ')
                        else:
                            board[row][col]=self.term.purple(f'  {piece.type.value}\u2082 ')
        return board
                        
                    

                
        

    def __IsFinished(self):
        if self.model.deadPiecesPlayerOne == 9:
            self.model.winner = Player.Two
            return True
        elif self.model.deadPiecesPlayerTwo == 9: 
            self.model.winner = Player.One 
            return True 
        elif self._isDenCaptured():
            return True 
        return False 
    
    def __processInput(self,input):
        input = input.strip()

        if input == "U":
            if self.model.selectedPiece == None:
                self.dashboardText = "No Piece is currently selected"
            self.dashboardText = self.model.unselect()
        elif len(input) != 2:            
            self.dashboardText = f"Invalid Input! Your input should be 2 characters, you gave {len(input)}"
        elif not (input[0]  in "123456789" and input[1]  in "ABCDEFG"):                
            self.dashboardText = f"Invalid Input! String format needs to be Row,Column e.g '3C' you entered {input} "
        
        else:
            #Valid Move
            if self.model.selectedPiece == None:           
                self.dashboardText = self.model.selectPiece(position=input)
                
            else:
                self.dashboardText = self.model.attemptMove(position=input)   

        self.board = self.updateBoard() 

    def _isDenCaptured(self):
        #Checks if both the boards have presence of enemy Piece
        #Assumes a den can't be occupied by same team
        if self.model.board[0][3].occupiedPiece != None:
            self.model.winner = Player.Two
            return True
        elif  self.model.board[8][3].occupiedPiece != None: 
            self.model.winner = Player.One 
            return True 
        return False 
        

           
    

        

          
        




        

        


    

    


    