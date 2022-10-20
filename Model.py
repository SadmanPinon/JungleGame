from turtle import pos
from xmlrpc.client import Boolean
from Constants import * 
 

class Model():
    
    def __init__(self) -> None:
        self.board  = [[0 for col in range(7)] for row in range(9)] 
        self.__initializeBoard()
        self.__assignPieces()
        self.selectedPiece = None
        self.deadPiecesPlayerOne = 0 
        self.deadPiecesPlayerTwo = 0 
        self.playerTurn = Player.One
        self.winner = None 

    ## Auxlery Functions ------------------------------------------------------------------------------------------------------------------------

    def __initializeBoard(self) -> None:
        for row in range(9):
            for col in range (0,7):
                if (row,col) in riverAreas:
                    self.board[row][col] = Square(type = SquareType.Water,row=row,col=col,model=self)
                elif (row,col) in trapAreas:
                    self.board[row][col] = Square(type = SquareType.Trap,row=row,col=col,model=self)
                elif (row,col) in denAreas:
                    self.board[row][col] = Square(type = SquareType.Den,row=row,col=col,model=self)
                else:
                    self.board[row][col] = Square(type = SquareType.Normal,row=row,col=col,model=self)
    def __assignPieces(self) -> None:
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

    def _getCoordinate(self,position: str) -> tuple[int, int]:
        #Converts Human friendly coordinate (7A) to machine friendly coordinate (row=6,col=0)
        row = int(position[0])-1
        column = columnDict[position[1]]
        return (row,column)   

      ##Intent Functions ------------------------------------------------------------------------------------------------------------------------

    def selectPiece(self,position: str) -> str:
        coordinate = self._getCoordinate(position = position)
        piece = self.board[coordinate[0]][coordinate[1]].occupiedPiece 

        if piece.team != self.playerTurn:
            return f"You can't choose Opponent's Piece!"

        self.selectedPiece = piece

        if piece == None : 
            return f"No Piece Exists in position {position} "


        return f"You have selected {piece.type}" 

    def attemptMove(self,position : str =input) -> str:
         coordinate = self._getCoordinate(position = position)
         square = self.board[coordinate[0]][coordinate[1]]
         result = square.tryToOccupy(piece = self.selectedPiece)

         return result

    def unselect(self) -> str:
        self.selectedPiece = None 
        return "Piece unselected"   


    def isIntervened(self,X1: tuple[int, int],Y1: tuple[int, int]) -> Boolean:
        matchingIndex = 0 if X1[0] == Y1[0] else 1
        differingIndex = 1 if X1[0] == Y1[0] else 0 #If row same then col differingIndex and vice Versa 

        startingIndex = X1[differingIndex]  if X1[differingIndex] < Y1[differingIndex] else Y1[differingIndex]
        startingIndex +=1 
        endingIndex = X1[differingIndex]  if X1[differingIndex] >= Y1[differingIndex] else Y1[differingIndex]
        
        for index in range(startingIndex,endingIndex):
            
            if matchingIndex == 0: 
                        
                if self.board[X1[0]][index].occupiedPiece != None:  #Intervening square found
                    return True  
            else:
                if self.board[index][X1[1]].occupiedPiece != None:  #Intervening square found
                    return True  
           
            
        return False 

    def changeTurns(self) -> None:
        #Change to 1 if 2 is playing otherwise 1
        self.playerTurn = Player.One if self.playerTurn == Player.Two else Player.Two 

        #Deselects any selected piece 
        self.selectedPiece = None 

   
    
                






class Piece():
    def __init__(self,type,location,player) -> None:
        self.team : Player = player
        self.type : PieceType = type 
        self.location : Square = location
    
    def __eq__(self, other):     
        if (other == None):
            return False    
        return (self.team == other.team) and (self.type == other.type)

    



    def attack(self,opponent) -> Boolean:
        #Doesn't check if same or diff team, assumes its diff team. 
        if self.type.value >= opponent.type.value: #In general if higher (or eq) rank...
            if not (self.type == PieceType.Elephant and opponent.type == PieceType.Rat): #Elephant cant eat rat
                return True #Eat                 
        elif (self.type == PieceType.Rat and opponent.type == PieceType.Elephant):#Rat can eat Elephant
            return True #Eat 
        return False 


    

