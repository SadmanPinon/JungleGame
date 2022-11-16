from xmlrpc.client import Boolean
from Display import Display
from blessed import Terminal  
from Model import * 

class Game():
    '''View Controller of the Game. The Game Class concerns with transfer of information between the Model and Display class'''
    term = Terminal() #Used for formatting terminal text
    dashboardText = "Welcome to JungleBoard" #Dashboard Text display useful info regarding stages of the game (e.g piece occupied/player attacked)
    model = Model() #Model class responsible for game logic
    def __init__(self):
        self.board = self.updateBoard()  #Obtains and prepares the latest board from the model to present to display.
        
        self.display = Display(game=self)        
        

    




    ##Intent Functions ------------------------------------------------------------------------------------------------------------------------
    def start(self) -> None:
        '''Starts the game for user to Begin Playing'''
        self.__feedbackLoop()
        

    def updateBoard(self) -> None:
        '''
        Based on the data of the model, the board's structure is created. in this function
        @returns The updated board as arrays of strings
        '''
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
                        
                    

                
    ## Auxlery Functions ------------------------------------------------------------------------------------------------------------------------

    def __isFinished(self) -> Boolean:
        '''
        Checks the two logic of the game to determine if the game is finsihed
        @returns Boolean indicating if the game is finished. 
        '''
        if self.model.deadPiecesPlayerOne == 9:
            self.model.winner = Player.Two
            return True
        elif self.model.deadPiecesPlayerTwo == 9: 
            self.model.winner = Player.One 
            return True 
        elif self._isDenCaptured():
            return True 
        return False 
    
    def __processInput(self,input:str) -> None:
        '''
        Processes the input for it's validity and after which passes to the appropriate model function to take action 
        Updates board once input is processed to view the newest state of game.
        '''
        input = input.strip()

        if input == "U":
            
            if self.model.selectedPiece == None:
                self.dashboardText = "No Piece is currently selected"
                return 
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

    def _isDenCaptured(self) -> Boolean:
        '''
        Checks if both the boards have presence of enemy Piece
        Assumes a den can't be occupied by same team

        @Returns Boolean on wether the Den is captured or not
        '''
        if self.model.board[0][3].occupiedPiece != None:
            self.model.winner = Player.Two
            return True
        elif  self.model.board[8][3].occupiedPiece != None: 
            self.model.winner = Player.One 
            return True 
        return False 
        
    
    def __feedbackLoop(self) -> None:
        '''The Feedback Loop initiates the continous chain of Input -> State Update -> Output.
        This continues until it's determined that the game is finished. 
        
        '''
        while not self.__isFinished():            
            self.display.drawBoard()
            input = self.display.takeInput()
            self.__processInput(input)
        
        winner = "Player 1" if self.model.winner == Player.One else "Player 2"
        print(f"Game Finished! {winner} Wins!")
           
    

        

          
        




        

        


    

    


    