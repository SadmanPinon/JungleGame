from unittest.mock import patch
import unittest
from Model import *
from Constants import *


# What functionalities are tested
# How they are tested
# Expected Results 


#model.attemptMove() is checked
#model.changeTurns() is checked
#model.selectPiece() is checked
#model.isIntervened is checked
#model.unselect()
#square.empty() is checked
#piece.attack() is checked
class TestModel(unittest.TestCase):

    def test_initializeBoard1(self):
        '''
              test_initializeBoard1 tests the integrity of the initializeBoard function

              1.Functionality Tested : checks if the water squares in the board is correctly initialized in their position

              2. How It's Tested :
                 Initialize a new model
                 Passes Through Each Row and Column of Board
                 Checks if the squares on the RiverAreas are indeed SquareType.Water
                 


              3. Expected Outcome :
                  ALL Squares on the RiverAreas coordinate are supposed to be of type SquareType.Water
        '''
        model = Model()
        for row in range(9):
            for col in range(0, 7):
                if (row, col) in riverAreas:
                    self.assertEqual(model.board[row][col].type, SquareType.Water)

    def test_initializeBoard2(self):
        '''
              test_initializeBoard2 tests the integrity of the initializeBoard function

              1.Functionality Tested : checks if the water squares in the board is correctly initialized in their position

              2. How It's Tested :
                 Initialize a new model
                 Passes Through Each Row and Column of Board
                 Checks if the squares on the TrapAreas are indeed SquareType.Trap



              3. Expected Outcome :
                  ALL Squares on the TrapAreas coordinate are supposed to be of type SquareType.Trap
        '''
        model = Model()
        
        for row in range(9):
            for col in range(0, 7):
                if (row, col) in trapAreas:
                    self.assertEqual(model.board[row][col].type, SquareType.Trap)

    def test_initializeBoard3(self):
        '''
          test_initializeBoard3 tests the integrity of the initializeBoard function

          1.Functionality Tested : checks if the Den squares in the board is correctly initialized in their position

          2. How It's Tested :
             Initialize a new model
             Passes Through Each Row and Column of Board
             Checks if the squares on the DenAreas are indeed SquareType.Den



          3. Expected Outcome :
              ALL Squares on the DenAreas coordinate are supposed to be of type SquareType.Den
        '''
        model = Model()
       
        for row in range(9):
            for col in range(0, 7):
                if (row, col) in denAreas:
                    self.assertEqual(model.board[row][col].type, SquareType.Den)

    def test_initializeBoard4(self):
        '''
          test_initializeBoard4 tests the integrity of the initializeBoard function

          1.Functionality Tested : checks if the Normal squares in the board is correctly initialized in their position

          2. How It's Tested :
             Initialize a new model
             Passes Through Each Row and Column of Board
             Checks if the Squares are not from Den, Trap or River Area
             If not, it is determined to be a position for normal square
             It is checked if it is of type Normal Square



          3. Expected Outcome :
              ALL Squares determined to be from normal area coordinate are supposed to be of type SquareType.Normal
        '''
        model = Model()
       
        for row in range(9):
            for col in range(0, 7):
                if (row, col) not in riverAreas and (row, col) not in trapAreas and (row, col) not in denAreas:
                    self.assertEqual(model.board[row][col].type, SquareType.Normal)

   
    def test_changeTurns1(self):
        '''
              test_changeTurns1 tests the integrity of the changeTurns function

              1.Functionality Tested : Tests if Player One is being Changed to Player Two and selected Piece is None

              2. How It's Tested :
                 Initialize a new model
                 Set the model's playerTurn to Player.One
                 Selects a random Piece as the model class's selectedPiece
                 Invokes the changeTurns() function

              3. Expected Outcome :
                  Player Turn should be Player Two
                  SelectedPiece should be null
        '''
        model = Model()
        model.playerTurn = Player.One
        model.selectedPiece = Piece(player=Player.One, location=model.board[0][0], type=PieceType.Lion)

        model.changeTurns()
        self.assertEqual(model.playerTurn, Player.Two)
        self.assertEqual(model.selectedPiece, None)
    def test_changeTurns2(self):

        '''
          test_changeTurns2 tests the integrity of the changeTurns function

          1.Functionality Tested : Tests if Player Two is being Changed to Player One and selected Piece is None

          2. How It's Tested :
             Initialize a new model
             Set the model's playerTurn to Player.Two
             Selects a random Piece as the model class's selectedPiece
             Invokes the changeTurns() function

          3. Expected Outcome :
              Player Turn should be Player One
              SelectedPiece should be null
        '''
        model = Model()
        model.playerTurn = Player.Two
        model.selectedPiece = Piece(player=Player.Two, location=model.board[0][0], type=PieceType.Lion)

        model.changeTurns()
        self.assertEqual(model.playerTurn, Player.One)
        self.assertEqual(model.selectedPiece, None)
    def test_changeTurns3(self):
        '''
          test_changeTurns3 tests the integrity of the changeTurns function

          1.Functionality Tested : Tests if the function can invoke the current turn when repeatedly being called

          2. How It's Tested :
             Initialize a new model
             @Checks Player Turn to see if it's 1
             invokes the function
             @Checks Player Turn to see if It's 2
             Invokes the function twice to simulate repeated calling 
             @Checks Player Turn to see if It's 2


          3. Expected Outcome :
              Outcome 1 : Player.One
              Outcome 2 : Player.Two
              Outcome 3 : Player.Two
        '''

        model = Model()
        self.assertEqual(model.playerTurn, Player.One)
        model.changeTurns()
        self.assertEqual(model.playerTurn, Player.Two)
        model.changeTurns()
        model.changeTurns()
        self.assertEqual(model.playerTurn, Player.Two)
               

   
    
    def test_getCoordinate(self):
        '''
              test_getCoordinate tests the integrity of the getCoordinate function

              1.Functionality Tested : Test if the function is accurately translating human friendly coordinate to machine
              readable coordinate.

              2. How It's Tested :
                 Initialize a new model
                 Two Instances of ...
                         invoke the get_coordinate function
                         check if the output is same as what's expected

              3. Expected Outcome :
                  act : 0,0 is expected
                  act : 6,0 is expected
        '''
        model = Model()

        act = model._getCoordinate('1A')
        self.assertEqual(act, (0, 0))

        act2 = model._getCoordinate('7G')
        self.assertEqual(act2, (6, 6))


    def test_attempt1(self):
        '''
              test_attempt1 tests the integrity of the attempt function

              1.Functionality Tested : Tests if the function fails to attempt when illegal move performed

              2. How It's Tested :
                 Initialize a new model
                 Selects a Piece to move
                 Performs various combinations of moves by invoking attemptMove(), all of which are illegal moves.

              3. Expected Outcome :
                  "Invalid Jump Attempted" for ALL cases
        '''
        model = Model()
        model.selectPiece('1A')
        self.assertEqual(model.attemptMove('3A'), 'Invalid Jump attempted!')
        self.assertEqual(model.attemptMove('9G'), 'Invalid Jump attempted!')
        self.assertEqual(model.attemptMove('6B'), 'Invalid Jump attempted!')
        self.assertEqual(model.attemptMove('1A'), 'Invalid Jump attempted!')

        self.assertEqual(model.playerTurn, Player.One)

    def test_attempt2(self):
        '''
          test_attempt2 tests the integrity of the attempt function

          1.Functionality Tested : Tests if the function succesfully moves when a legal move is performed.

          2. How It's Tested :
             Initialize a new model
             Selects a Piece to move
             Performs a legal move by invoking attemptMove()

          3. Expected Outcome :
                AssertEqual suceeds with matching the output "Succesfully moved piece to square (2, \'A\')"
        '''
        model = Model()
        model.selectPiece('1A')
        self.assertEqual(model.attemptMove('2A'), 'Succesfully moved piece to square (2, \'A\')')
        self.assertEqual(model.playerTurn, Player.Two)

    def test_attempt3(self):

        '''
    test_attack_rat_elephant_from_water checks if a rat can
    attack an elephant from the water

    it first moves both pieces into position before the tests are performed
    '''
        model = Model()

        model.selectPiece('3A')
        model.attemptMove('4A')

        model.selectPiece('7A')
        model.attemptMove('6A')

        model.selectPiece('4A')
        model.attemptMove('4B')

        model.selectPiece('9A')
        model.attemptMove('9B')

        model.selectPiece('4B')
        model.attemptMove('5B')

        model.selectPiece('9B')
        model.attemptMove('9A')

        model.selectPiece('5B')
        model.attemptMove('6B')

        model.selectPiece('9A')
        model.attemptMove('9B')

        model.selectPiece('6B')
        # test if the attack happened and if it accurately notifies the user
        self.assertEqual(model.attemptMove(
            '6A'), "Cross-Border attack isn't allowed!")
        # test if the elephant still exists on 6A
        self.assertEqual(
            model.board[5][0].occupiedPiece.type, PieceType.Elephant)
        # test if the rat is still on 6B in the water
        self.assertEqual(model.board[5][1].occupiedPiece.type, PieceType.Rat)

    def test_select_piece1(self):
        '''
              test_select_piece1 tests the selectPiece function

              1.Functionality Tested : test if you can cannot select other player's pieces

              2. How It's Tested :
                 Initialize a new model
                 Try to select all of the opponents pieces player 1
                 switch pplayer
                 Try to select all of the opponents pieces as player 2

              3. Expected Outcome :
                You can't choose Opponent's Piece!
        '''
        wrong_select = "You can't choose Opponent's Piece!"
        model = Model()
        # player 1's turn trying to select opponent's piece
        self.assertEqual(model.selectPiece(
            '7A'), wrong_select)  # add assertion here
        self.assertEqual(model.selectPiece('9A'), wrong_select)
        self.assertEqual(model.selectPiece('8B'), wrong_select)
        self.assertEqual(model.selectPiece('7C'), wrong_select)
        self.assertEqual(model.selectPiece('7E'), wrong_select)
        self.assertEqual(model.selectPiece('8F'), wrong_select)
        self.assertEqual(model.selectPiece('7G'), wrong_select)
        self.assertEqual(model.selectPiece('9G'), wrong_select)

        model.changeTurns()

        self.assertEqual(model.selectPiece(
            '3A'), wrong_select)  # add assertion here
        self.assertEqual(model.selectPiece('1A'), wrong_select)
        self.assertEqual(model.selectPiece('2B'), wrong_select)
        self.assertEqual(model.selectPiece('3C'), wrong_select)
        self.assertEqual(model.selectPiece('3E'), wrong_select)
        self.assertEqual(model.selectPiece('2F'), wrong_select)
        self.assertEqual(model.selectPiece('1G'), wrong_select)
        self.assertEqual(model.selectPiece('3G'), wrong_select)

    def test_select_piece2(self):
        '''
               test_select_piece1 tests the selectPiece function

               1.Functionality Tested : test if you can cannot select squares with no pieces

               2. How It's Tested :
                  Initialize a new model
                  Try to select all of the squares with no pieces player 1
                  switch pplayer
                  Try to select all of the squares with no pieces as player 2

               3. Expected Outcome :
                 No Piece Exists in position
         '''
        model = Model()
        n = "No Piece Exists in position"

        # try to select nothing
        self.assertIn(n, model.selectPiece('1B'))
        self.assertIn(n, model.selectPiece('1C'))
        self.assertIn(n, model.selectPiece('1D'))
        self.assertIn(n, model.selectPiece('1E'))
        self.assertIn(n, model.selectPiece('1F'))
        self.assertIn(n, model.selectPiece('2A'))
        self.assertIn(n, model.selectPiece('2C'))
        self.assertIn(n, model.selectPiece('2D'))
        self.assertIn(n, model.selectPiece('2E'))
        self.assertIn(n, model.selectPiece('2G'))
        self.assertIn(n, model.selectPiece('3B'))
        self.assertIn(n, model.selectPiece('3D'))
        self.assertIn(n, model.selectPiece('3F'))
        self.assertIn(n, model.selectPiece('4A'))
        self.assertIn(n, model.selectPiece('4B'))
        self.assertIn(n, model.selectPiece('4C'))
        self.assertIn(n, model.selectPiece('4D'))
        self.assertIn(n, model.selectPiece('4E'))
        self.assertIn(n, model.selectPiece('4F'))
        self.assertIn(n, model.selectPiece('4G'))
        self.assertIn(n, model.selectPiece('5A'))
        self.assertIn(n, model.selectPiece('5B'))
        self.assertIn(n, model.selectPiece('5C'))
        self.assertIn(n, model.selectPiece('5D'))
        self.assertIn(n, model.selectPiece('5E'))
        self.assertIn(n, model.selectPiece('5F'))
        self.assertIn(n, model.selectPiece('5G'))
        self.assertIn(n, model.selectPiece('6A'))
        self.assertIn(n, model.selectPiece('6B'))
        self.assertIn(n, model.selectPiece('6C'))
        self.assertIn(n, model.selectPiece('6D'))
        self.assertIn(n, model.selectPiece('6E'))
        self.assertIn(n, model.selectPiece('6F'))
        self.assertIn(n, model.selectPiece('6G'))
        self.assertIn(n, model.selectPiece('7B'))
        self.assertIn(n, model.selectPiece('7D'))
        self.assertIn(n, model.selectPiece('7F'))
        self.assertIn(n, model.selectPiece('8A'))
        self.assertIn(n, model.selectPiece('8C'))
        self.assertIn(n, model.selectPiece('8D'))
        self.assertIn(n, model.selectPiece('8E'))
        self.assertIn(n, model.selectPiece('8G'))
        self.assertIn(n, model.selectPiece('9B'))
        self.assertIn(n, model.selectPiece('9C'))
        self.assertIn(n, model.selectPiece('9D'))
        self.assertIn(n, model.selectPiece('9E'))
        self.assertIn(n, model.selectPiece('9F'))

        model.changeTurns()
        self.assertIn(n, model.selectPiece('1B'))
        self.assertIn(n, model.selectPiece('1C'))
        self.assertIn(n, model.selectPiece('1D'))
        self.assertIn(n, model.selectPiece('1E'))
        self.assertIn(n, model.selectPiece('1F'))
        self.assertIn(n, model.selectPiece('2A'))
        self.assertIn(n, model.selectPiece('2C'))
        self.assertIn(n, model.selectPiece('2D'))
        self.assertIn(n, model.selectPiece('2E'))
        self.assertIn(n, model.selectPiece('2G'))
        self.assertIn(n, model.selectPiece('3B'))
        self.assertIn(n, model.selectPiece('3D'))
        self.assertIn(n, model.selectPiece('3F'))
        self.assertIn(n, model.selectPiece('4A'))
        self.assertIn(n, model.selectPiece('4B'))
        self.assertIn(n, model.selectPiece('4C'))
        self.assertIn(n, model.selectPiece('4D'))
        self.assertIn(n, model.selectPiece('4E'))
        self.assertIn(n, model.selectPiece('4F'))
        self.assertIn(n, model.selectPiece('4G'))
        self.assertIn(n, model.selectPiece('5A'))
        self.assertIn(n, model.selectPiece('5B'))
        self.assertIn(n, model.selectPiece('5C'))
        self.assertIn(n, model.selectPiece('5D'))
        self.assertIn(n, model.selectPiece('5E'))
        self.assertIn(n, model.selectPiece('5F'))
        self.assertIn(n, model.selectPiece('5G'))
        self.assertIn(n, model.selectPiece('6A'))
        self.assertIn(n, model.selectPiece('6B'))
        self.assertIn(n, model.selectPiece('6C'))
        self.assertIn(n, model.selectPiece('6D'))
        self.assertIn(n, model.selectPiece('6E'))
        self.assertIn(n, model.selectPiece('6F'))
        self.assertIn(n, model.selectPiece('6G'))
        self.assertIn(n, model.selectPiece('7B'))
        self.assertIn(n, model.selectPiece('7D'))
        self.assertIn(n, model.selectPiece('7F'))
        self.assertIn(n, model.selectPiece('8A'))
        self.assertIn(n, model.selectPiece('8C'))
        self.assertIn(n, model.selectPiece('8D'))
        self.assertIn(n, model.selectPiece('8E'))
        self.assertIn(n, model.selectPiece('8G'))
        self.assertIn(n, model.selectPiece('9B'))
        self.assertIn(n, model.selectPiece('9C'))
        self.assertIn(n, model.selectPiece('9D'))
        self.assertIn(n, model.selectPiece('9E'))
        self.assertIn(n, model.selectPiece('9F'))

    def test_select_piece3(self):
        '''
               test_select_piece1 tests the selectPiece function

               1.Functionality Tested : test if you can cannot select squares with no pieces

               2. How It's Tested :
                  Initialize a new model
                  Try to select all of the pieces of pieces player 1
                  switch pplayer
                  Try to select all of the pieces of pieces as player 2

               3. Expected Outcome :
                "You have selected "
         '''
        model = Model()
        s = "You have selected "
        # try to select own pieces
        self.assertIn(s, model.selectPiece('3A'))
        self.assertIn(s, model.selectPiece('1A'))
        self.assertIn(s, model.selectPiece('2B'))
        self.assertIn(s, model.selectPiece('3C'))
        self.assertIn(s, model.selectPiece('3E'))
        self.assertIn(s, model.selectPiece('2F'))
        self.assertIn(s, model.selectPiece('1G'))
        self.assertIn(s, model.selectPiece('3G'))
        model.changeTurns()
        # switch turn
        # testing own player's pieces
        self.assertIn(s, model.selectPiece('7A'))
        self.assertIn(s, model.selectPiece('9A'))
        self.assertIn(s, model.selectPiece('8B'))
        self.assertIn(s, model.selectPiece('7C'))
        self.assertIn(s, model.selectPiece('7E'))
        self.assertIn(s, model.selectPiece('8F'))
        self.assertIn(s, model.selectPiece('7G'))
        self.assertIn(s, model.selectPiece('9G'))
    def test_validJump(self):
        '''
    FUNCTIONALITY: test_if_other_can_jump checks if the others can jump
    across river tiles other pieces should not be able to jump across the river

    HOW IT IS DONE: initially the pieces are moved into position prior to the
    test being performed
    then check if the square where the piece jumped from is empty and the square
    that the piece should be are none and piece respectively

    EXPCETED RESULT:
    NONE, PIECETYPE.DOG
    '''
        model = Model()
        model.selectPiece('2B')
        model.attemptMove('3B')

        model.selectPiece('9A')
        model.attemptMove('9B')

        model.selectPiece('3B')
        model.attemptMove('7B')
        # there should not be a piece on square 7B
        self.assertEqual(model.board[6][1].occupiedPiece, None)
        # check if the dog is still on 3B
        self.assertEqual(model.board[2][1].occupiedPiece.type, PieceType.Dog)
    def test_attack(self):
        '''
    FUNCTIONALITY: test_player_two_kill checks if it is possible for player 2's pieces
    to kill player 1's pieces

    HOW IT IS DONE: this is done between player 2's rat and player 1's elephant
    
    EXPECTED RESULT: DEADPIECES PLAYER 1 = 1
    '''
        model = Model()

        model.changeTurns()
        model.selectPiece('7G')
        model.attemptMove('6G')

        model.changeTurns()
        model.selectPiece('6G')
        model.attemptMove('5G')

        model.changeTurns()
        model.selectPiece('5G')
        model.attemptMove('4G')

        model.changeTurns()
        model.selectPiece('4G')
        model.attemptMove('3G')

        self.assertEqual(model.deadPiecesPlayerOne, 1)
    def test_isIntervened(self):
        '''
    FUNCTIONALITY:similar to the test_interving
    
    HOW IT IS DONE: test_is_intervened checks the direct function
    to see if between two positions there is a piece
    to test if this is true various pieces are moved
    and various different positions are checked
    
    EXPECTED RESULT:
    TRUE, FALSE,TRUE, FALSE
    '''
        model = Model()
        self.assertEqual(model.isIntervened((0, 1), (2, 1)), True)

        model.selectPiece('1A')
        model.attemptMove('2A')

        self.assertEqual(model.isIntervened((0, 0), (0, 4)), False)

        model.selectPiece('7G')
        model.attemptMove('6G')

        model.selectPiece('2A')
        model.attemptMove('1A')

        model.selectPiece('6G')
        model.attemptMove('6F')

        self.assertEqual(model.isIntervened((5, 3), (5, 6)), True)

        self.assertEqual(model.isIntervened((0, 1), (0, 4)), False)
    def test_ownDen1(self):
        '''
       FUNCTIONALITY: test_attack_own_den checks if player 1 can attack their own den
       like all functions initialize a new model functions to start
       with a fresh board

       HOW IT IS DONE: Since the function checks for player 1 it always skips player 2's turn
       To speed up the coding the program moves the piece on square 91
       which is the tiger piece
       and move it from 1A to 1B
       and then from 1B to 1C
       then 1C to 1D

       note:
       first we have to select the piece using the selectPiece function
       and then move the piece using the attemptMove function

       EXPECTED RESULT:
       "Illegal Move! You tried to move to your own den square"
       '''
        model = Model()
        model.selectPiece('1A')
        model.attemptMove('1B')

        model.changeTurns()
        model.selectPiece('1B')
        model.attemptMove('1C')

        model.changeTurns()

        model.selectPiece('1C')
        self.assertEqual(model.attemptMove('1D'), "Illegal Move! You tried to move to your own den square")

    def test_ownDen2(self):
        '''
    FUNCTIONALITY: test_ownDen2 checks if player 2 can attack their own den
    like all functions initialize a new model functions to start
    with a fresh board

    HOW IT IS DONE: Since the function checks for player 2 it always skips player 1's turn
    To speed up the coding the program moves the piece on square 9A
    which is the tiger piece
    and move it from 9A to 9B
    and then from 9B to 9C
    then 9C to 9D

    note:
    first we have to select the piece using the selectPiece function
    and then move the piece using the attemptMove function

    EXPECTED RESULT:
    "Illegal Move! You tried to move to your own den square"
    '''
        model = Model()
        model.changeTurns()
        model.selectPiece('9A')
        model.attemptMove('9B')

        model.changeTurns()
        model.selectPiece('9B')
        model.attemptMove('9C')

        model.changeTurns()

        model.selectPiece('9C')
        self.assertEqual(model.attemptMove('9D'), "Illegal Move! You tried to move to your own den square")
    def test_elligibleJump1(self):
        '''
    FUNCTIONALITY:test_if_lion_can_jump checks if the lion can jump
    across river tiles

    a lion should be possible to do this

    HOW IT IS DONE:   initially the lion is moved into position prior to the
    test being performed

    EXPECTED RESULT:
    SQUARE(6,1) is occupied by LION
    '''
        model = Model()

        model.selectPiece('3A')
        model.attemptMove('4A')

        model.selectPiece('9A')
        model.attemptMove('9B')

        model.selectPiece('1A')
        model.attemptMove('2A')

        model.selectPiece('9B')
        model.attemptMove('9A')

        model.selectPiece('2A')
        model.attemptMove('3A')

        model.selectPiece('9A')
        model.attemptMove('9B')

        model.selectPiece('3A')
        model.attemptMove('3B')

        model.selectPiece('9B')
        model.attemptMove('9A')

        model.selectPiece('3B')
        model.attemptMove('7B')

        self.assertEqual(model.board[6][1].occupiedPiece.type, PieceType.Lion)
    def test_elligibleJump2(self):
        '''
    FUNCTIONALITY: test_if_tiger_can_jump checks if the tiger can jump
    across river tiles

    HOW IT IS DONE: initially the lion is moved into position prior to the
    test being performed

    EXPECTED RESULT:
    SQUARE(6,1) is occupied by TIGER
    '''
        model = Model()

        model.selectPiece('3G')
        model.attemptMove('4G')

        model.selectPiece('9A')
        model.attemptMove('9B')

        model.selectPiece('1G')
        model.attemptMove('2G')

        model.selectPiece('9B')
        model.attemptMove('9A')

        model.selectPiece('2G')
        model.attemptMove('3G')

        model.selectPiece('9A')
        model.attemptMove('9B')

        model.selectPiece('3G')
        model.attemptMove('3F')

        model.selectPiece('9B')
        model.attemptMove('9A')

        model.selectPiece('3F')
        model.attemptMove('7F')

        self.assertEqual(model.board[6][5].occupiedPiece.type, PieceType.Tiger)
    def test_unselect(self):
        '''
        FUNCTIONALITY: test_unselect checks if the program is able to unselec the currently selected piecce
        so that other pieces can be chosen

        HOW IT IS DONE: checks various cases of unselecting and sees if nothing breaks

        EXPECTED RESULT: 'Piece unselected'
        '''
        # check if unselect works in normal case
        model = Model()
        model.selectPiece('1A')
        self.assertEqual(model.selectedPiece.type, PieceType.Lion)
        model.unselect()
        self.assertEqual(model.selectedPiece, None)

        # check if unselect works if nothing is selected
        self.assertEqual(model.unselect(), 'Piece unselected')
        self.assertEqual(model.unselect(), 'Piece unselected')
        self.assertEqual(model.unselect(), 'Piece unselected')

        # check if unselect works after multiple state changes
        model.selectPiece('1A')
        model.selectPiece('3A')
        model.selectPiece('2B')
        model.unselect()
        self.assertEqual(model.selectedPiece, None)
    def test_waterElligible(self):
        '''
        FUNCTIONALITY: test_if_other_pieces_can_move_into_water tests if pieces
        other than the rat can enter the water

        HOW IT IS DONE:this is done by taking the leopard piece located at 3C and moving it
        to 4C

        RESULT:
        "Illegal Move, You can't move into water. Only Rat(1) Can!"
        '''
        model = Model()
        model.selectPiece('3C')
        self.assertEqual(model.attemptMove('4C'), "Illegal Move, You can't move into water. Only Rat(1) Can!")
    def test_intervening(self):
        '''
    FUNCTIONALITY :test_interving initializes model and checks if a jumping piece such as a lion or tiger
    is able to jump when a rat is in the water

    HOW IT IS DONE: It starts by moving the mouse piece
    from 3A to 4A
    skipping the 2nd player's turn
    and then 4A to 4B
    which is a river square
    then the test moves the lion piece
    but first it skips the 2nd players turn
    then lion moves 1A to 2A
    skip 2nd player turn
    lion piece 2A -> 3A
    skip 2nd player
    lion 3A -> 4A
    skip 2nd player
    lion 4A -> 4D
    this however will not work since there's a rat piece in one of the squares

    EXPECTED RESULT:
    'Invalid Jump attempted!'
    '''
        model = Model()
        model.selectPiece('3A')
        model.attemptMove('4A')

        model.changeTurns()

        model.selectPiece('4A')
        model.attemptMove('4B')

        model.changeTurns()

        model.selectPiece('1A')
        model.attemptMove('2A')

        model.changeTurns()

        model.selectPiece('2A')
        model.attemptMove('3A')

        model.changeTurns()

        model.selectPiece('3A')
        model.attemptMove('4A')

        model.changeTurns()

        model.selectPiece('4A')
        self.assertEqual(model.attemptMove('4D'), 'Invalid Jump attempted!')
    def test_tryToOcupy(self):
            '''

        FUNCTIONALITY: test_move_piece_same_square checks the output of the game when a user tries to
        move a selected piece onto itself and onto a square thats already occupied

        HOW IT IS DONE:
        first it attempts to move lion piece on 1A to 1A
        resulting in the user being notified
        then the program move the piece to 2A
        skip player 2's turn
        then try to move 2A to 3A

        RESULT: "This square is already occupied by your Piece"
        '''
            model = Model()
            model.selectPiece('1A')
            self.assertEqual(model.attemptMove('1A'), "Invalid Jump attempted!")
            self.assertIn("Succesfully moved piece to square", model.attemptMove('2A'))

            model.changeTurns()

            model.selectPiece('2A')
            self.assertIn("This square is already occupied by your Piece", model.attemptMove('3A'))

