from unittest.mock import patch
import unittest
from Model import *
from Constants import *

wrong_select = "You can't choose Opponent's Piece!"
s = "You have selected "
n = "No Piece Exists in position"


class UnitTestCase(unittest.TestCase):
    '''
    Testing all the valid possible cases that can performed on the Model.selectPiece() function
    '''
    def test_if_other_pieces_can_move_into_water(self):
        model = Model()
        model.selectPiece('3C')
        self.assertEqual(model.attemptMove('4C'),"Illegal Move, You can't move into water. Only Rat(1) Can!")
    def test_square_empty(self):
        model = Model()
        self.assertEqual(model.board[0][0].empty(),False)
    def test_attack_own_den_p2(self):
        model = Model()
        model.changeTurns()
        model.selectPiece('9A')
        model.attemptMove('9B')

        model.changeTurns()
        model.selectPiece('9B')
        model.attemptMove('9C')

        model.changeTurns()

        model.selectPiece('9C')
        self.assertEqual(model.attemptMove('9D'),"Illegal Move! You tried to move to your own den square")
    def test_intervening(self):
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
        self.assertEqual(model.attemptMove('4D'),'Invalid Jump attempted!')
    def test_attack_own_den_p1(self):
        model = Model()
        model.selectPiece('1A')
        model.attemptMove('1B')

        model.changeTurns()
        model.selectPiece('1B')
        model.attemptMove('1C')

        model.changeTurns()

        model.selectPiece('1C')
        self.assertEqual(model.attemptMove('1D'),"Illegal Move! You tried to move to your own den square")
    def test_select_piece(self):
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

        # try to select own pieces
        self.assertIn(s, model.selectPiece('3A'))
        self.assertIn(s, model.selectPiece('1A'))
        self.assertIn(s, model.selectPiece('2B'))
        self.assertIn(s, model.selectPiece('3C'))
        self.assertIn(s, model.selectPiece('3E'))
        self.assertIn(s, model.selectPiece('2F'))
        self.assertIn(s, model.selectPiece('1G'))
        self.assertIn(s, model.selectPiece('3G'))

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

        # switch turn
        model.playerTurn = Player.Two
        self.assertEqual(model.selectPiece(
            '3A'), wrong_select)  # add assertion here
        self.assertEqual(model.selectPiece('1A'), wrong_select)
        self.assertEqual(model.selectPiece('2B'), wrong_select)
        self.assertEqual(model.selectPiece('3C'), wrong_select)
        self.assertEqual(model.selectPiece('3E'), wrong_select)
        self.assertEqual(model.selectPiece('2F'), wrong_select)
        self.assertEqual(model.selectPiece('1G'), wrong_select)
        self.assertEqual(model.selectPiece('3G'), wrong_select)
        # testing own player's pieces
        self.assertIn(s, model.selectPiece('7A'))
        self.assertIn(s, model.selectPiece('9A'))
        self.assertIn(s, model.selectPiece('8B'))
        self.assertIn(s, model.selectPiece('7C'))
        self.assertIn(s, model.selectPiece('7E'))
        self.assertIn(s, model.selectPiece('8F'))
        self.assertIn(s, model.selectPiece('7G'))
        self.assertIn(s, model.selectPiece('9G'))

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
    def test_move_piece_same_square(self):
        model = Model()
        model.selectPiece('1A')
        self.assertEqual(model.attemptMove('1A'),"Invalid Jump attempted!")
        self.assertIn("Succesfully moved piece to square",model.attemptMove('2A'))

        model.selectPiece('9A')
        model.attemptMove('8A')

        model.selectPiece('2A')
        self.assertIn("This square is already occupied by your Piece",model.attemptMove('3A'))

    def test_unselect(self):
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

    def test_attempt(self):
        model = Model()
        model.selectPiece('1A')
        self.assertEqual(model.attemptMove('3A'), 'Invalid Jump attempted!')
        self.assertEqual(model.attemptMove('9G'), 'Invalid Jump attempted!')
        self.assertEqual(model.attemptMove('6B'), 'Invalid Jump attempted!')
        self.assertEqual(model.attemptMove('1A'), 'Invalid Jump attempted!')
        self.assertEqual(model.attemptMove(
            '2A'), 'Succesfully moved piece to square (2, \'A\')')
        self.assertEqual(model.playerTurn, Player.Two)

    def test_change_player(self):
        model = Model()
        self.assertEqual(model.playerTurn, Player.One)
        model.changeTurns()
        self.assertEqual(model.playerTurn, Player.Two)
        model.changeTurns()
        model.changeTurns()
        self.assertEqual(model.playerTurn, Player.Two)

    def test_is_intervened(self):
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

    def test_piece_attack_rat_attack_elephant(self):
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

        model.selectPiece('5A')
        model.attemptMove('6A')

        self.assertEqual(model.board[5][0].occupiedPiece.type, PieceType.Rat)
        self.assertEqual(model.deadPiecesPlayerTwo, 1)

    def test_piece_attack_elephant_attack_rat(self):
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
        self.assertEqual(model.attemptMove('5A'),"Inelligible Attack")
        self.assertEqual(model.board[0][6].occupiedPiece.attack(model.board[0][2]),True)
        self.assertEqual(model.board[4][0].occupiedPiece.type, PieceType.Rat)


    def test_attack_rat_elephant_from_water(self):
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
        self.assertEqual(model.attemptMove(
            '6A'), "Cross-Border attack isn't allowed!")

        self.assertEqual(
            model.board[5][0].occupiedPiece.type, PieceType.Elephant)
        self.assertEqual(model.board[5][1].occupiedPiece.type, PieceType.Rat)

    def test_if_lion_can_jump(self):
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

    def test_if_tiger_can_jump(self):
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

    def test_if_others_can_jump(self):
        model = Model()
        model.selectPiece('2B')
        model.attemptMove('3B')

        model.selectPiece('9A')
        model.attemptMove('9B')

        model.selectPiece('3B')
        model.attemptMove('7B')

        self.assertEqual(model.board[6][1].occupiedPiece, None)
        self.assertEqual(model.board[2][1].occupiedPiece.type, PieceType.Dog)

    def test_player_two_kill(self):
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

        self.assertEqual(model.deadPiecesPlayerOne,1)

if __name__ == '__main__':
    unittest.main()
