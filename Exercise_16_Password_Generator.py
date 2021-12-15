import string
import random


class Option:
    yes = "1"
    no = "2"
    weak_password = "1"
    strong_password = "2"
    exit_program = "3"


class Message:
    new_password = "How strong your new password should be? Type no. of option:\n" \
                   "1. weak (not recommended!)\n" \
                   "2. strong\n" \
                   "3. exit from program:\n"
    weak_option = "Are sure that you want weak password? Type no. of option:\n" \
                  "1. yes\n" \
                  "2. no\n" \
                  "3. exit from program\n"
    weak_result = "Here are propositions of two passwords:"
    character_password = "How many characters your password should have? " \
                         "You can choose between 5 and 20 characters. For exit choose 3.\n"
    strong_result = "Your new password is:\n"
    wrong_input = "Wrong input!"
    goodbye = "Goodbye!"


weak_password_list = ['123456', '123456789', '12345', 'qwerty', 'password', '12345678', '111111', '123123',
                      '1234567890', '1234567', 'qwerty123', '000000', '1q2w3e', 'aa12345678', 'abc123', 'password1',
                      '1234', 'qwertyuiop', '123321', 'password123', 'iloveyou', '1q2w3e4r', 'dragon', 'monkey',
                      'asdfghjkl', 'myspace1', 'fuckyou', 'football', 'princess', 'sunshine', 'michael', 'computer',
                      'daniel', 'shadow', 'samsung', 'killer', 'superman', 'master', 'azerty', 'ashley', 'target123',
                      'baseball', 'qwerty', 'soccer', 'charlie', 'tinkle', 'jessica', 'q1w2e3r4t5''12345', 'qwerty',
                      'password', '12345678', '111111', '123123', '1234567890', '1234567', 'qwerty123', '000000',
                      '1q2w3e', 'aa12345678', 'abc123', 'password1', '1234', 'qwertyuiop', '123321', 'password123',
                      'iloveyou', '1q2w3e4r', 'dragon', 'monkey', 'asdfghjkl', 'myspace1', 'fuckyou', 'football',
                      'princess', 'sunshine', 'michael', 'computer', 'daniel', 'shadow', 'samsung', 'killer',
                      'superman', 'master', 'azerty', 'ashley', 'target123', 'baseball', 'qwerty', 'soccer', 'charlie',
                      'tinkle', 'jessica', 'q1w2e3r4t5']

prompt = ">>> "


def generate_weak_password():
    user_input = input(Message.weak_option + prompt)
    while Option.no != user_input:
        if Option.yes == user_input:
            weak_password_one = random.choice(weak_password_list)
            weak_password_two = random.choice(weak_password_list)
            if weak_password_two == weak_password_one:
                weak_password_two = random.choice(weak_password_list)
            else:
                print(Message.weak_result)
                print(weak_password_one + " and " + weak_password_two)
                print(Message.goodbye)
                exit()
        elif Option.no == user_input:
            break
        elif Option.exit_program == user_input:
            print(Message.goodbye)
            exit()
        else:
            print(Message.wrong_input)
            continue


def generate_strong_password():
    while True:
        password_length_input = input(Message.character_password + prompt)
        if password_length_input.isnumeric():
            if 5 <= int(password_length_input) <= 20:
                generated_string = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choices(generated_string, k=int(password_length_input)))
                print(Message.strong_result + password)
                print(Message.goodbye)
                exit()
            elif Option.exit_program == password_length_input:
                print(Message.goodbye)
                exit()
            else:
                print(Message.wrong_input)
        else:
            print(Message.wrong_input)


while True:
    user_password_option = input(Message.new_password + prompt)
    match user_password_option:
        case Option.weak_password:
            generate_weak_password()
            continue
        case Option.strong_password:
            generate_strong_password()
        case Option.exit_program:
            print(Message.goodbye)
            exit()
        case _:
            print(Message.wrong_input)
            continue