class TestPiece(unittest.TestCase):
    
    def test_piece_attack1(self):
        '''
             test_piece_attack1 tests the integrity of the Piece.attack() function

             1.Functionality Tested : It Checks if a higher value piece can kill a lower valued piece

             2. How It's Tested :
                 We initialize a new board and initialize a new wolf piece belonging to player 1
                 and another rat piece belonging to p2 and make the wolf piece attack the rat piece

             3. Expected Outcome :
                 The Function is expected to return TRUE
         '''
        model = Model()
        p1 = Piece(PieceType.Wolf, Square(1, 0, 0, model), Player.One)
        self.assertEqual(p1.attack(Piece(PieceType.Rat, Square(1, 0, 0, model), Player.Two)), True)

    def test_piece_attack2(self):
        '''
             test_piece_attack2 tests the integrity of the Piece.attack() function

             1.Functionality Tested : It Checks if a rat  piece can kill an elephant piece

             2. How It's Tested :
                 We initialize a new board and initialize a new rat piece belonging to player 1
                 and another elephant piece belonging to p2 and make the rat piece attack the elephant piece

             3. Expected Outcome :
                 The Function is expected to return TRUE
         '''

        model = Model()
        p1 = Piece(PieceType.Rat, Square(1, 0, 0, model), Player.One)
        self.assertEqual(p1.attack(Piece(PieceType.Elephant, Square(1, 0, 0, model), Player.Two)), True)

    def test_piece_attack3(self):
        '''
              test_piece_attack3 tests the integrity of the Piece.attack() function

             1.Functionality Tested : It Checks if a rat  piece can kill an elephant piece

             2. How It's Tested :
                 We initialize a new board and initialize a new rat piece belonging to player 1
                 and another wolf piece belonging to p2 and make the rat piece attack the wolf piece

             3. Expected Outcome :
                 The Function is expected to return TRUE
         '''
        model = Model()
        p1 = Piece(PieceType.Rat, Square(1, 0, 0, model), Player.One)
        self.assertEqual(p1.attack(Piece(PieceType.Wolf, Square(1, 0, 0, model), Player.Two)), False)

   
    def test_eq_1(self):
        '''
              test_eq_1 tests the integrity of the Piece.__eq__() function

             1.Functionality Tested : It Checks if two pieces are identical

             2. How It's Tested :
                 We initialize a new wolf piece on square 1A and call the __eq__
                 function with the exact same specifications as the earlier wolf piece


             3. Expected Outcome :
                 The Function is expected to return TRUE
         '''
        model = Model()
        p1 = Piece(PieceType.Wolf,Square(SquareType.Normal,0,0,model),Player.One)
        p = p1.__eq__(Piece(PieceType.Wolf,Square(SquareType.Normal,0,0,model),Player.One))
        self.assertEqual(p,True)

    def test_eq_2(self):
        '''
              test_eq_2 tests the integrity of the Piece.__eq__() function

             1.Functionality Tested : It Checks if two pieces are different

             2. How It's Tested :
                 We initialize a new wolf piece on square 1A and call the __eq__
                 function against no piece
             3. Expected Outcome :
                 The Function is expected to return FALSE
         '''
        model = Model()
        p1 = Piece(PieceType.Wolf, Square(SquareType.Normal, 0, 0, model), Player.One)
        p = p1.__eq__(None)
        self.assertEqual(p, False)

    def test_eq_3(self):
        '''
              test_eq_3 tests the integrity of the Piece.__eq__() function

             1.Functionality Tested : It Checks if two pieces are different

             2. How It's Tested :
                 We initialize a new wolf piece on square 1A and call the __eq__
                 function against the same team's rat piece
             3. Expected Outcome :
                 The Function is expected to return FALSE
         '''
        model = Model()
        p1 = Piece(PieceType.Rat,Square(SquareType.Normal,0,0,model),Player.One)
        p = p1.__eq__(Piece(PieceType.Wolf,Square(SquareType.Normal,0,0,model),Player.One))
        self.assertEqual(p,False)

    def test_eq_4(self):
        '''
              test_eq_4 tests the integrity of the Piece.__eq__() function

             1.Functionality Tested : It Checks if two pieces are different

             2. How It's Tested :
                 We initialize a new wolf piece on square 1A and call the __eq__
                 function against a different team's wolf piece
             3. Expected Outcome :
                 The Function is expected to return FALSE
         '''
        model = Model()
        p1 = Piece(PieceType.Rat,Square(SquareType.Normal,0,0,model),Player.One)
        p = p1.__eq__(Piece(PieceType.Wolf,Square(SquareType.Normal,0,0,model),Player.Two))
        self.assertEqual(p,False)


    # Other TESTS --------------
    def test_piece_attack_elephant_attack_rat(self):
        '''
       test_piece_attack_elephant_attack_rat
       checks if a elephant is able to attack an rat which should not be
       possible

        it should notify the player that such attack is not possible
        the board should also not be updated
       '''
        model = Model()

        # p1
        model.selectPiece('3A')
        model.attemptMove('4A')

        # p2
        model.selectPiece('7A')
        model.attemptMove('6A')

        # p1
        model.selectPiece('4A')
        model.attemptMove('5A')

        # p2
        model.selectPiece('9A')
        model.attemptMove('8A')

        model.selectPiece('1A')
        model.attemptMove('2A')

        model.selectPiece('6A')
        self.assertEqual(model.attemptMove('5A'), "Inelligible Attack")
        self.assertEqual(model.board[0][6].occupiedPiece.attack(model.board[0][2]), True)
        self.assertEqual(model.board[4][0].occupiedPiece.type, PieceType.Rat)

