from xmlrpc.client import Boolean
from Display import Display
from blessed import Terminal
from Model import *


class Game():
    '''View Controller of the Game. The Game Class concerns with transfer of information between the Model and Display class'''
    term = Terminal()  # Used for formatting terminal text
    # Dashboard Text display useful info regarding stages of the game (e.g piece occupied/player attacked)
    dashboardText = "Welcome to JungleBoard, just type 'help' if you need any."
    model = Model()  # Model class responsible for game logic

    def __init__(self):
        # Obtains and prepares the latest board from the model to present to display.
        self.board = self.updateBoard()

        self.display = Display(game=self)

    # Intent Functions ------------------------------------------------------------------------------------------------------------------------

    def start(self) -> None:
        '''Starts the game for user to Begin Playing'''
        self.__feedbackLoop()

    def updateBoard(self) -> None:
        '''
        Based on the data of the model, the board's structure is created. in this function
        @returns The updated board as arrays of strings
        '''
        board = [[0 for col in range(7)] for row in range(9)]
        for row in range(0, 9):
            for col in range(0, 7):
                piece = self.model.board[row][col].occupiedPiece
                if piece == None:
                    board[row][col] = f"  X  "
                else:
                    # Assign Pieces its subscript based on which team they are in
                    if piece.team == Player.One:
                        if piece == self.model.selectedPiece:

                            board[row][col] = self.term.yellow_bold_underline(
                                f'  {piece.type.value}\u2081 ')
                        else:
                            board[row][col] = self.term.pink(
                                f'  {piece.type.value}\u2081 ')
                    else:
                        if piece == self.model.selectedPiece:
                            board[row][col] = self.term.yellow_bold_underline(
                                f'  {piece.type.value}\u2082 ')
                        else:
                            board[row][col] = self.term.purple(
                                f'  {piece.type.value}\u2082 ')
        return board

    # Auxlery Functions ------------------------------------------------------------------------------------------------------------------------

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

    def __processInput(self, input: str) -> None:
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
        elif input == "HELP":
            self.__printHelp()
            return

        elif len(input) != 2:
            self.dashboardText = f"Invalid Input! Your input should be 2 characters, you gave {len(input)}"
        elif not (input[0] in "123456789" and input[1] in "ABCDEFG"):
            self.dashboardText = f"Invalid Input! String format needs to be Row,Column e.g '3C' you entered {input} "

        else:
            # Valid Move
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
        elif self.model.board[8][3].occupiedPiece != None:
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

            if input == "EXIT":
                print(
                    f"{self.term.white_on_red('Game is terminated! Thanks for playing!')}")
                break

            self.__processInput(input)

        if self.model.winner is None:
            # For cases when game is forced to terminate early without any winner being set

            return

        winner = "Player 1" if self.model.winner == Player.One else "Player 2"
        print(f"Game Finished! {winner} Wins!")

    def __printHelp(self) -> None:
        '''Prints the help command for user's reference'''
        print("--THE GAME RULES--\n\nThe Board is of  9 x 7 configuration with each rows marked with numbers 1-7 and each column marked with characters A-G.")
        print("Users select a piece by inputting the appropriate row,column pair.\nFor example, The Rat Piece of Player 1 is in the Coordinate 3A.\nSimilarly, The Rat Piece of Player 2 is in the Coordinate 7G.\n")
        print("Each Piece in game is represented as a Number, Subscript pair.\nThe number represents the Character ( and the rank) of the piece.\n\nBelow table lists the appropriate Character for each power: ")
        print("-----------------------")
        print("|   Rank   |Character |")
        print("-----------------------")
        print("|    1     |    Rat   |")
        print("-----------------------")
        print("|    2     |    Cat   |")
        print("-----------------------")
        print("|    3     |    Dog   |")
        print("-----------------------")
        print("|    4     |   Wolf   |")
        print("-----------------------")
        print("|    5     |  Leopard  |")
        print("-----------------------")
        print("|    6     |   Tiger  |")
        print("-----------------------")
        print("|    7     |    Lion   |")
        print("-----------------------")
        print("|    8     | Elephant |")
        print("-----------------------")
        print("In general, Pieces of higher ranks can capture pieces of equal or lower rank.\n However, as per game rules,  exceptions apply :\n\nElephant can not capture enemy Rat Piece despite higher rank ( 8 > 1 )\nRat can capture enemy Elephant piece despite lower rank ( 1 > 8 )\nAny piece can capture an opponent piece when they are trapped.")
        print("The subscript indicates the Player to which the piece belongs to.\nThe color also indicates the Player to which the piece belongs to ( Pink for 1, Purple for 2).\n\n")
        print("--COMMANDS PROVIDED--")
        print("All Commands are Case insensitive, but space sensitive.\n\n -> “RowColumn”:  Appropriate board position  “coordinate ”( e.g “3A” , “7D”) Without any space.\n\nUsers can use this command to ")
        print("1)Select Piece: Only applicable when no Piece is currently selected by the player or the coordinate given by the command does indeed have a valid piece that can be selected ( e.g doesn’t belong to the other team).\nSelected piece will be highlighted and confirmation prompts will be given in dashboard text.\n")
        print("2)Move Piece: Only applicable when a particular piece is already selected. If the coordinates specified obey the rules of the game, a move and/or capture may be performed.\n Status can be checked by checking the dashboard.\n")
        print("U : Unselects a selected piece ( if any). Unselected piece will lose its highlight")

        #   '''

        #     Introduction

        #   '''
