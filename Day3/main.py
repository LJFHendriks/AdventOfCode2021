import numpy as np


def part1():
    numbers = np.loadtxt("input.txt", dtype="str")
    total = [0 for i in numbers[0]]
    for number in numbers:
        for i, value in enumerate(number):
            total[i] += int(value)
    fraction = [value / len(numbers) for value in total]
    gamma_rate = ""
    epsilon_rate = ""
    for value in fraction:
        if value >= 0.5:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))

def scrub(numbers, index, tup):
    if len(numbers) < 2:
        return numbers[0]
    total = 0
    for number in numbers:
        total += int(number[index])
    fraction = total / len(numbers)
    if fraction >= 0.5:
        return scrub(list(filter(lambda number: number[index] == tup[0], numbers)), index + 1, tup)
    else:
        return scrub(list(filter(lambda number: number[index] == tup[1], numbers)), index + 1, tup)



def part2():
    numbers = np.loadtxt("input.txt", dtype="str")

    oxygen_generator_rating = int(scrub(numbers, 0, ("1", "0")), 2)
    c02_scrubber_rating = int(scrub(numbers, 0, ("0", "1")), 2)

    print(oxygen_generator_rating * c02_scrubber_rating)


if __name__ == "__main__":
    part1()
    part2()
