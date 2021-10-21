from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe():
    def __init__(self):
        self.board = [ " " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [ self.board [i*3: (i+1)*3 ] for i in range(3)]:
            print( " | " + " | ".join(row) + " | ")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        
        for row in number_board:
            print( " | " + " | ".join(row) + " | ")

    def available_moves(self):
        """This returns a list of all the available spots on the board"""
        return [ i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        """This function returns if there are empty squares"""
        return " " in self.board

    def num_empty_squares(self):
        """This function counts the number of empty squares"""
        # return len(self.available_moves())
        return self.board.count(" ")

    def winner (self, square, letter):
        """
        This method checks for the winner of the game.
        Winners are gotten through having the same letter on a row, diagonal or column
        """
        # 1. Check for winners on a row 
        row_index = square //3 # - Check the row of the square selected 
        row = self.board[row_index*3: (row_index+1)*3] #A list of all items in that row
         #Checks that there are no empty spaces in the row AND that all the spots are the same as the letter
        if all([ spot == letter for spot in row ]):
            return True
             
        # 2. Check for winner on a column
        col_index = square % 3
        column = [ self.board[col_index + i * 3] for i in range(3)]
        if all ( spot == letter for spot in column):
            return True
        
        # 3. Check the diagonals whose index is  even i.e. 0,2,4,6,8
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left-right diagonal
            if all ( spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right-left diagonal
            if all ( spot == letter for spot in diagonal2):
                return True

        # 4. If all the checks fail, there is no winner
        return False


    def make_move(self, square, letter_of_player):
        """This function allows a selected player to make a move on the board.
        If the move is valid (spot on board is available and the number passed in is an int), 
        then make the move - assign the square to the letter of the player"""

        if self.board[square] == " ":
            self.board[square] = letter_of_player
            # This method checks for the winner
            if self.winner(square, letter_of_player):
                self.current_winner = letter_of_player
            return True
        return False


def play(game, x_player, o_player, print_game=True):
    """This is the game being played."""
    if print_game:
        game.print_board_nums() #This will help us see all the moves being made using the index of the spots chosen

    letter = "X" # This is the starting player

    # Keep iterating until all the spots in the board are filled.
    while game.empty_squares():
        # 1. Get the move from the appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)


        # 2. Let the players make moves until the board is filled and a winner declared
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}.".format(square))
                game.print_board()
                print("")
        
        # 4. Check for a current winner before assigning the next player
        if game.current_winner:
            if print_game:
                print(letter + " wins!")
                return letter # This is the winner
        
        # 3. After X player, it should be O player's turn
        letter = "O" if letter == "X" else "X"

        # Slow down time
        time.sleep(1)

    # Just in case that it is a tie
    if print_game():
        print("It is a tie!")


# Running the game
if __name__ == '__main__':
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe() #Instance of the class
    play(game=t, x_player=x_player, o_player=o_player, print_game=True)