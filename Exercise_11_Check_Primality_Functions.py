prompt = ">>> "
user_number_message = "Choose a number to check if is prime number\n"
prime_number = "It's prime number"
not_prime_number = "It's not a prime number"
user_number = int(input(user_number_message + prompt))

half_user_number = int(user_number / 2)
divisor = 2
while True:
    if divisor <= half_user_number:
        if user_number % divisor == 0:
            print(not_prime_number)
            break
    else:
        print(prime_number)
        break
    divisor += 1
