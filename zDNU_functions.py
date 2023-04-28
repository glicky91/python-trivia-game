# TODO maybe add a class called easy --> gives a user a starting off bump of 3 points?
from storage import QUESTION_DICT, trivia_menu
import random


class Game:
    def __init__(self):
        self.is_playing = None
        self.answered_questions = []
        self.user_list = []

    # Below will include the way to ask and check answer for trivia.
    def gather_data(self):
        # here we are assigning the input to be in the user class and then also adding to the list
        self.user_list.append(
            User(input("Our first contestant tonight is.... ")))
        self.user_list.append(
            User(input("Our second contestant tonight is.... ")))
        print(
            f"Hi {self.user_list[0].name} and {self.user_list[1].name}! Welcome to Santa Cruz Trivia!")
        # Here we are choosing a random user to go first by assigning it to self.is_playing (self is the game and we are using is_playing as current_user )
        self.is_playing = random.choice(self.user_list)
        print(
            f"To start off we have randomly chosen {self.is_playing.name} to go first!")

    def debug(self):
        print("The current player is", self.is_playing.name,
              "The other player is", self.other_player().name)

    def ask_question(self):
        trivia_menu()
        print(
            f"It is {self.is_playing.name}'s turn to try their luck at Trivia!")
        selected_cat = input(
            "Please type the number of the catagory you would like your question to be: ")
        if selected_cat == "6":
            print(
                f"Goodbye {self.is_playing.name} and {self.other_player().name}.The ending score is\n{self.is_playing.name}:{self.is_playing.points}\n{self.other_player().name}:{self.other_player().points}. We hope to see you again soon.")
            exit()
        selected_level = input(
            "Select your complexity level. 1 is the easiest and 3 is the hardest. The harder the question the more points you get!\n")
        quest = selected_cat+selected_level
        if quest in self.answered_questions:
            print(
                "You or your opponent have already correctly answered this question. Please select a new one.")
            return
        selected_answer = input(QUESTION_DICT[selected_cat][selected_level][0])
        if selected_answer == QUESTION_DICT[selected_cat][selected_level][1]:
            self.answered_questions.append(quest)
            self.is_playing.points += int(selected_level)
            print(
                f"You have selectd the correct answer! Your score is now {self.is_playing.points}.")
            self.extremes()
        else:
            self.is_playing.points -= 1
            # TODO something about the other persons turn to play
            print(
                f"Incorrect! Your score is now {self.is_playing.points}. It is now {self.other_player().name}'s turn to play.")
            self.extremes()
            self.switch()

    def extremes(self):
        if self.is_playing.points < 0:
            print(
                f"Game over. You lose. Your ending score was {self.is_playing.points}.Your opponent wins")
            exit()
        if len(self.answered_questions) >= 15:
            # TODO order the users by points... mabye user.list.sort(key = points, reverse)
            print(
                f"Congratulations! The game has been won. The ending score is:\n{self.user_list[0].name}:{self.user_list[0].points}\n{self.user_list[1].name}:{self.user_list[1].points}")
            exit()

    def switch(self):
        for player in self.user_list:
            if player != self.is_playing:
                self.is_playing = player
                break

    def other_player(self):
        for player in self.user_list:
            if player != self.is_playing:
                return player


class User:
    def __init__(self, name):
        self.points = 0
        self.name = name


# Functions to play game.
# Question for this section: How do I show that the players are both under classes of User and Game?


# Question: How do I pull in the current_player selected above? I'm also struggling to initalize the classes in this funct. If I initialize them it is making me pull in name and is_playing which doesn't work.
