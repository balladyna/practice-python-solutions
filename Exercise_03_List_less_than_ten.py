a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

numbers_list = (less_than_five for less_than_five in a if less_than_five < 5)

print(list(numbers_list))

prompt = ">>> "

user_number = (int(input(f"Choose a number\n{prompt}")))

user_numbers_list = (less_than_user_number for less_than_user_number in a if less_than_user_number < user_number)

if user_number in a:
    print("The number is on the list. Here are numbers from the list which are less than yours.")
    print(list(user_numbers_list))
else:
    print("The number is not on the list. Here are numbers from the list which are less than yours.")
    print(list(user_numbers_list))
