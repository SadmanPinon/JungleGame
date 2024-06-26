from turtle import pos
from xmlrpc.client import Boolean
from Constants import *


class Model():
    '''The Model has the Logical state of the game, including board state, player turn and winner status. It uses two Helper classes, Piece and Square
    to maintain and update the logic of the game.
    '''

    def __init__(self) -> None:
        self.board = [[0 for col in range(7)] for row in range(9)]
        self.__initializeBoard()
        self.__assignPieces()
        self.selectedPiece = None
        self.deadPiecesPlayerOne = 0
        self.deadPiecesPlayerTwo = 0
        self.playerTurn = Player.One
        self.winner = None

    # Auxlery Functions ------------------------------------------------------------------------------------------------------------------------

    def __initializeBoard(self) -> None:
        '''Initializes the board to it's newest State'''
        for row in range(9):
            for col in range(0, 7):
                if (row, col) in riverAreas:
                    self.board[row][col] = Square(
                        type=SquareType.Water, row=row, col=col, model=self)
                elif (row, col) in trapAreas:
                    self.board[row][col] = Square(
                        type=SquareType.Trap, row=row, col=col, model=self)
                elif (row, col) in denAreas:
                    self.board[row][col] = Square(
                        type=SquareType.Den, row=row, col=col, model=self)
                else:
                    self.board[row][col] = Square(
                        type=SquareType.Normal, row=row, col=col, model=self)

    def __assignPieces(self) -> None:
        '''Assigns Pieces to it's initial position by Creating Piece instances and assigning them to the appropriate
            square in the board array.
        '''
        self.board[0][0].occupiedPiece = Piece(
            player=Player.One, location=self.board[0][0], type=PieceType.Lion)
        self.board[0][6].occupiedPiece = Piece(
            player=Player.One, location=self.board[0][6], type=PieceType.Tiger)
        self.board[1][1].occupiedPiece = Piece(
            player=Player.One, location=self.board[1][1], type=PieceType.Dog)
        self.board[1][5].occupiedPiece = Piece(
            player=Player.One, location=self.board[1][5], type=PieceType.Cat)
        self.board[2][0].occupiedPiece = Piece(
            player=Player.One, location=self.board[2][0], type=PieceType.Rat)
        self.board[2][2].occupiedPiece = Piece(
            player=Player.One, location=self.board[2][2], type=PieceType.Leopard)
        self.board[2][4].occupiedPiece = Piece(
            player=Player.One, location=self.board[2][4], type=PieceType.Wolf)
        self.board[2][6].occupiedPiece = Piece(
            player=Player.One, location=self.board[2][6], type=PieceType.Elephant)

        self.board[8][6].occupiedPiece = Piece(
            player=Player.Two, location=self.board[8][6], type=PieceType.Lion)
        self.board[8][0].occupiedPiece = Piece(
            player=Player.Two, location=self.board[8][0], type=PieceType.Tiger)
        self.board[7][5].occupiedPiece = Piece(
            player=Player.Two, location=self.board[7][5], type=PieceType.Dog)
        self.board[7][1].occupiedPiece = Piece(
            player=Player.Two, location=self.board[7][1], type=PieceType.Cat)
        self.board[6][6].occupiedPiece = Piece(
            player=Player.Two, location=self.board[6][6], type=PieceType.Rat)
        self.board[6][4].occupiedPiece = Piece(
            player=Player.Two, location=self.board[6][4], type=PieceType.Leopard)
        self.board[6][2].occupiedPiece = Piece(
            player=Player.Two, location=self.board[6][2], type=PieceType.Wolf)
        self.board[6][0].occupiedPiece = Piece(
            player=Player.Two, location=self.board[6][0], type=PieceType.Elephant)

    def _getCoordinate(self, position: str) -> tuple[int, int]:
        '''
        Converts Human friendly coordinate (7A) to machine friendly coordinate (row=6,col=0)
        @Returns Tuple of (Row,Column) in Integer Format
        '''

        row = int(position[0])-1
        column = columnDict[position[1]]
        return (row, column)

      # Intent Functions ------------------------------------------------------------------------------------------------------------------------

    def selectPiece(self, position: str) -> str:
        '''
        Given a board position, this function attempts to select the piece in that position
        @Returns String indicating wether the operation was succesful 
        '''
        coordinate = self._getCoordinate(position=position)
        piece = self.board[coordinate[0]][coordinate[1]].occupiedPiece

        if piece == None:
            return f"No Piece Exists in position {position} "

        if piece.team != self.playerTurn:
            return f"You can't choose Opponent's Piece!"

        self.selectedPiece = piece

        return f"You have selected {piece.type}"

    def attemptMove(self, position: str = input) -> str:
        '''
         Given a board position, this function attempts to move into the particular board position
         @Returns String indicating wether the operation was succesful
        '''
        coordinate = self._getCoordinate(position=position)
        square = self.board[coordinate[0]][coordinate[1]]
        result = square.tryToOccupy(piece=self.selectedPiece)

        return result

    def unselect(self) -> str:
        '''
         Unselects the currently selected Piece
         @Returns String indicating wether the operation was succesful
        '''
        self.selectedPiece = None
        return "Piece unselected"

    def isIntervened(self, X1: tuple[int, int], Y1: tuple[int, int]) -> Boolean:
        '''
         Given a Origin Position X1 and Jump Target Position Y1, this function determines if 
         there are pieces in the intervening squares between the two squares. 
         @Returns Boolean indicating if there is intervening square or not. 
        '''
        matchingIndex = 0 if X1[0] == Y1[0] else 1
        # If row same then col differingIndex and vice Versa
        differingIndex = 1 if X1[0] == Y1[0] else 0

        startingIndex = X1[differingIndex] if X1[differingIndex] < Y1[differingIndex] else Y1[differingIndex]
        startingIndex += 1
        endingIndex = X1[differingIndex] if X1[differingIndex] >= Y1[differingIndex] else Y1[differingIndex]

        for index in range(startingIndex, endingIndex):

            if matchingIndex == 0:

                if self.board[X1[0]][index].occupiedPiece != None:  # Intervening square found
                    return True
            else:
                if self.board[index][X1[1]].occupiedPiece != None:  # Intervening square found
                    return True

        return False

    def changeTurns(self) -> None:
        '''
         Switches Player Turns         
        '''
        # Change to 1 if 2 is playing otherwise 1
        self.playerTurn = Player.One if self.playerTurn == Player.Two else Player.Two

        # Deselects any selected piece
        self.selectedPiece = None


