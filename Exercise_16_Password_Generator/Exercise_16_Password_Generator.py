from Exercise_16_Modules import *


while True:
    user_password_option = input(Message.new_password + prompt)
    match user_password_option:
        case Option.weak_password:
            generate_weak_password()
            continue
        case Option.strong_password:
            generate_strong_password_loop()
        case Option.exit_program:
            print(Message.goodbye)
            exit()
        case _:
            print(Message.wrong_input)
            continue
