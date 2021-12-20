from Exercise_16_Password_Generator.Exercise_16_Modules import *
import random
import string

weak_password_file = "weak_password.txt"
strong_password_file = "strong_password.txt"

data = generate_passwords_from_list(weak_password_list)

data_two = generate_strong_password()

with open(weak_password_file, "w") as file_object:
    file_object.write(data)

with open(strong_password_file, "w") as file_object:
    file_object.write(data_two)
