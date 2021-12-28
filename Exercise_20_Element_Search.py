prompt = ">>> "
user_number_message = "Please choose a number in range from 1 to 75:\n"
wrong_input_message = "Wrong input."
on_list_message = "Your number is present at index"
not_on_list_message = "Element is not in list"
user_number_input = ""

binary_search_list = [number for number in range(14, 75)]
# binary_search_list = [1, 1, 1, 1, 1, 15, 23, 25, 26, 27, 28, 29, 29, 29, 30, 31, 38, 39, 44, 44, 44, 45, 47, 88]


def binary_search(sample_list, sample_number):
    low = 0
    high = len(sample_list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if sample_list[mid] < sample_number:
            low = mid + 1
        elif sample_list[mid] > sample_number:
            high = mid - 1
        else:
            return mid
    return -1


try:
    user_number_input = int(input(user_number_message + prompt))
except ValueError as value_error:
    print(value_error)
    exit()
except EOFError as eof_error:
    print(eof_error)
    exit()

number_position = binary_search(binary_search_list, user_number_input)

if number_position != -1:
    print(on_list_message + " " + str(number_position))
else:
    print(not_on_list_message)