class Square():
    def __init__(self,type,row,col,model) -> None:
        self.type : SquareType = type
        self.occupiedPiece : Piece = None
        self.row = row
        self.col = col
        self.model = model

    ## Auxlery Functions ------------------------------------------------------------------------------------------------------------------------

    def _jumpElligible(self,piece: Piece) -> Boolean:
        #Checks if a piece is elligible to make the jump
        return (piece.type == PieceType.Tiger or piece.type == PieceType.Lion) #Is the piece a Tiger or a Lion?


    def _withinOneSquare(self,piece: Piece) -> Boolean:
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

    def _ownDen(self,piece: Piece) -> Boolean:
        #Checks if piece is an ally piece trying to move to it's own den.
        if self.type == SquareType.Den: #Checks if the square is a den square to begin with
            #Checks if den and piece are from same team
            if (piece.team == Player.One) and (self.row == 0):
                return True 
            elif (piece.team == Player.Two) and (self.row == 8):
                return True 
        return False 

    def _waterElligible(self,piece: Piece) -> Boolean:
        #Only concerns scenario when a rat tries to move into a water.
        return piece.type == PieceType.Rat 
        # Water Square check needs to be implemented exertnally before invoking the function
        #This func assumes that the square is water square. 
        
        

    def _validJump(self,piece: Piece) -> Boolean: 
        #Will check if elligible piece is making a valid jump! assume it's an elligible piece already. ( by using _jumpElligible())
        #X1 = Oirign, Y1 = Destination
        X1 = (piece.location.row,piece.location.col)
        Y1 = (self.row,self.col)

        for pair in jumpPoints:
            if X1 in pair and Y1 in pair: #Both Starting and Ending condition match
                if not self.model.isIntervened(X1=X1,Y1=Y1):
                   
                    return True 
                
                return False 
        return False  

    def _attemptAttack(self,piece: Piece) -> str: # UNFINISHED
        #Will check if the attack is elligible
        # Scenarios: 
        #     1. Cross Border Attack Check 
        #     2. If Rank is followed 
        #     3. If Victim in Den Square
        #     4. Jump attack in presence of intervening square.
      

        #3
        if (self.type == SquareType.Trap):
            return self._attack(piece=piece)
        #1
        elif (piece.type == PieceType.Rat and self._crossBorderAttack(piece=piece)):
            return "Cross-Border attack isn't allowed!"
            
        #2
        elif piece.attack(self.occupiedPiece):
            return self._attack(piece=piece)

        return "Inelligible Attack"

    def _attack(self,piece : Piece) -> str:
        #Attacks and occupies
        statement = f"Succesfully attacked {self.occupiedPiece.type}"
            #Logs for model to track state of game
        if self.occupiedPiece.type == Player.One:
            self.model.deadPiecesPlayerOne += 1
        else:
            self.model.deadPiecesPlayerTwo += 1 

        #Removes Reference
        piece.location.occupiedPiece = None 
        self.occupiedPiece = piece 
        piece.location = self
        #Changes Player Turns
        self.model.changeTurns()
        return statement

    def _crossBorderAttack(self,piece: Piece)-> str:
        #Assumes piece is a rat piece 
        return self.type != piece.location.type
        
    def _occupy(self,piece: Piece) -> str:
        #Called when its determined that occupying this square is a legal move. 
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


    ##Intent Functions ------------------------------------------------------------------------------------------------------------------------

    def tryToOccupy(self,piece: Piece) -> str: # UNFINISHED

         #If vacant square, checks if further rules are followed
        #If one square rule is followed
        if not self._withinOneSquare(piece):
            if not self._jumpElligible(piece): #If not within one square, it could be a jump elligible piece 
                return "Invalid destination. You are out of your range."
            #Meaning a jump elligible piece that's outside of one range, checking if the jump is valid
            elif not self._validJump(piece):
                return "Invalid Jump attempted!"         
        elif self._ownDen(piece=piece):
            return "Illegal Move! You tried to move to your own den square"
        elif (self.type==SquareType.Water) and (not self._waterElligible(piece=piece)):
            return "Illegal Move, You can't move into water. Only Rat(1) Can!"

        #If already a piece exists in the square 
        if self.occupiedPiece != None:
            if self.occupiedPiece.team == piece.team: #Checks if collison with own piece
                if self.occupiedPiece == piece:
                    return "You are already here"
                return "This square is already occupied by your Piece"
            else: 
                #Collison with enemy piece, checking attack elligibility
                return self._attemptAttack(piece=piece)


            
       
                        
       


        outcome = self._occupy(piece=piece)  #<-----Need further logic before calling this
        return outcome   

    

    
    def empty(self) -> Boolean: #Mostly ( should work)
        #Called to remove piece from old square when located to new square
        piece = self.occupiedPiece
        if  piece != None and piece.location != self: #If there is an occupied piece which is referencing another square
            self.occupiedPiece = None 
            return True 
        return False 
       

    
