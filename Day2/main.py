import numpy as np


def part1():
    moves = np.loadtxt("input.txt", dtype="str")
    hor_pos = 0
    depth = 0

    for move in moves:
        match move[0]:
            case "forward":
                hor_pos += int(move[1])
            case "down":
                depth += int(move[1])
            case "up":
                depth -= int(move[1])

    print(f"The final depth equals: {depth}")
    print(f"The final horizontal position equals: {hor_pos}")
    print(f"Multiplying them gives: {depth * hor_pos}")


def part2():
    moves = np.loadtxt("input.txt", dtype="str")

    hor_pos = 0
    depth = 0
    aim = 0

    for move in moves:
        match move[0]:
            case "forward":
                hor_pos += int(move[1])
                depth += aim * int(move[1])
            case "down":
                aim += int(move[1])
            case "up":
                aim -= int(move[1])

    print(f"The final depth equals: {depth}")
    print(f"The final horizontal position equals: {hor_pos}")
    print(f"Multiplying them gives: {depth * hor_pos}")
    print(f"The final aim equals: {aim}")


if __name__ == "__main__":
    part1()
    part2()
