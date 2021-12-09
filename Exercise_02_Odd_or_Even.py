prompt = "\n>>> "
num = int(input(f"Hi, choose a number, we will check if it is even or odd: {prompt}"))

modulo_result = num % 2
modulo_result_two = num % 4

if modulo_result_two == 0:
    print("This number is multiple of 4! That also means that it is an even number.")
elif modulo_result == 0:
    print("We found an even number!")
else:
    print("This number is odd.")

check = int(input(f"Please choose a divider: {prompt}"))

divided_number = num % check

if divided_number == 0:
    print(f"{num} divides evenly by {check}")
else:
    print(f"{num} not divides evenly by {check}")
