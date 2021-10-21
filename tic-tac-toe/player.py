import math 
import random

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        """The computer will choose a random spot/square on the board that is empty"""
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        """
        The human will choose a random spot/square on the board that is available. The method will do tests to ensure the spot chosen and the value placed there is valid
        """
        valid_square = False
        value = None

        while not valid_square:
            square = input(self.letter + "'s turn. Please input 0-8: ")

            #Checks 
            #Is the value input a valid one
            #Is the spot chosen available or does it have data on it
            try: 
                value = int(square) #Turns the string into an integer
                if value not in game.available_moves(): #Ensures the spot chosen is available
                    raise ValueError
                valid_square = True #If all checks pass the square is valid and value is okay
            except ValueError:
                print("Invalid input! Please try again!")

        return value
