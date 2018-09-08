#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

#import random module for random.choice element
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

#Main player - only move is rock
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

#create a player subclass that plays randomly
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1wins = 0 #keeps track of number of wins player one
        self.p2wins = 0 #of wins player two
        self.ties = 0 #of tie games
#       self.learn[]

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        #determine who wins
        if beats(move1, move2): #pass in moves from round to run through beats to determine winner
            #add to score and print stats
            self.p1wins += 1
            print(f"Player One wins! Game Totals: Player One: {self.p1wins}, Player Two: {self.p2wins}, Ties: {self.ties}")
        #if p1 did not beat p2, reverse inputs to run p2 moves against p1 moves (if true, p2 wins, if false its a tie)
        elif beats(move2, move1):
            self.p2wins += 1
            print(f"Player Two wins! Game Totals: Player One: {self.p1wins}, Player Two: {self.p2wins}, Ties: {self.ties}")
        #if neither returns true, its a tie 
        else:
            self.ties += 1
            print(f" It's a tie! Game Totals: Player One: {self.p1wins}, Player Two: {self.p2wins}, Ties: {self.ties}")


    def play_game(self):
        print("Prepare for battle!")
        for round in range(1, 4): #when choosing number of rounds for round in range(1,3)
            print(f"Round {round}:")
            self.play_round()
        print(f"Game over! Final score: Player One: {self.p1wins}, Player Two: {self.p2wins}, Ties: {self.ties}")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()

