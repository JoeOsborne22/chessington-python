"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square
class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """

        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        
        squares_y_axis=1
        if self.player.name == 'BLACK':
            squares_y_axis=-1

        cur_Pos= board.find_piece(self)
        checkIfUnmoved = (cur_Pos.row == 1 and self.player.name == 'WHITE') or (cur_Pos.row == 6 and self.player.name == 'BLACK')
        # checkIfUnmoved = (cur_Pos.row == 1 and self.player.name == 'WHITE') or (cur_Pos.row == 6 and self.player.name == 'BLACK')

        
        poss_moves = []
        #find all cells on board
        boardCells=[]
        for row in range(0,len(board.board)):
            for cell in range(0,len(board.board[row])):
                boardCells.append([row,cell])
                
        if valid_square (cur_Pos.row + squares_y_axis): 
            row_increment = cur_Pos.row + squares_y_axis 
        else:
            row_increment = cur_Pos.row    
                  
        pawn_one=(Square.at(row_increment,cur_Pos.col)) #move forward one square
        
        #check if piece diagonally across
        pawn_take=[]
        pawn_take.append(Square.at(row_increment,cur_Pos.col+1)) #Take piece to left forward one square
        pawn_take.append(Square.at(row_increment,cur_Pos.col+ -1)) #Take piece to left forward one square
        for check in pawn_take:
            if board.get_piece(check) is not None:
                poss_moves.append(check)

        #check if pawn_one off board
        if board.get_piece(pawn_one) == None and pawn_one not in poss_moves :
            poss_moves.append(pawn_one)
            
            if checkIfUnmoved:
                #check if square off board
                if valid_square (cur_Pos.row + 2 * squares_y_axis ): 
                    pawn_two = Square.at(cur_Pos.row + 2 * squares_y_axis, cur_Pos.col) 
                else: 
                    pawn_two = Square.at(cur_Pos.row, cur_Pos.col) 
               
                if board.get_piece(pawn_two) == None and pawn_two not in poss_moves:
                     poss_moves.append(pawn_two)    
            
        return poss_moves

def valid_square (self): 
    return self >= 0 and self <= 7 
             

class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []