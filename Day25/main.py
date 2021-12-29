import numpy as np


def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        seafloor = list()
        for line in file:
            seafloorline = list()
            for char in line:
                if char == ".":
                    seafloorline.append(0)
                elif char == ">":
                    seafloorline.append(1)
                elif char == "v":
                    seafloorline.append(2)
            seafloor.append(seafloorline)
    return np.array(seafloor, dtype=int)

def step(seafloor):
    moves = False
    # move >
    x, y = np.where(seafloor == 1)
    move_filter = np.where(seafloor[x, (y + 1) % seafloor.shape[1]] == 0)
    seafloor[x[move_filter], y[move_filter]] = 0
    seafloor[x[move_filter], (y[move_filter] + 1) % seafloor.shape[1]] = 1
    if move_filter[0].size > 0:
        moves = True

    # move v
    x, y = np.where(seafloor == 2)
    move_filter = np.where(seafloor[(x + 1) % seafloor.shape[0], y] == 0)
    seafloor[x[move_filter], y[move_filter]] = 0
    seafloor[(x[move_filter] + 1) % seafloor.shape[0], y[move_filter]] = 2
    if move_filter[0].size > 0:
        moves = True
    return seafloor, moves

def part1():
    seafloor = get_input()

    i = 0
    moves = True
    while moves:
        i += 1
        seafloor, moves = step(seafloor)

    print(i)


def part2():
    seafloor = get_input()

    print(step(seafloor))


if __name__ == "__main__":
    part1()
    # part2()
