import random
from functionsv2 import User, Game, Easy

x = True
my_game = Game()
my_game.gather_data()
# my_game.debug()


while x == True:
    my_game.ask_question()
