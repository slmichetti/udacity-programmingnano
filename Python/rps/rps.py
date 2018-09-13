#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

# import random module for random.choice element
import random

moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']
affirmatives = ['yes', 'yea', 'yep', 'y', 'sure']
negatives = ['n', 'no', 'nope', 'nay']

# Creates main Player class. All subclass players inherit from this class
class Player:
    # Player always returns move rock
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Create a computer player subclassthat plays randomly
class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


# Subclass player that copies the opponent's last move
class ReflectPlayer(Player):

    # Starts player with a random move since no previous move to call
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
        if index == 4:
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
                "Choose your weapon: rock, paper, scissors, lizard or spock: "
            ).lower()
            # Incorrect response - prompted to enter a new move
            if Human_move.lower() not in moves:
                print("Oops, I don't recognize that weapon. Please try again")
            else:
                break

        return Human_move


# Function to define what move beats another
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'rock' and two == 'lizard') or
            (one == 'scissors' and two == 'lizard') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock') or
            (one == 'paper' and two == 'spock') or
            (one == 'lizard' and two == 'paper') or
            (one == 'lizard' and two == 'spock') or
            (one == 'spock' and two == 'rock') or
            (one == 'spock' and two == 'scissors'))


class Game:

    # Init to establish players in the game, track each player's wins and ties
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1wins = 0
        self.p2wins = 0
        self.ties = 0
        self.rounds = 0
        
    # Human Player picks number of rounds to play
    def ask_rounds(self):
        while True:
            num_rounds = input(
                "Enter the number of rounds you would like to play: ")
            #check for valid number
            if num_rounds.isnumeric():
                num_rounds = int(num_rounds)
                if num_rounds <= 0:
                    print ("Please pick a valid number:  ")
                elif num_rounds > 9:
                    print ("Max number of rounds is 9. Please pick again:  ") 
                else:
                    print(f"Cool! Let's play {num_rounds} rounds!\n")
                    self.rounds = num_rounds
                    break
            else:
                print("I don't know that number. Please try again.")      

    def draw_separator(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    #player input choose opponent
    def choose_opponent(self):
        print(
        "~~~~~~~~~~~~~~~~~~~~~CHOOSE YOUR OPPONENT~~~~~~~~~~~~~~~~~~~~~"
        "\n [1] Rocker: rocks out on every move." 
        "\n [2] Suprise: you never know what move this opponent will make."
        "\n [3] Mockingbird: mimics your last move."
        "\n [4] Cyclist: moves in cycles through the moves.\n")
        while True:
            opponent_choice = (input("Enter your choice now: "))
            if opponent_choice == "1":
                self.p2 = Player()
                break
            elif opponent_choice == "2":
                self.p2 = RandomPlayer()
                break
            elif opponent_choice == "3":
                self.p2 = ReflectPlayer()
                break
            elif opponent_choice == "4":
                self.p2 = CyclePlayer()
                break
            else: print("I'm sorry. I didnt understand, please try again.")


    # Prints winner for the round and totals for wins and ties
    def keep_score(self, move1, move2):
        # Determine who wins
        if beats(move1, move2):
            # add to score and print stats
            self.p1wins += 1
            print(f"{move1} beats {move2}! Player 1 wins this round!")
            print("Game Totals:")
            print(f" Player One: {self.p1wins}")
            print(f" Player Two: {self.p2wins}")
            print(f" Ties: {self.ties}")
        # Reverse inputs to determine if its a tie
        elif beats(move2, move1):
            self.p2wins += 1
            print(f"{move2} beats {move1}! Player 2 wins this round!")
            print("Game Totals:")
            print(f" Player One: {self.p1wins}")
            print(f" Player Two: {self.p2wins}")
            print(f" Ties: {self.ties}")
        else:
            self.ties += 1
            print("It's a tie!")
            print("Game Totals:")
            print(f" Player One: {self.p1wins}")
            print(f" Player Two: {self.p2wins}")
            print(f" Ties: {self.ties}")

    # Displays final message signifying the end of the game with final scores
    def show_final_score(self):
        # Show final score of the game
        print("~~~~~~~~~~~~~~~~~~~~ GAME OVER! ~~~~~~~~~~~~~~~~~~~~")
        if self.p1wins > self.p2wins:
            print("*****PLAYER ONE WINS!!*****")
        elif self.p2wins > self.p1wins:
            print("*****PLAYER TWO WINS!!*****")
        else:
            print("There is no winner. Games were tied!")
        print("Final score:")
        print(f"Player One: {self.p1wins}")
        print(f"Player Two: {self.p2wins}")
        print(f"Ties: {self.ties}")
        self.draw_separator()
        

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

        self.draw_separator()
        print(
            "  WELCOME TO ROCK, PAPER, SCISSORS, LIZARD, SPOCK!      ")
        self.draw_separator()
        print(
            "Your moves: Rock, Paper, Scissors, Lizard or Spock.\n"
            "\n   Rules of the game:"
            "\n     ~ Rock crushers Scissors and Lizard."
            "\n     ~ Scissors cut Paper and decapitate Lizard."
            "\n     ~ Lizard eats Paper and poisons Spock."
            "\n     ~ Paper disproves Spock and covers Rock."
            "\n     ~ Spock vaporizes Rock and smashes Scissors.\n")
        self.draw_separator()
        while True:
            ready = input("Are you ready (Y/N)? ").lower()
            if ready.lower() in affirmatives:
                break             
            elif ready.lower() in negatives:
                print("Ok. Come back when you're ready to play")
                return
            else:
                print("I am not sure what you want to do. Try again.")

        self.ask_rounds()
        self.choose_opponent()
        self.draw_separator()
        print("                 PREPARE FOR BATTLE! ")
        self.draw_separator()
        for round in range(0, self.rounds):  
            print(f"Round {round+1}: ")
            self.play_round()
        self.draw_separator()
        self.show_final_score()


if __name__ == '__main__':
    game = Game(Human(), RandomPlayer())
    game.play_game()

