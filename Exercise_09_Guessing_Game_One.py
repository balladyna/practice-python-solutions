import random

prompt = ">>> "
guess_message = "Choose a number from 1 to 9. If you want to end game just type 'exit':\n"
high_number_message = "Number is to high! Try again!"
low_number_message = "Number is to low! Try again!"
goodbye_message = "Goodbye! To the next time!"
wrong_input_message = "Do you really want "
win_message = "Congratulation! You guess computer number!"

list_of_numbers = range(1, 10)
computer_choice = random.choice(list_of_numbers)


def play_game():
    user_choice_int = int(user_choice)
    if user_choice_int > computer_choice:
        print(high_number_message)
    elif user_choice_int < computer_choice:
        print(low_number_message)


while True:
    user_choice = (input(guess_message + prompt))
    if user_choice.isnumeric():
        if int(user_choice) == computer_choice:
            print(win_message + " " + goodbye_message)
            break
        else:
            play_game()
            continue
    else:
        if user_choice == 'exit':
            print(goodbye_message)
            break
        else:
            print(wrong_input_message + user_choice + "???")
            continue
