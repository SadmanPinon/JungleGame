from blessed import Terminal  


class Display():
    def __init__(self,game):
        self.game = game 
  

    
    def drawBoard(self):
        #Statically setting coordinates where special Squares will exist
        riverAreas = [
            (3,1),(3,2),(3,4),(3,5),
            (4,1),(4,2),(4,4),(4,5),
            (5,1),(5,2),(5,4),(5,5)
            ]
        trapAreas = [
            (0,2),(8,2),
            (0,4),(8,4),
            (1,3),(7,3)
            ]
        denAreas = [(0,3),(8,3)]

        
        term = Terminal() #Special String formatter 

        for row in range (0,9):
            #Declaring Vertical Grid 1-9
            print(f"{term.yellow}{row+1}",end="")          
            for col in range (0,7):
                if (row,col) in riverAreas:
                    print(f"{term.white_on_blue(f'{self.game.board[row][col]}')}",end="")
                elif (row,col) in trapAreas:
                    print(f"{term.white_on_red(f'{self.game.board[row][col]}')}",end="")
                elif (row,col) in denAreas:
                    print(f"{term.white_on_green(f'{self.game.board[row][col]}')}",end="")
                else:
                    print(f"{term.white(f'{self.game.board[row][col]}')}",end="")
            print("\n")
        for item in "ABCDEFG":
            print(f"    {term.yellow(f'{item}')}  ",end="")
        print("\n")


    def takeInput(self):
        print(self.game.dashboardText)
        userInput = input("Enter Input: ")
        return userInput
        
            

