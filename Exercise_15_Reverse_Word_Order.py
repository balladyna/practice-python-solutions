prompt = ">>> "
user_message = input(f"Write here few words and I will revise order of them:\n{prompt}")

user_list = []


def create_list(new_list):
    new_list = user_message.split()
    new_list.reverse()
    print(new_list)

create_list(user_list)
