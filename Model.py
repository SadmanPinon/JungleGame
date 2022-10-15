from Constants import * 
 

class Model():
    def __init__(self) -> None:
        self.board  = [[0 for col in range(7)] for row in range(9)] 
        self.__initializeBoard()
        self.__assignPieces()
        
    def __initializeBoard(self):
        for row in range(9):
            for col in range (0,7):
                if (row,col) in riverAreas:
                    self.board[row][col] = Square(type = SquareType.Water)
                elif (row,col) in trapAreas:
                    self.board[row][col] = Square(type = SquareType.Trap)
                elif (row,col) in denAreas:
                    self.board[row][col] = Square(type = SquareType.Den)
                else:
                    self.board[row][col] = Square(type = SquareType.Normal)
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
        


                






class Piece():
    def __init__(self,type,location,player) -> None:
        self.team : Player = player
        self.type : PieceType = type 
        self.location : Square = location

    

class Square():
    def __init__(self,type) -> None:
        self.type : SquareType = type
        self.occupiedPiece : Piece = None 

    
