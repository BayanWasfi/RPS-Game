import random
import sys
from termcolor import colored
import time
# Here were the type moves rock, paper and scissors.
moves = ['rock', 'paper', 'scissors']


# Parent class always plays rock and learn move
class Player():

    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, learn_move):
        pass


# Subclass RandomPlayer, computer chooses its move at random
class RandomPlayer(Player):
    def move(self):
        user_input = random.choice(moves)
        return (user_input)


# Subclass ReflectPlayer that remembers what move opponent played last round.
class ReflectPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.learn_move = moves[0]

    def move(self):
        if self.learn_move is None:
            user_input = moves[0]
        else:
            user_input = self.learn_move
            return (user_input)

    def learn(self, learn_move):
        self.learn_move = learn_move


# Subclass that choses an item from the moves function
# in organised order and cycle it in this order rock, paper and scissors
class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.step = 0

    def move(self):
        user_input = None
        if self.step == 0:
            user_input = moves[0]
            self.step = self.step + 1
        elif self.step == 1:
            user_input = moves[1]
            self.step = self.step + 1
        else:
            user_input = moves[2]
            self.step = self.step - 2
        return user_input


# This subclass that ask the user to choose an option, also validate user input
class HumanPlayer(Player):

    def move(self):
        while True:
            user_input = input('rock, paper, scissors? \
            \nor q for quitting! ')
            user_input = user_input.lower().strip()
            # Gives the user an option to quit the game at any time
            if user_input in ['q']:
                print('quitting...')
                sys.exit(0)
            # This part check if the validity of the input
            elif (user_input != 'rock' and user_input != 'paper'
                  and user_input != 'scissors'):
                print('Invalid input. Choose:')
            else:
                return(user_input)


# The game controller, where it control the game and number of rounds
# it also give the option of exiting the game at any time
class Game():

    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_game(self):
        print("Game start!\
        \nThe rules are: rock beats scissors\
        \npaper beats rock \
        \nand scissors beat paper.\
        \nEnter q if you want to quit the game")
        for round in range(7):
            time.sleep(1)
            print(f"===Round {round}===")
            self.play_round()
        if self.p1.score > self.p2.score:
            print(colored('You are the WINNER!', 'red'))
        elif self.p1.score < self.p2.score:
            print(colored('Computer is the WINNER!', 'red'))
        else:
            print(colored('Tie!', 'red'))
        print(f"The final score: \
        \n{self.p1.score} for You & {self.p2.score} for Computer")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = self.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play(self, move1, move2):
        print(f"\n\nYou played {move1}")
        print(f"Opponent played {move2}\n\n")

        if move1 == 'q':
            sys.exit(0)
        elif beats(move1, move2):
            print(colored("--> You Win!!", 'green', 'on_cyan'))
            self.p1.score += 1
            print(f"Score: You: {self.p1.score},\
             Computer: {self.p2.score}\n\n")
            return 1
        elif beats(move2, move1):
            print(colored("--> Computer Win!!", 'green', 'on_cyan'))
            self.p2.score += 1
            print(f"Score: You: {self.p1.score},\
             Computer: {self.p2.score}\n\n")
            return 2
        else:
            print(colored("--> Tie!!", 'green', 'on_cyan'))
            print(f"Score: You: {self.p1.score},\
             Computer: {self.p2.score}\n\n")
            return 0


# A function that set all the possible winning options, in other words,
# if move one plays against move two then the player that played move one
# will win
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


#  The code will start from here, if the user enter an invalid option
# it throws an error and ask the user to enter the correct option
if __name__ == '__main__':
    while True:
        while True:
            p2 = input('Whom do you want to play against?\n[1]Rock Player \
            \n[2]Random Player\n[3]Reflective Player \
            \n[4]Cycles Player\n').strip()
            if p2 == '1':
                p2 = Player()
                break
            elif p2 == '2':
                p2 = RandomPlayer()
                break
            elif p2 == '3':
                p2 = ReflectPlayer()
                break
            elif p2 == '4':
                p2 = CyclePlayer()
                break
            else:
                print('Not valid input, please enter from 1 to 4: ')

    # Create a game object and quit function is also available
        g = Game(p2)
        g.play_game()
        while True:
            a = input('Do you want to play again? (Y or N): ').upper()
            if a in ['N']:
                print('quitting game...')
                sys.exit(0)
            elif a in ['Y']:
                break
            else:
                print('Not valid input, please enter Y or N: ')
