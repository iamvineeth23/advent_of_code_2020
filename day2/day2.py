
## advent of code - day 2
## Author: Vineeth

file = open("input.txt", "r")
content=file.readlines()

part_1 = 0
part_2 = 0
for data in content:

    split_list = data.split()
    num = split_list[0].split(sep='-')

    min = int(num[0])
    max = int(num[1])

    letter = split_list[1][0]
    password = split_list[2]

    if min <= password.count(letter) <= max:
        part_1 += 1

    if (password[min-1] == letter) ^ (password[max-1] == letter):
        part_2 += 1


print("Part 1: ", part_1)
print("Part 2: ", part_2)
