from function1 import User
from storage1 import trivia_menu
x = True

name1 = input("Our  contestant tonight is.... ")
player1 = User(name1)
print(f"Hi {player1.name}! Welcome to Santa Cruz Trivia!")
while x == True:
    trivia_menu()
    User.play_game(player1)
