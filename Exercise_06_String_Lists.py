prompt = ">>> "
user_string = input(f"Choose a string. We will check, if it is palindrome:\n{prompt}")

reversed_string = user_string[::-1]

if reversed_string == user_string:
    print(f"Number {user_string} is palindrome.")
else:
    print(f"Sorry, {user_string} it's not palindrome")