class TestSquare(unittest.TestCase):


 
    def test_jumpElligible1(self):
        '''
              test_jumpElligible1 tests the integrity of the jumpElligible function

              1.Functionality Tested : checks if the piece is elligible to jump

              2. How It's Tested :
                 Initialize a new model
                 Initialize a new square
                 Initialize a new lion piece
                 check using jumpElligible func() if piece should be able to jump

              3. Expected Outcome :
                  The Function is expected to return TRUE
        '''
        model = Model()
        sq = Square(SquareType.Normal,1,1,model)
        acc = sq._jumpElligible(Piece(PieceType.Lion,sq,Player.One))
        self.assertEqual(acc,True)
    def test_jumpElligible2(self):
        '''
              test_jumpElligible1 tests the integrity of the jumpElligible function

              1.Functionality Tested : checks if the piece is elligible to jump

              2. How It's Tested :
                 Initialize a new model
                 Initialize a new square
                 Initialize a new tiger piece
                 check using jumpElligible func() if piece should be able to jump

              3. Expected Outcome :
                  The Function is expected to return TRUE
        '''
        model = Model()
        sq = Square(SquareType.Normal,1,1,model)
        acc = sq._jumpElligible(Piece(PieceType.Tiger,sq,Player.One))
        self.assertEqual(acc,True)
    def test_jumpElligible3(self):
        '''
              test_jumpElligible1 tests the integrity of the jumpElligible function

              1.Functionality Tested : checks if the piece is elligible to jump

              2. How It's Tested :
                 Initialize a new model
                 Initialize a new square
                 Initialize a new rat piece
                 check using jumpElligible func() if piece should be able to jump

              3. Expected Outcome :
                  The Function is expected to return FALSE
        '''
        model = Model()
        sq = Square(SquareType.Normal,1,1,model)
        acc = sq._jumpElligible(Piece(PieceType.Rat,sq,Player.One))
        self.assertEqual(acc,False)

 

    def test_waterElligible1(self):
        '''
              test_waterElligible tests the integrity of the waterElligible function

              1.Functionality Tested : checks if the piece is elligible to enter water

              2. How It's Tested :
                 Initialize a new model
                 Initialize a new square
                 Initialize a new rat piece
                 check using waterElligible func() if piece should be able to enter the water

              3. Expected Outcome :
                  The Function is expected to return TRUE
        '''
        model = Model()
        sq = Square(SquareType.Normal,1,1,model)
        acc = sq._waterElligible(Piece(PieceType.Rat,sq,Player.One))
        self.assertEqual(acc,True)

    def test_waterElligible2(self):
        '''
              test_waterElligible tests the integrity of the waterElligible function

              1.Functionality Tested : checks if the piece is elligible to enter water

              2. How It's Tested :
                 Initialize a new model
                 Initialize a new square
                 Initialize a new elephant piece
                 check using waterElligible func() if piece should be able to enter the water

              3. Expected Outcome :
                  The Function is expected to return FALSE
        '''
        model = Model()
        sq = Square(SquareType.Normal,1,1,model)
        acc = sq._waterElligible(Piece(PieceType.Elephant,sq,Player.One))
        self.assertEqual(acc,False)

 
    def test_tryToOccupy1(self):
        '''
              test_tryToOccupy1 tests the integrity of the tryToOccupy function

              1.Functionality Tested : Tests if a piece is able to move to an invalid positions

              2. How It's Tested :
                Initialize a new model
                Initialize a new square on (0,0)
                Initialize a new Piece on another square far away on (3.3)
                test if the piece on square (3,3) can move to (0,0)
              3. Expected Outcome :
     "Invalid destination. You are out of your range."
        '''
        model = Model()
        sq1 = Square(SquareType.Normal,0,0,model)
        p1 = Piece(PieceType.Rat,Square(SquareType.Normal,3,3,model),Player.One)
        self.assertEqual(sq1.tryToOccupy(p1),"Invalid destination. You are out of your range.")

    def test_tryToOccupy2(self):
        '''
              test_tryToOccupy2 tests the integrity of the tryToOccupy function

              1.Functionality Tested : Tests if a piece is able to move, but can jump, to an invalid positions

              2. How It's Tested :
                Initialize a new model
                Initialize a new square on (0,0)
                Initialize a new Piece (Lion) on another square far away on (3.3)
                test if the piece on square (3,3) can move to (0,0)
              3. Expected Outcome :
               "Invalid Jump attempted!"
        '''
        model = Model()
        sq1 = Square(SquareType.Normal, 0, 0, model)
        p1 = Piece(PieceType.Lion, Square(SquareType.Normal, 3, 3, model), Player.One)
        self.assertEqual(sq1.tryToOccupy(p1), "Invalid Jump attempted!")


    def test_tryToOccupy3(self):
        '''
              test_tryToOccupy3 tests the integrity of the tryToOccupy function

              1.Functionality Tested : Tests if a piece is able to move, but can jump, to their own den square

              2. How It's Tested :
                Initialize a new model
                Initialize a new square on (0,0)
                Initialize a new Piece (Lion) on another square far away on (3.3)
                test if the piece on square (3,3) can move to (0,0)
              3. Expected Outcome :
               "Illegal Move! You tried to move to your own den square"
        '''
        model = Model()
        sq1 = Square(SquareType.Den, 0, 0, model)
        p1 = Piece(PieceType.Lion, Square(SquareType.Normal, 0, 1, model), Player.One)
        self.assertEqual(sq1.tryToOccupy(p1), "Illegal Move! You tried to move to your own den square")

    def test_tryToOccupy4(self):
        '''
               test_tryToOccupy4 tests the integrity of the tryToOccupy function

               1.Functionality Tested : Tests if a piece is able to move, but can jump, on a water square

               2. How It's Tested :
                 Initialize a new model
                 Initialize a new square on (0,0) with type water
                 Initialize a new Piece (Lion) on another square far away on (3.3)
                 test if the piece on square (3,3) can move to (0,0)
               3. Expected Outcome :
                 "Illegal Move, You can't move into water. Only Rat(1) Can!"
         '''
        model = Model()
        sq1 = Square(SquareType.Water, 0, 0, model)
        p1 = Piece(PieceType.Lion, Square(SquareType.Normal, 0, 1, model), Player.One)
        self.assertEqual(sq1.tryToOccupy(p1), "Illegal Move, You can't move into water. Only Rat(1) Can!")

    def test_tryToOccupy5(self):
        '''
               test_tryToOccupy5 tests the integrity of the tryToOccupy function

               1.Functionality Tested : Tests if a piece is able to move when there's an allied
               piece

               2. How It's Tested :
                 Initialize a new model
                 Initialize a new square on (0,0) with wolf piece
                 Initialize a new Piece (Lion) on another square far away on (0,1)
                 test if the piece on square (0,1) can move to (0,0)
               3. Expected Outcome :
                 "This square is already occupied by your Piece"
         '''
        model = Model()
        model.board[0][0].occupiedPiece = Piece(PieceType.Wolf, model.board[0][0], Player.One)
        model.board[0][1].occupiedPiece =Piece(PieceType.Lion,model.board[0][1], Player.One)
        self.assertEqual(model.board[0][0].tryToOccupy(model.board[0][1].occupiedPiece), "This square is already occupied by your Piece")


    def test_tryToOccupy6(self):
        '''
               test_tryToOccupy6 tests the integrity of the tryToOccupy function

               1.Functionality Tested : Tests if a piece is able to move to its own square

               2. How It's Tested :
                 Initialize a new model
                 Initialize a new square on (0,0) with a lion piece
                 Initialize a new Piece (Lion) on another on (0,1)
                 test if the piece on square (0,1) can move to (0,0)
               3. Expected Outcome :
                 "You are already here"
         '''
        model = Model()
        model.board[0][0].occupiedPiece = Piece(PieceType.Lion, model.board[0][0], Player.One)
        model.board[0][1].occupiedPiece =Piece(PieceType.Lion,model.board[0][1], Player.One)
        self.assertEqual(model.board[0][0].tryToOccupy(model.board[0][1].occupiedPiece), "You are already here")

    def test_tryToOccupy7(self):
        '''
               test_tryToOccupy7 tests the integrity of the tryToOccupy function

               1.Functionality Tested : Tests if a piece is able to attack

               2. How It's Tested :
                 Initialize a new model
                 Initialize a new square on (0,0) with a Player 2 rat
                 Initialize a new Piece (Lion) on another square far away on (0,1)
                 test if the piece on square (0,1) can move to (0,0)
               3. Expected Outcome :
                 "Succesfully attacked PieceType.Rat"
         '''
        model = Model()
        model.board[0][0].occupiedPiece = Piece(PieceType.Rat, model.board[0][0], Player.One)
        model.board[0][1].occupiedPiece =Piece(PieceType.Lion,model.board[0][1], Player.Two)
        self.assertEqual(model.board[0][0].tryToOccupy(model.board[0][1].occupiedPiece), "Succesfully attacked PieceType.Rat")


    def test_tryToOccupy8(self):
        '''
               test_tryToOccupy8 tests the integrity of the tryToOccupy function

               1.Functionality Tested : Tests if a piece is able to move

               2. How It's Tested :
                 Initialize a new model
                 Initialize a new square on (0,0) with type normal
                 Initialize a new Piece (Lion) on another square far away on (0,1)
                 test if the piece on square (0,1) can move to (0,0)
               3. Expected Outcome :
                 "There was a problem, couldn't leave old square"
         '''
        model = Model()
        sq1 = Square(SquareType.Normal, 0, 0, model)
        p1 = Piece(PieceType.Lion, Square(SquareType.Normal, 0, 1, model), Player.One)
        self.assertEqual(sq1.tryToOccupy(p1), "There was a problem, couldn't leave old square")

    def test_empty1(self):
        '''
            test_empty1 tests the integrity of the empty function

            1.Functionality Tested : It Checks if it can empty a square that is already empty (o.e no Pieces)

            2. How It's Tested :
                We initlize a new board and check for an Empty square's coordinate to see if it's empty

            3. Expected Outcome :
                The Function is expected to return False
        '''
        model = Model()
        self.assertEqual(model.board[0][1].empty(),False)
    def test_empty2(self):
        '''
              test_empty2 tests the integrity of the empty function

              1.Functionality Tested : It Checks if it can empty a square that has an outgoing piece

              2. How It's Tested :
                  We initlize a new board.
                  We move the Piece Elephant of Team 2 to 5,0 from 6,0 by DIRECTLY acessssing the board.
                  We change the Elephant Piece's location by manipulating the Piece class's location
                  We check the output of the empty function

              3. Expected Outcome :
                  The Function is expected to return True
        '''

        model = Model()
        square = model.board[6][0]
        piece = square.occupiedPiece
        piece.location = model.board[5][0]
        self.assertEqual(square.empty(), True)
    def test_empty3(self):
        '''
              test_empty3 tests the integrity of the empty function

              1.Functionality Tested : It Checks if it can empty a square that has a piece but not marked as outgoing

              2. How It's Tested :
                  We initlize a new board.
                  We move the Piece Elephant of Team 2 to 5,0 from 6,0 by DIRECTLY acessssing the board.
                  We DO NOT change the Elephant Piece's location unlike test_empty2
                  We check the output of the empty function

              3. Expected Outcome :
                  The Function is expected to return False
        '''
        model = Model()
        square = model.board[6][0]
        piece = square.occupiedPiece


        self.assertEqual(square.empty(), False)

def run_some_tests():
   

    test_classes_to_run = [TestSquare, TestPiece,TestModel]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)

if __name__ == '__main__':
    run_some_tests()
