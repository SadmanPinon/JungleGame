
from Constants import *

class Display():
    '''
    Displays the State of the board to the user. and recieves user input command
    '''
    def __init__(self,game):
        self.game = game 
  

    
    def drawBoard(self) -> None:
        '''
         Statically setting coordinates where special Squares will exist
        '''
       
        

        
         #Special String formatter 
        term = self.game.term
        for row in range (0,9):
            #Declaring Vertical Grid 1-9
            print(f"{term.yellow}{row+1}",end="")          
            for col in range (0,7):
                if (row,col) in riverAreas:
                    print(f"{term.on_blue(f'{self.game.board[row][col]}')}",end="")
                elif (row,col) in trapAreas:
                    print(f"{term.on_red(f'{self.game.board[row][col]}')}",end="")
                elif (row,col) in denAreas:
                    print(f"{term.on_green(f'{self.game.board[row][col]}')}",end="")
                else:
                    print(f"{term.white(f'{self.game.board[row][col]}')}",end="")
            print("\n")
        print(" ",end="")
        for item in "ABCDEFG":
            print(f"  {term.yellow(f'{item}')}  ",end="")
        print("\n")


    def takeInput(self) -> str:
        term = self.game.term
        '''
        Takes User Input
        @Returns formatted string indicating user input
        '''
        print(self.game.dashboardText)
        player = f"{term.on_pink('Player 1')}" if self.game.model.playerTurn == Player.One else f"{term.on_purple('Player 2')}"
        print(f"{player}'s Turn")       
        userInput = input("Enter Input: ")
        return userInput.upper().strip()
        
            

