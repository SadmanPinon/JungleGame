from Display import Display
class Game():

    dashboardText = "Welcome to JungleBoard"
    def __init__(self):
        self.board = self.__initalizeBoard()      
        
        self.display = Display(game=self)        
        

    def start(self):
        self.__feedbackLoop()
        




    ##Intent Functions ------------------------------------------------------------------------------------------------------------------------
    def __feedbackLoop(self):

        while not self.__IsFinished():
            self.display.drawBoard()
            input = self.display.takeInput()
            self.__processInput(input)


    def __initalizeBoard(self):
        board = [[0 for col in range(7)] for row in range(9)] 
        for row in range(0,9):
            for col in range(0,7):
                board[row][col]=f"   X   "
        return board

    def __IsFinished(self):
        return False 
    
    def __processInput(self,input):
        if len(input.strip()) != 2:
            
            self.dashboardText = f"Invalid Input! Your input should be 2 characters, you gave {len(input.strip())}"

    

    

    


    