class Piece():
    '''
    This class represents an inidividual Piece in the game. 
    '''

    def __init__(self, type, location, player) -> None:
        self.team: Player = player
        self.type: PieceType = type
        self.location: Square = location

    '''Custom Equal to function that checks if the two pieces are from the same team and 
        if their type is same to determine if they are the same. 
        @Returns Boolean indicating if two pieces are equal or not. 
    '''

    def __eq__(self, other) -> Boolean:
        if (other == None):
            return False
        return (self.team == other.team) and (self.type == other.type)

    def attack(self, opponent) -> Boolean:
        '''
        Determines if a Piece can attack it's Opponent Piece
        @Returns Boolean indicating if the attack is possible or not
        '''
        # Doesn't check if same or diff team, assumes its diff team.
        # In general if higher (or eq) rank...
        if self.type.value >= opponent.type.value:
            # Elephant cant eat rat
            if not (self.type == PieceType.Elephant and opponent.type == PieceType.Rat):
                return True  # Eat
        elif (self.type == PieceType.Rat and opponent.type == PieceType.Elephant):  # Rat can eat Elephant
            return True  # Eat
        return False


class Square():
    '''
        The Square class represents an individual unit of the board. 
        This Square class is responsible for housing the pieces as well as checking most of the rules 
        of the game. 
    '''

    def __init__(self, type, row, col, model) -> None:
        self.type: SquareType = type
        self.occupiedPiece: Piece = None
        self.row = row
        self.col = col
        self.model = model

    # Auxlery Functions ------------------------------------------------------------------------------------------------------------------------

    def _jumpElligible(self, piece: Piece) -> Boolean:
        '''
        Checks if a piece is elligible to make the jump
        @Returns Boolean indivating the elligibility
        '''

        # Is the piece a Tiger or a Lion?
        return (piece.type == PieceType.Tiger or piece.type == PieceType.Lion)

    def _withinOneSquare(self, piece: Piece) -> Boolean:
        '''
        Implements the rule that makes sure the piece is
        moving ONE square only verticall/horizonally but not diagonally.
        @Returns Boolean  indiciating if the piece is within one square.
        '''

        currentLocation = piece.location
        if currentLocation.row == self.row:
            # If same row...
            if abs(currentLocation.col - self.col) == 1:  # Col difference can only be 1
                return True
            else:
                return False  # More than one square away
        elif currentLocation.col == self.col:
            # If same col...
            if abs(currentLocation.row - self.row) == 1:  # Row difference can only be 1
                return True
            else:
                return False  # More than one square away
        else:
            return False  # Diagonally or too far away.

    def _ownDen(self, piece: Piece) -> Boolean:
        ''''
        Checks if piece is an ally piece trying to move to it's own den.
        @Returns Boolean Indicating the Piece attempted to move it it's own team's den
        '''

        if self.type == SquareType.Den:  # Checks if the square is a den square to begin with
            # Checks if den and piece are from same team
            if (piece.team == Player.One) and (self.row == 0):
                return True
            elif (piece.team == Player.Two) and (self.row == 8):
                return True
        return False

    def _waterElligible(self, piece: Piece) -> Boolean:
        # Only concerns scenario when a rat tries to move into a water.
        return piece.type == PieceType.Rat
        # Water Square check needs to be implemented exertnally before invoking the function
        # This func assumes that the square is water square.

    def _validJump(self, piece: Piece) -> Boolean:
        '''
        Will check if elligible piece is making a valid jump! assume it's an elligible piece already. ( by using _jumpElligible())
        X1 = Oirign, Y1 = Destination
        @Returns Boolean Indicating if the jump is valid
        '''

        X1 = (piece.location.row, piece.location.col)
        Y1 = (self.row, self.col)

        for pair in jumpPoints:
            if X1 in pair and Y1 in pair:  # Both Starting and Ending condition match
                if not self.model.isIntervened(X1=X1, Y1=Y1):

                    return True

                return False
        return False
    
    def _validTrap(self,piece: Piece) -> Boolean: 
        '''
        Valid Trap ensures that 

        1) The Piece itself is a trap square
        2) The occupied piece belongs to an enemy team. 

        @Returns Boolean indicating if this is a valid situation where an attack can be performed
        on a trapped piece. 
        '''
        if self.type == SquareType.Trap: #If the square is a trap square 
            if piece.team == Player.One: 
                return self.row <3 # If trap belongs to Player 1 
            elif piece.team == Player.Two: 
                return self.row >6 # If trap belongs to player 2 
        return False 

    def _attemptAttack(self, piece: Piece) -> str:
        '''
         Will check if the attack is elligible
        Scenarios: 
            1. Cross Border Attack Check 
            2. If Rank is followed 
            3. If Victim in Den Square
            4. Jump attack in presence of intervening square.
        @Returns String Indicating the result of attempt
        '''

        # 3
        if (self._validTrap(piece=piece)):
            return self._attack(piece=piece)
        # 1
        elif (piece.type == PieceType.Rat and self._crossBorderAttack(piece=piece)):
            return "Cross-Border attack isn't allowed!"

        # 2
        elif piece.attack(self.occupiedPiece):
            return self._attack(piece=piece)

        return "Inelligible Attack"

    def _attack(self, piece: Piece) -> str:
        '''
        Attacks and occupies
        @Returns String indicating the result of attack attempt
        '''
        statement = f"Succesfully attacked {self.occupiedPiece.type}"
        # Logs for model to track state of game
        if piece.type == Player.One:
            self.model.deadPiecesPlayerTwo += 1
        else:
            self.model.deadPiecesPlayerOne += 1

        # Removes Reference
        piece.location.occupiedPiece = None
        self.occupiedPiece = piece
        piece.location = self
        # Changes Player Turns
        self.model.changeTurns()
        return statement

    def _crossBorderAttack(self, piece: Piece) -> Boolean:
        '''
        Checks logic on if the attack is a cross border attack. 
        The function Assumes provided piece is a rat piece 
        @Returns Boolean indicating if it's a cross border attack
        '''

        return self.type != piece.location.type

    def _occupy(self, piece: Piece) -> str:
        # Called when its determined that occupying this square is a legal move.
        oldLocation = piece.location
        self.occupiedPiece = piece
        piece.location = self
        emptied = oldLocation.empty()
        if emptied:
            colString = "ABCDEFG"
            colString = colString[self.col]
            self.model.changeTurns()
            return f"Succesfully moved piece to square {self.row+1,colString}"
        return "There was a problem, couldn't leave old square"

    # Intent Functions ------------------------------------------------------------------------------------------------------------------------

    def tryToOccupy(self, piece: Piece) -> str:
        '''
        Attempts to occupy a Square by the string.
        @Returns the result of the occupation move
        '''

        # If vacant square, checks if further rules are followed
        # If one square rule is followed
        if not self._withinOneSquare(piece):
            # If not within one square, it could be a jump elligible piece
            if not self._jumpElligible(piece):
                return "Invalid destination. You are out of your range."
            # Meaning a jump elligible piece that's outside of one range, checking if the jump is valid
            elif not self._validJump(piece):
                return "Invalid Jump attempted!"
        elif self._ownDen(piece=piece):
            return "Illegal Move! You tried to move to your own den square"
        elif (self.type == SquareType.Water) and (not self._waterElligible(piece=piece)):
            return "Illegal Move, You can't move into water. Only Rat(1) Can!"

        # If already a piece exists in the square
        if self.occupiedPiece != None:
            if self.occupiedPiece.team == piece.team:  # Checks if collison with own piece
                if self.occupiedPiece == piece:
                    return "You are already here"
                return "This square is already occupied by your Piece"
            else:
                # Collison with enemy piece, checking attack elligibility
                return self._attemptAttack(piece=piece)

        # <-----Need further logic before calling this
        outcome = self._occupy(piece=piece)
        return outcome

    def empty(self) -> Boolean:
        '''
        Called to remove piece from old square when located to new square
        @Returns Boolean on if the operation was succesful 
        //ERRCD: 23
        '''

        piece = self.occupiedPiece
        # If there is an occupied piece which is referencing another square
        if piece != None and piece.location != self:
            self.occupiedPiece = None
            return True
        return False
