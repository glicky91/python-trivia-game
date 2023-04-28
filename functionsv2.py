from storage import QUESTION_DICT, trivia_menu
import random


class User:
    def __init__(self, name):
        self.points = 0
        self.name = name


class Easy(User):
    def __init__(self, name):
        super().__init__(name)
        self.points = 3


class Game:
    def __init__(self):
        self.is_playing = None
        self.answered_questions = []
        self.user_list = []

# This function is where we gather the user's names and determine who goes first as well as what mode it is [ easy or hard]
    def gather_data(self):
        # here we are assigning the input to be in the user class and then also adding to the list
        level = input(
            "Would you both like to play on easy mode? This will start you off with 3 additional points and give you a buffer in case you get one of your first questions wrong.\nType in yes or no.")
        if level.lower() == "yes":
            self.user_list.append(
                Easy(input("Our first contestant tonight is.... ")))
            self.user_list.append(
                Easy(input("Our second contestant tonight is.... ")))
        else:
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

    # Used this code to test out a few differnt issues I was having
    # def debug(self):
    #     print("The current player is", self.is_playing.name,
    #           "The other player is", self.other_player().name)

    def ask_question(self):
        trivia_menu()
        print(
            f"It is {self.is_playing.name}'s turn to try her/his luck at Trivia!")
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
