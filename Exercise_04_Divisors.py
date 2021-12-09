def user_divisors(number):
    divisors = 1
    while divisors <= number:
        if number % divisors == 0:
            print(divisors)
        # divisors = divisors + 1
        divisors += 1


prompt = ">>> "
user_number = int(input(f"Please choose a number\n{prompt}"))

print(f"The divisors of {user_number} are:")
user_divisors(user_number)
