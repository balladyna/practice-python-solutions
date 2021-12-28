from collections import Counter

one_1_file = open("D:\work\projects\practice-python-solutions\Exercise_22_Read_From_File\File_names.txt", "rt")
one_2_data = one_1_file.read()
one_3_words = one_2_data.split()
one_4_result = Counter(one_3_words)
print(one_4_result)

two_1_file = open("D:\work\projects\practice-python-solutions\Exercise_22_Read_From_File\category_file.txt", "rt")

new = []

for line in two_1_file:
    end = int(line.find('/sun'))
    delete_line = line[3:end]
    new.append(delete_line)

print(Counter(new))

