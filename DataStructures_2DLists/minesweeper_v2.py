"""
Create a file named minesweeper.py
Create a function that takes a grid of # and -, where each hash (#) represents
a mine and each dash (-) represents a mine-free spot.
Return a grid, where each dash is replaced by a digit, indicating the number of
mines immediately adjacent to the spot i.e. horizonatally, vertically and diagonally.

"""


# function to verify if a character in the patter is the below symbol
def is_bomb(data):
    return data == "#"


# checks if within boundaries
def in_bounds(x, y, len_x, len_y):
    return x >= 0 and y >= 0 and x < len_x and y < len_y


# function to accept 2d array, checking coordindates
def minesweeper(data):
    width: int = len(data[0])
    length: int = len(data)

    output = []
    for y, row in enumerate(data, start=0):
        output_row = []
        for x, value in enumerate(row, start=0):

            count = 0
            if value == "#":
                output_row.append("#")
                continue

            # NW
            if in_bounds(x - 1, y - 1, width, length) and is_bomb(data[y - 1][x - 1]):
                count += 1

            # N
            if in_bounds(x, y - 1, width, length) and is_bomb(data[y - 1][x]):
                count += 1

            # NE
            if in_bounds(x + 1, y - 1, width, length) and is_bomb(data[y - 1][x + 1]):
                count += 1

            # W
            if in_bounds(x - 1, y, width, length) and is_bomb(data[y][x - 1]):
                count += 1

            # E
            if in_bounds(x + 1, y, width, length) and is_bomb(data[y][x + 1]):
                count += 1

            # SW
            if in_bounds(x - 1, y + 1, width, length) and is_bomb(data[y + 1][x - 1]):
                count += 1

            # S
            if in_bounds(x, y + 1, width, length) and is_bomb(data[y + 1][x]):
                count += 1

            # SE
            if in_bounds(x + 1, y + 1, width, length) and is_bomb(data[y + 1][x + 1]):
                count += 1

            output_row.append(str(count))

        output.append(output_row)

    return output


def print_2d(input_data):
    for row in input_data:
        print(row)
    print()


def test_minesweeper_1():
    input_data = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
    ]

    print_2d(minesweeper(input_data))


def test_minesweeper_2():
    input_data = [
        ["-", "-"],
        ["-", "#"],
        ["-", "-"],
        ["-", "#"],
        ["-", "-"],
    ]

    print_2d(minesweeper(input_data))


def test_minesweeper_3():
    input_data = [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "#", "-", "#", "-", "#", "-", "#", "-", "#"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ]

    print_2d(minesweeper(input_data))


test_minesweeper_1()
test_minesweeper_2()
test_minesweeper_3()
