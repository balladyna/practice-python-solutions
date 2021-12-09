import random
from Exercise_08_dict_en import game_dict_en
from Exercise_08_dict_pl import game_dict_pl

rock = "1"
scissors = "2"
paper = "3"
game_options = [rock, scissors, paper]

prompt = "\n>>> "

language_message = "Choose language / Wybierz język. For English 1, for Polish 2:"
unknown_input_message = "Unknown input, try again / Nieznana wartość, spróbuj jeszcze raz."


def play_game(game_dict):
    computer_choice = random.choice(game_options)
    user_choice = input((game_dict["options_message"]) + prompt)
    user_choice_lower = user_choice.lower()

    if user_choice_lower not in game_options:
        print((game_dict["try_again_message"]))
    elif computer_choice == user_choice_lower:
        print((game_dict["draw_message"]))
    elif computer_choice == rock:
        if user_choice_lower == paper:
            print((game_dict["win_message_rock"]))
        else:
            print((game_dict["defeat_message_rock"]))
    elif computer_choice == scissors:
        if user_choice_lower == rock:
            print((game_dict["win_message_scissors"]))
        else:
            print((game_dict["defeat_message_scissors"]))
    elif computer_choice == paper:
        if user_choice_lower == scissors:
            print((game_dict["win_message_paper"]))
        else:
            print((game_dict["defeat_message_paper"]))


def new_game(game_dict):
    user_command = input((game_dict["new_game_message"]) + prompt)
    yes_option = "1"
    no_option = "2"

    if user_command == no_option:
        print((game_dict["goodbye_message"]))
        exit()
    elif user_command != yes_option:
        print((game_dict["wrong_input_message"]) + user_command + "???")
        exit()


language_message = input(language_message + prompt)
english_dict_option = "1"
polish_dict_option = "2"

while True:
    if language_message == english_dict_option:
        play_game(game_dict_en)
        new_game(game_dict_en)
    elif language_message == polish_dict_option:
        play_game(game_dict_pl)
        new_game(game_dict_pl)
    else:
        print(unknown_input_message)
        break
