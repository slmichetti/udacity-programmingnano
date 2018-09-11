#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

# import random module for random.choice element
import random

moves = ['rock', 'paper', 'scissors']


# Creates main Player class. All subclass players inherit from this class
class Player:
    #
    def move(self):
        return 'rock'

    def learn(self, my_last_move, opponents_last_move):
        pass


# Create a computer player subclassthat plays randomly
class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


# Subclass player that copies the opponent's last move
class ReflectPlayer(Player):
    """
    Initializes player with a random move if player goes first since there
    will not be a previous move to call
    """
    def __init__(self):
        self.opponents_last_move = random.choice(moves)

    # Creates a move equal to opponent's last move
    def move(self):
        return self.opponents_last_move

    # Sets up the player to learn opponents previous move
    def learn(self, my_move, their_move):
        self.opponents_last_move = their_move


class CyclePlayer(Player):

    # Starts round with a random move for player
    def __init__(self):
        self.my_last_move = random.choice(moves)

    # Index last move to determine list placement and identify next move
    def move(self):
        index = moves.index(self.my_last_move)
        if index == 2:
            return moves[0]
        else:
            return moves[index + 1]

    # Sets up the player to recall its own previous move
    def learn(self, my_move, their_move):
        self.my_last_move = my_move


# Subclass for a Human Player
class Human(Player):
    """
    Function requests input from the human player to create the move.
    If the response is not found in the list of moves,it gives an error and
    asks for input again.
    """
    def move(self):
        Human_move = ""

        while True:
            Human_move = input(
                "Choose your weapon: rock, paper or scissors\n").lower()
            # Incorrect response - prompted to enter a new move
            if Human_move.lower() not in moves:
                print("Oops, I don't recognize that weapon. Please try again")
            else:
                break

        return Human_move


# Function to define what move beats another
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    # Init to establish players in the game, track each player's wins and ties
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1wins = 0
        self.p2wins = 0
        self.ties = 0

    # Prints winner for the round and totals for wins and ties
    def keep_score(self, move1, move2):
        # Determine who wins
        if beats(move1, move2):
            # add to score and print stats
            self.p1wins += 1
            print(f"{move1} beats {move2}! Player 1 wins this round!")
            print("Game Totals:")
            print(f" You: {self.p1wins}")
            print(f" Computer: {self.p2wins}")
            print(f" Ties: {self.ties}")
        # Reverse inputs to determine if its a tie
        elif beats(move2, move1):
            self.p2wins += 1
            print(f"{move2} beats {move1}! Player 2 wins this round!")
            print("Game Totals:")
            print(f" You: {self.p1wins}")
            print(f" Computer: {self.p2wins}")
            print(f" Ties: {self.ties}")
        else:
            self.ties += 1
            print("It's a tie!")
            print("Game Totals:")
            print(f" You: {self.p1wins}")
            print(f" Computer: {self.p2wins}")
            print(f" Ties: {self.ties}")

    # Displays final message signifying the end of the game with final scores
    def show_final_score(self):
        # Show final score of the game
        print("~~~~~~~~~~~~~~~~~~~~ GAME OVER! ~~~~~~~~~~~~~~~~~~~~")
        print("Final score:")
        print(f"Player One: {self.p1wins}")
        print(f"Player Two: {self.p2wins}")
        print(f"Ties: {self.ties}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    # Defines the moves played in the round
    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.keep_score(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # Starts the beginning of the game
    def play_game(self):

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~ PREPARE FOR BATTLE! ~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        # Identify round in range
        for round in range(1, 4):
            print(f"Round {round}: ")
            self.play_round()
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.show_final_score()


if __name__ == '__main__':
    game = Game(Human(), Cycle())
    game.play_game()
