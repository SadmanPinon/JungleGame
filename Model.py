from turtle import pos
from Constants import * 
 

class Model():
    def __init__(self) -> None:
        self.board  = [[0 for col in range(7)] for row in range(9)] 
        self.__initializeBoard()
        self.__assignPieces()
        self.selectedPiece = None 
        # self.playerTurn = Player.One
        
    def __initializeBoard(self):
        for row in range(9):
            for col in range (0,7):
                if (row,col) in riverAreas:
                    self.board[row][col] = Square(type = SquareType.Water,row=row,col=col)
                elif (row,col) in trapAreas:
                    self.board[row][col] = Square(type = SquareType.Trap,row=row,col=col)
                elif (row,col) in denAreas:
                    self.board[row][col] = Square(type = SquareType.Den,row=row,col=col)
                else:
                    self.board[row][col] = Square(type = SquareType.Normal,row=row,col=col)
    def __assignPieces(self):
        self.board[0][0].occupiedPiece = Piece(player = Player.One,location=self.board[0][0],type=PieceType.Lion)
        self.board[0][6].occupiedPiece = Piece(player = Player.One,location=self.board[0][6],type=PieceType.Tiger)
        self.board[1][1].occupiedPiece = Piece(player = Player.One,location=self.board[1][1],type=PieceType.Dog)
        self.board[1][5].occupiedPiece = Piece(player = Player.One,location=self.board[1][5],type=PieceType.Cat)
        self.board[2][0].occupiedPiece = Piece(player = Player.One,location=self.board[2][0],type=PieceType.Rat)
        self.board[2][2].occupiedPiece = Piece(player = Player.One,location=self.board[2][2],type=PieceType.Leopard)
        self.board[2][4].occupiedPiece = Piece(player = Player.One,location=self.board[2][4],type=PieceType.Wolf)
        self.board[2][6].occupiedPiece = Piece(player = Player.One,location=self.board[2][6],type=PieceType.Elephant)


        self.board[8][6].occupiedPiece = Piece(player = Player.Two,location=self.board[8][6],type=PieceType.Lion)
        self.board[8][0].occupiedPiece = Piece(player = Player.Two,location=self.board[8][0],type=PieceType.Tiger)
        self.board[7][5].occupiedPiece = Piece(player = Player.Two,location=self.board[7][5],type=PieceType.Dog)
        self.board[7][1].occupiedPiece = Piece(player = Player.Two,location=self.board[7][1],type=PieceType.Cat)
        self.board[6][6].occupiedPiece = Piece(player = Player.Two,location=self.board[6][6],type=PieceType.Rat)
        self.board[6][4].occupiedPiece = Piece(player = Player.Two,location=self.board[6][4],type=PieceType.Leopard)
        self.board[6][2].occupiedPiece = Piece(player = Player.Two,location=self.board[6][2],type=PieceType.Wolf)
        self.board[6][0].occupiedPiece = Piece(player = Player.Two,location=self.board[6][0],type=PieceType.Elephant)

    def selectPiece(self,position):
        coordinate = self._getCoordinate(position = position)
        piece = self.board[coordinate[0]][coordinate[1]].occupiedPiece 
        self.selectedPiece = piece



        return f"You have selected {piece.type}" 

    def attemptMove(self,position=input):
         coordinate = self._getCoordinate(position = position)
         square = self.board[coordinate[0]][coordinate[1]]
         result = square.tryToOccupy(piece = self.selectedPiece)

         return result

    def _getCoordinate(self,position):
        #Converts Human friendly coordinate (7A) to machine friendly coordinate (row=6,col=0)
        row = int(position[0])-1
        column = columnDict[position[1]]
        return (row,column)  


    
                






class Piece():
    def __init__(self,type,location,player) -> None:
        self.team : Player = player
        self.type : PieceType = type 
        self.location : Square = location
    
    def __eq__(self, other):     
        if (other == None):
            return False    
        return (self.team == other.team) and (self.type == other.type)

    

class Square():
    def __init__(self,type,row,col) -> None:
        self.type : SquareType = type
        self.occupiedPiece : Piece = None
        self.row = row
        self.col = col


    def _jumpElligible(self,piece):
        #Checks if a piece is elligible to make the jump
        return piece.type == PieceType.Tiger or piece.type == PieceType.Lion


    def _withinOneSquare(self,piece):
        #Implements the rule that makes sure the piece is moving ONE square only verticall/horizonally but not diagonally.
        currentLocation = piece.location
        if currentLocation.row == self.row:
            #If same row...
            if abs(currentLocation.col - self.col) == 1: #Col difference can only be 1 
                return True 
            else: return False #More than one square away
        elif currentLocation.col == self.col:
            #If same col...
            if abs(currentLocation.row - self.row) == 1: #Row difference can only be 1 
                return True 
            else: return False #More than one square away
        else: return False  #Diagonally or too far away.


    def _validJump(self,piece):
        #Will check if elligible piece is making a valid jump!
        pass

    def _attemptAttack(self,piece):
        #Will check if the attack is elligible
        return "YOU MUST RETURN SOMETHING"



    def tryToOccupy(self,piece):
        #If already a piece exists in the square 
        if self.occupiedPiece != None:
            if self.occupiedPiece.team == piece.team: #Checks if collison with own piece
                return "This square is already occupied by your Piece"
            else: 
                #Collison with enemy piece, checking attack elligibility
                return self._attemptAttack()


            
        #If vacant square, checks if further rules are followed
        #If one square rule is followed
        if not self._withinOneSquare(piece):
            if not self._jumpElligible(piece): #If not within one square, it could be a jump elligible piece 
                return "Invalid destination. You are out of your range."
            #Meaning a jump elligible piece that's outside of one range, checking if the jump is valid
            if not self._validJump(piece):
                return "Invalid Jump attempted!"
        #TO DO: 
          #Check if the piece has right to move in (e.g Den, Water , Cross-border for a rat)
          #Implement Active Player who has turn
          #Implement Turn rotation




    
