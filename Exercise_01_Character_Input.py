from datetime import datetime

currentYear = datetime.now().year

prompt = '>>> '
name = input(f"What's your name?\n{prompt}")
age = int(input(f"How old are you?\n{prompt}"))

#age = int(age)
when_old = 100 + currentYear - age

print(f"Hi {name.title()}! You will be 100 years old in {when_old}!")
