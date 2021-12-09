import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = (number for number in a if number in b)
new_list = list(dict.fromkeys(new_list))

print("List no. 1:")
print(list(a))
print("\nList no. 2")
print(list(b))
print("\nCommon elements of list no. 1 and 2:")
print(list(new_list))

random_list_a = random.sample(range(0, 30), 10)
random_list_b = random.sample(range(0, 30), 14)
combined_random_lists = (random_number for random_number in random_list_a if random_number in random_list_b)
combined_random_lists = list(dict.fromkeys(combined_random_lists))

print("\nRandom list no. 1:")
print(sorted(list(random_list_a)))
print("\nRandom list no. 2:")
print(sorted(list(random_list_b)))
print("\nCommon elements of random lists:")
print(sorted(list(combined_random_lists)))
