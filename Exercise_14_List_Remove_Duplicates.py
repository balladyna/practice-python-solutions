new_list_a = []


def new_list_loop(number):
    for number in range(number):
        new_list_a.append(number * number)
    print("Here is the list: " + (str(sorted(new_list_a * 3))))


def new_list_set(list_x):
    list_b = set(list_x)
    print("Here is the list without doubles: " + (str(sorted(list(list_b)))))


new_list_loop(8)
new_list_set(new_list_a)
