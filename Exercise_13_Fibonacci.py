prompt = ">>> "
fibonacci_numbers = "How many Fibonacci numbers do you want to generate (position \"1\" is number \"0\")?\n"

user_number = int(input(fibonacci_numbers + prompt))
fibonacci_list = [0, 1]

while True:
    a = fibonacci_list[-1] + fibonacci_list[-2]
    if user_number >= len(fibonacci_list):
        fibonacci_list.append(a)
    else:
        print(fibonacci_list[0:user_number])
        break


# Fibonacci sequence - recursive implementation of function (a function that calls itself).
# Program calculates number in selected position of Fibonacci sequence.
# Example sequence of Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, ...] etc.
# Example behavior: if user input will be '1', the output of console will be '0',
# if user input will be '1', the output of console will be '1',
# if user input will be '5', the output of console will be '3'.


def fibonacci_sequence(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    return fibonacci_sequence(number - 1) + fibonacci_sequence(number - 2)


print("Recursive Fibonacci function result: " + (str(fibonacci_sequence(user_number - 1))))
