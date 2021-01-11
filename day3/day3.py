
## advent of code - day 3
## Author: Vineeth


with open("input.txt") as file:
    content = [line[0:-1] for line in file]

# print(len(content))

right = 3
down = 1
width = len(content[0])


def path(right, down):

    count = 0
    x = 0
    y = 0

    while y < len(content)-1:

        x += right
        y += down

        if x >= width:
            x -= width

        if content[y][x] == "#":
            count += 1

    return count


print("Part 1: ", path(3,1))
print("Part 2: ", path(1,1)*path(3,1)*path(5,1)*path(7,1)*path(1,2))
