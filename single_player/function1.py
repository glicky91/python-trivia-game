from storage1 import QUESTION_DICT


class User:
    def __init__(self, name):
        self.points = 0
        self.name = name
        self.my_list = []

    def neg_points(self):
        if self.points < 0:
            print(
                f"Game over. You lose. Your ending score was {self.points}.")
            exit()

    def play_game(self):
        if len(self.my_list) >= 15:
            print(
                f"Congratulations! You won the game. The ending score is:\n{self.name}:{self.points}")
            exit()
        selected_cat = input(
            "Please type the number of the catagory you would like your question to be: ")
        if selected_cat == "6":
            print(
                f"Goodbye, the ending score is\n{self.name}:{self.points}\n I hope to see you again soon.")
            exit()
        selected_level = input(
            "Select your complexity level. 1 is the easiest and 3 is the hardest. The harder the question the more points you get!\n")
        quest = selected_cat+selected_level
        if quest in self.my_list:
            print(
                "You have already correctly answered this question. Please select a new one.")
            return
        selected_answer = input(QUESTION_DICT[selected_cat][selected_level][0])
        if selected_answer == QUESTION_DICT[selected_cat][selected_level][1]:
            self.my_list.append(quest)
            self.points += int(selected_level)
            print(
                f"You have selectd the correct answer! Your score is now {self.points}.")
        else:
            self.points -= 1
            User.neg_points(self)
            print(
                f"Incorrect! You have lost a point. Your score is now {self.points}.")
