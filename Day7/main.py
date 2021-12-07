import numpy as np


def get_input():
    with open("input.txt", "r") as file:
        list = [int(x) for x in file.read().split(",")]
    return list


def get_fuel(positions, location):
    return np.sum(np.abs(positions - location))


def test_up_down(positions, location, function):
    initial = function(positions, location)
    if function(positions, location + 1) < initial:
        return 1
    if function(positions, location - 1) < initial:
        return -1
    return 0


def part1():
    positions = np.array(get_input())
    start = int(np.floor(positions.mean()))
    change = test_up_down(positions, start, get_fuel)

    old_pos = start
    new_pos = start + change
    while get_fuel(positions, new_pos) < get_fuel(positions, old_pos):
        old_pos = new_pos
        new_pos = old_pos + change

    print(old_pos)
    print(get_fuel(positions, old_pos))


def get_fuel2(positions, location):
    steps = np.abs(positions - location)
    return np.sum(steps * (steps + 1) // 2)


def part2():
    positions = np.array(get_input())
    start = int(np.floor(positions.mean()))
    change = test_up_down(positions, start, get_fuel2)
    old_pos = start
    new_pos = start + change
    while get_fuel2(positions, new_pos) < get_fuel2(positions, old_pos):
        old_pos = new_pos
        new_pos = old_pos + change

    print(old_pos)
    print(get_fuel2(positions, old_pos))


if __name__ == "__main__":
    part1()
    part2()
