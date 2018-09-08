#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

# import random module for random.choice element
import random

moves = ['rock', 'paper', 'scissors']


# Player class, but this player always plays "rock".  #All subclass players inherit from this class.
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# create a computer player subclassthat plays randomly
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# create a computer player that remembers opponent's lsat move
# class ReflectPlayer(Player):
#    def learn(self, my_move, their_move):
#        pass

# create a subclass for comupter player that remembers last move and cycles through the remaining moves
# class CyclePlayer(Player):
#    def learn(self, my_move):
        # cycle through moves based on last move
#        pass

# create a subclass for a Human Player
class HumanPlayer(Player):
    def move(self):
        #player chooses move from list. 
        HumanPlayer_move = ""
        
        while True:
            HumanPlayer_move = input("Choose your weapon: rock, paper or scissors\n").lower()
            #if player's answer is incorrect or not found, prompted to enter a new move
            if HumanPlayer_move.lower() not in moves:
                print("Oops, you picked a weapon that is not a part of this game. Try again")
            else:
                break 
        
        return HumanPlayer_move


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
            print(f"Player One wins! Game Totals: Player One: {self.p1wins}, Player Two: {self.p2wins}, Ties: {self.ties}")
        # if p1 did not beat p2, reverse inputs to run p2 moves against p1 moves (if true, p2 wins, if false its a tie)
        elif beats(move2, move1):
            self.p2wins += 1
            print(f"Player Two wins! Game Totals: Player One: {self.p1wins}, Player Two: {self.p2wins}, Ties: {self.ties}")
        # if neither returns true, its a tie
        else:
            self.ties += 1
            print(f" It's a tie! Game Totals: Player One: {self.p1wins}, Player Two: {self.p2wins}, Ties: {self.ties}")

    def play_game(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~ PREPARE FOR BATTLE! ~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        # when choosing number of rounds for round in range(1,3)
        for round in range(1,4):
            print(f"Round {round}:")
            self.play_round()
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~ GAME OVER! ~~~~~~~~~~~~~~~~~~~~")
        print(f"Final score: Player One: {self.p1wins}, Player Two: {self.p2wins}, Ties: {self.ties}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
