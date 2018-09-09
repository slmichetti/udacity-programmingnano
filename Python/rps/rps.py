#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

# import random module for random.choice element
import random

moves = ['rock', 'paper', 'scissors']


# Player class. This main player always plays "rock"
# All subclass players inherit from this class
class Player:
    # Initializes the player class and creates random previous moves
    def __init__(self):
        self.own_previous_move = random.choice(moves)
        self.opponents_last_move = random.choice(moves)

    def move(self):
        return 'rock'

    # Used to update the previous moves for the player and opponent
    def learn(self, my_move, their_move):
        self.own_previous_move = my_move
        self.opponents_last_move = their_move


# Create a computer player subclassthat plays randomly
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Subclass for a Human Player
class HumanPlayer(Player):
    def move(self):
        # Player chooses move from list
        HumanPlayer_move = ""

        while True:
            HumanPlayer_move = input("Choose your weapon: rock, paper or scissors\n").lower()
            # Incorrect response - prompted to enter a new move
            if HumanPlayer_move.lower() not in moves:
                print("Oops, I don't recognize that weapon. Try again")
            else:
                break

        return HumanPlayer_move


# Subclass player that copies the opponent's last move
class ReflectPlayer(Player):
    # Call def learn for opponent's last move
    def move(self):
        return self.opponents_last_move


# Subclass player -remembers last move and cycles through  moves
class CyclePlayer(Player):
    # Call def learn to get last move to cycle through list
    def move(self):
        index = moves.idex(self.own_previous_move)
        if index == 2:
            return moves[0]
        else:
            return moves[index+1]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1wins = 0  # keeps track of number of wins player one
        self.p2wins = 0  # of wins player two
        self.ties = 0  # of tie games

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # determine who wins
        if beats(move1, move2):
            # add to score and print stats
            self.p1wins += 1
            print("Player One wins!")
        # Reverse inputs to determine if its a tie
        elif beats(move2, move1):
            self.p2wins += 1
            print("Player Two wins!")
        else:
            self.ties += 1
            print("It's a tie!")

    def play_game(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~ PREPARE FOR BATTLE! ~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        # Identify round in range
        for round in range(1,4):
            print(f"Round {round}:")
            self.play_round()
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~ GAME OVER! ~~~~~~~~~~~~~~~~~~~~")
        print("Final score:")
        print(f"Player One: {self.p1wins}")
        print(f"Player Two: {self.p2wins},")
        print(f"Ties: {self.ties}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
